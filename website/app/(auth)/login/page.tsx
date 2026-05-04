"use client";

import { Suspense, useState } from "react";
import { signIn } from "next-auth/react";
import { useRouter, useSearchParams } from "next/navigation";
import Image from "next/image";
import Footer from "@/components/Footer";

function LoginPageContent() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const error = searchParams.get("error");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setIsLoading(true);

    const result = await signIn("credentials", {
      email,
      password,
      redirect: false,
    });

    setIsLoading(false);

    if (result?.ok) {
      router.push("/dashboard");
    } else {
      // Fehler anzeigen
      console.error("Login failed:", result?.error);
    }
  }

  return (
    <div className="min-h-screen flex flex-col" style={{ background: "linear-gradient(135deg, #1F3A45 0%, #2B5A6F 60%, #3B7A8F 100%)" }}>
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

        <div className="hidden sm:block absolute top-0 right-0 opacity-25 pointer-events-none" style={{ width: "320px", height: "320px" }}>
          <img
            src="/berater.png"
            alt=""
            className="w-full h-full object-contain"
            style={{
              filter: "drop-shadow(0 8px 24px rgba(91,166,84,0.15))",
            }}
            draggable={false}
          />
        </div>
      </header>

      <div className="flex flex-1 items-center justify-center px-4">
        <div className="w-full max-w-md">
          <div className="bg-white rounded-lg shadow-2xl overflow-hidden">
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
                <h1 className="text-white font-semibold text-xl">Willkommen</h1>
                <p className="text-white/60 text-sm mt-1">
                  Test-Anmeldung (ohne Keycloak)
                </p>
              </div>
            </div>

            <div className="px-8 py-7 space-y-5">
              {error && (
                <div className="bg-red-50 border border-red-200 text-red-700 text-sm px-4 py-3 rounded-md">
                  {error === "suspended"
                    ? "Ihr Konto wurde gesperrt."
                    : "Anmeldung fehlgeschlagen"}
                </div>
              )}

              <form onSubmit={handleSubmit} className="space-y-3">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    E-Mail
                  </label>
                  <input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="philipp.lukas@outlook.de"
                    className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-[#5BA654]"
                    disabled={isLoading}
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Passwort
                  </label>
                  <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Passwort eingeben"
                    className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-[#5BA654]"
                    disabled={isLoading}
                  />
                </div>

                <button
                  type="submit"
                  disabled={isLoading}
                  className="w-full bg-[#5BA654] hover:bg-[#4A8F47] disabled:opacity-50 text-white font-medium py-2.5 px-4 rounded-md transition text-sm"
                >
                  {isLoading ? "Wird angemeldet..." : "Anmelden"}
                </button>
              </form>
            </div>
          </div>

          <p className="text-center text-white/30 text-xs mt-6">
            Test-Modus · WU-Berater v1.0
          </p>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default function LoginPage() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <LoginPageContent />
    </Suspense>
  );
}
