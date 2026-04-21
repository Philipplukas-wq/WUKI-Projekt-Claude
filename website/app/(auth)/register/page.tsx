"use client";

import { useState, FormEvent } from "react";
import Link from "next/link";
import Image from "next/image";

export default function RegisterPage() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  async function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setError(null);
    setSuccess(false);

    if (formData.password !== formData.confirmPassword) {
      setError("Passwörter stimmen nicht überein");
      return;
    }

    if (formData.password.length < 6) {
      setError("Passwort muss mindestens 6 Zeichen lang sein");
      return;
    }

    setLoading(true);

    try {
      const response = await fetch("/api/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: formData.name,
          email: formData.email,
          password: formData.password,
        }),
      });

      if (response.ok) {
        setSuccess(true);
        setFormData({ name: "", email: "", password: "", confirmPassword: "" });
        setTimeout(() => {
          window.location.href = "/login";
        }, 2000);
      } else {
        const data = await response.json();
        setError(data.error || "Registrierung fehlgeschlagen");
      }
    } catch (err) {
      setError("Fehler bei der Registrierung");
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen flex flex-col" style={{ background: "linear-gradient(135deg, #1F3A45 0%, #2B5A6F 60%, #3B7A8F 100%)" }}>
      {/* Header */}
      <header className="relative px-8 sm:px-12 py-8 flex items-start justify-between flex-shrink-0">
        <div className="flex items-center gap-3">
          <div className="w-12 h-12 rounded-lg overflow-hidden flex items-center justify-center flex-shrink-0">
            <img
              src="/wappen.png"
              alt="WU-Berater"
              className="w-full h-full object-contain"
            />
          </div>
          <div>
            <h2 className="text-white font-semibold text-lg tracking-tight">WU-Berater</h2>
            <p className="text-white/50 text-xs">Wirtschaftlichkeitsuntersuchungen</p>
          </div>
        </div>
      </header>

      {/* Register Form */}
      <div className="flex flex-1 items-center justify-center px-4">
        <div className="w-full max-w-md">
          <div className="bg-white rounded-lg shadow-2xl overflow-hidden">
            {/* Card Header */}
            <div className="bg-[#1F3A45] px-8 py-6 flex flex-col items-center gap-3">
              <div className="relative w-20 h-20">
                <Image
                  src="/wappen.png"
                  alt="WU-Berater"
                  fill
                  className="object-contain"
                  priority
                />
              </div>
              <div className="text-center">
                <h1 className="text-white font-semibold text-xl">Registrierung</h1>
                <p className="text-white/60 text-sm mt-1">
                  Neues Konto erstellen
                </p>
              </div>
            </div>

            {/* Form */}
            <form onSubmit={handleSubmit} className="px-8 py-7 space-y-5">
              <div>
                <label
                  htmlFor="name"
                  className="block text-sm font-medium text-[#2d3142] mb-1.5"
                >
                  Name
                </label>
                <input
                  id="name"
                  type="text"
                  required
                  value={formData.name}
                  onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                  className="w-full px-4 py-2.5 border border-[#e0e0e0] rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-[#5BA654] focus:border-transparent transition"
                  placeholder="Ihr Name"
                />
              </div>

              <div>
                <label
                  htmlFor="email"
                  className="block text-sm font-medium text-[#2d3142] mb-1.5"
                >
                  E-Mail-Adresse
                </label>
                <input
                  id="email"
                  type="email"
                  required
                  value={formData.email}
                  onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                  className="w-full px-4 py-2.5 border border-[#e0e0e0] rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-[#5BA654] focus:border-transparent transition"
                  placeholder="name@beispiel.de"
                />
              </div>

              <div>
                <label
                  htmlFor="password"
                  className="block text-sm font-medium text-[#2d3142] mb-1.5"
                >
                  Passwort
                </label>
                <input
                  id="password"
                  type="password"
                  required
                  value={formData.password}
                  onChange={(e) => setFormData({ ...formData, password: e.target.value })}
                  className="w-full px-4 py-2.5 border border-[#e0e0e0] rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-[#5BA654] focus:border-transparent transition"
                  placeholder="••••••••"
                />
              </div>

              <div>
                <label
                  htmlFor="confirmPassword"
                  className="block text-sm font-medium text-[#2d3142] mb-1.5"
                >
                  Passwort wiederholen
                </label>
                <input
                  id="confirmPassword"
                  type="password"
                  required
                  value={formData.confirmPassword}
                  onChange={(e) => setFormData({ ...formData, confirmPassword: e.target.value })}
                  className="w-full px-4 py-2.5 border border-[#e0e0e0] rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-[#5BA654] focus:border-transparent transition"
                  placeholder="••••••••"
                />
              </div>

              {error && (
                <div className="bg-red-50 border border-red-200 text-red-700 text-sm px-4 py-3 rounded-md">
                  {error}
                </div>
              )}

              {success && (
                <div className="bg-green-50 border border-green-200 text-green-700 text-sm px-4 py-3 rounded-md">
                  Registrierung erfolgreich! Weiterleitung zum Login...
                </div>
              )}

              <button
                type="submit"
                disabled={loading}
                className="w-full bg-[#5BA654] hover:bg-[#4A8F47] disabled:opacity-60 text-white font-medium py-2.5 px-4 rounded-md transition text-sm"
              >
                {loading ? "Wird registriert…" : "Registrieren"}
              </button>
            </form>

            {/* Login Link */}
            <div className="px-8 py-4 bg-[#f5f5f5] border-t border-[#e0e0e0]">
              <p className="text-center text-sm text-[#666]">
                Schon registriert?{" "}
                <Link href="/login" className="text-[#5BA654] font-semibold hover:underline">
                  Jetzt anmelden
                </Link>
              </p>
            </div>
          </div>

          <p className="text-center text-white/30 text-xs mt-6">
            Nur für autorisierte Nutzer · WU-Berater v1.0
          </p>
        </div>
      </div>
    </div>
  );
}
