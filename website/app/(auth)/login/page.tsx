"use client";

import { signIn } from "next-auth/react";
import { useState, FormEvent } from "react";
import { useRouter } from "next/navigation";
import Image from "next/image";
import Footer from "@/components/Footer";

export default function LoginPage() {
  const router = useRouter();
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setError(null);
    setLoading(true);

    const form = new FormData(e.currentTarget);
    const result = await signIn("credentials", {
      email: form.get("email") as string,
      password: form.get("password") as string,
      redirect: false,
    });

    setLoading(false);

    if (result?.ok) {
      router.push("/dashboard");
    } else {
      setError("Ungültige Zugangsdaten. Bitte versuchen Sie es erneut.");
    }
  }

  return (
    <div className="min-h-screen flex flex-col" style={{ background: "linear-gradient(135deg, #1F3A45 0%, #2B5A6F 60%, #3B7A8F 100%)" }}>
      {/* Header */}
      <header className="relative px-8 sm:px-12 py-8 flex items-start justify-between flex-shrink-0">
        {/* Logo & Branding (links) */}
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

        {/* Berater-Figur (oben rechts, subtil) */}
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

      {/* Login-Formular */}
      <div className="flex flex-1 items-center justify-center px-4">
        <div className="w-full max-w-md">
          {/* Karte */}
          <div className="bg-white rounded-lg shadow-2xl overflow-hidden">
            {/* Karten-Kopf */}
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
                  Bitte melden Sie sich an
                </p>
              </div>
            </div>

            {/* Formular */}
            <form onSubmit={handleSubmit} className="px-8 py-7 space-y-5">
              <div>
                <label
                  htmlFor="email"
                  className="block text-sm font-medium text-[#2d3142] mb-1.5"
                >
                  E-Mail-Adresse
                </label>
                <input
                  id="email"
                  name="email"
                  type="email"
                  required
                  autoComplete="email"
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
                  name="password"
                  type="password"
                  required
                  autoComplete="current-password"
                  className="w-full px-4 py-2.5 border border-[#e0e0e0] rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-[#5BA654] focus:border-transparent transition"
                  placeholder="••••••••"
                />
              </div>

              {error && (
                <div className="bg-red-50 border border-red-200 text-red-700 text-sm px-4 py-3 rounded-md">
                  {error}
                </div>
              )}

              <button
                type="submit"
                disabled={loading}
                className="w-full bg-[#5BA654] hover:bg-[#4A8F47] disabled:opacity-60 text-white font-medium py-2.5 px-4 rounded-md transition text-sm"
              >
                {loading ? "Anmelden …" : "Anmelden"}
              </button>

              <div className="text-center text-xs text-white/60">
                Noch kein Konto?{" "}
                <a href="/register" className="text-white/80 hover:text-white underline">
                  Hier registrieren
                </a>
              </div>
            </form>
          </div>

          <p className="text-center text-white/30 text-xs mt-6">
            Nur für autorisierte Nutzer · WU-Berater v1.0
          </p>
        </div>
      </div>
      <Footer />
    </div>
  );
}
