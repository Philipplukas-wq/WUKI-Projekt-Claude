"use client";

import { useSession } from "next-auth/react";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";

interface PendingUser {
  id: string;
  name: string | null;
  email: string;
  status: "PENDING" | "ACTIVE" | "SUSPENDED";
  createdAt: string;
}

export default function AdminUsersPage() {
  const { data: session } = useSession();
  const router = useRouter();
  const [users, setUsers] = useState<PendingUser[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check if user is admin
    if (session && !session.user.isAdmin) {
      router.push("/dashboard");
      return;
    }

    // Fetch pending users
    const fetchUsers = async () => {
      try {
        const res = await fetch("/api/admin/users");
        if (res.ok) {
          const data = await res.json();
          setUsers(data);
        }
      } catch (error) {
        console.error("Failed to fetch users:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchUsers();
  }, [session, router]);

  const handleApprove = async (userId: string) => {
    try {
      const res = await fetch(`/api/admin/users/${userId}/approve`, {
        method: "POST",
      });

      if (res.ok) {
        // Remove from list
        setUsers(users.filter((u) => u.id !== userId));
      } else {
        alert("Freigabe fehlgeschlagen");
      }
    } catch (error) {
      console.error("Error approving user:", error);
      alert("Fehler beim Freigeben des Nutzers");
    }
  };

  const handleSuspend = async (userId: string) => {
    if (!confirm("Nutzer wirklich sperren?")) return;

    try {
      const res = await fetch(`/api/admin/users/${userId}/suspend`, {
        method: "POST",
      });

      if (res.ok) {
        setUsers(users.filter((u) => u.id !== userId));
      } else {
        alert("Sperrung fehlgeschlagen");
      }
    } catch (error) {
      console.error("Error suspending user:", error);
      alert("Fehler beim Sperren des Nutzers");
    }
  };

  if (!session?.user.isAdmin) {
    return (
      <div className="p-6">
        <p className="text-red-600">Zugriff verweigert</p>
      </div>
    );
  }

  if (loading) {
    return (
      <div className="p-6">
        <p className="text-gray-600">Wird geladen...</p>
      </div>
    );
  }

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold mb-6 text-slate-900">
        Nutzer-Freigabe
      </h1>

      {users.length === 0 ? (
        <div className="bg-green-50 border border-green-200 rounded-lg p-6">
          <p className="text-green-900">Keine ausstehenden Freigaben.</p>
        </div>
      ) : (
        <div className="overflow-x-auto">
          <table className="w-full border-collapse">
            <thead>
              <tr className="bg-slate-100">
                <th className="border border-slate-300 px-4 py-3 text-left font-semibold text-slate-900">
                  Name
                </th>
                <th className="border border-slate-300 px-4 py-3 text-left font-semibold text-slate-900">
                  E-Mail
                </th>
                <th className="border border-slate-300 px-4 py-3 text-left font-semibold text-slate-900">
                  Registriert am
                </th>
                <th className="border border-slate-300 px-4 py-3 text-left font-semibold text-slate-900">
                  Aktionen
                </th>
              </tr>
            </thead>
            <tbody>
              {users.map((user) => (
                <tr key={user.id} className="hover:bg-slate-50">
                  <td className="border border-slate-300 px-4 py-3">
                    {user.name || "—"}
                  </td>
                  <td className="border border-slate-300 px-4 py-3">
                    {user.email}
                  </td>
                  <td className="border border-slate-300 px-4 py-3">
                    {new Date(user.createdAt).toLocaleDateString("de-DE")}
                  </td>
                  <td className="border border-slate-300 px-4 py-3 flex gap-2">
                    <button
                      onClick={() => handleApprove(user.id)}
                      className="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded text-sm font-medium transition"
                    >
                      Freigeben
                    </button>
                    <button
                      onClick={() => handleSuspend(user.id)}
                      className="bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded text-sm font-medium transition"
                    >
                      Ablehnen
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
