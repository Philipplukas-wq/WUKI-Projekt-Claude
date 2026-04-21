"use client";

import { signOut, useSession } from "next-auth/react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import Image from "next/image";

const navLinks = [
  { href: "/dashboard", label: "Startseite" },
  { href: "/wissenshub", label: "Wissenshub" },
  { href: "/wu-chat", label: "WU-Berater" },
];

export default function Navbar() {
  const pathname = usePathname();
  const { data: session } = useSession();

  return (
    <nav className="bg-[#1F3A45] shadow-md sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo & Name */}
          <Link href="/dashboard" className="flex items-center gap-3 group">
            <div className="relative w-11 h-11 rounded-lg overflow-hidden flex-shrink-0">
              <Image
                src="/wappen.png"
                alt="WU-Berater"
                fill
                className="object-cover"
              />
            </div>
            <span className="text-white font-semibold text-base tracking-wide group-hover:text-[#B8E0F0] transition">
              WU-Berater
            </span>
          </Link>

          {/* Navigation Links */}
          <div className="hidden md:flex items-center gap-1">
            {navLinks.map((link) => {
              const active = pathname === link.href || pathname.startsWith(link.href + "/");
              return (
                <Link
                  key={link.href}
                  href={link.href}
                  className={`px-4 py-2 rounded-md text-sm font-medium transition ${
                    active
                      ? "bg-[#5BA654] text-white"
                      : "text-white/70 hover:text-white hover:bg-white/10"
                  }`}
                >
                  {link.label}
                </Link>
              );
            })}
          </div>

          {/* Nutzer & Logout */}
          <div className="flex items-center gap-3">
            {session?.user?.email && (
              <span className="hidden sm:block text-white/50 text-xs">
                {session.user.email}
              </span>
            )}
            <button
              onClick={() => signOut({ callbackUrl: "/login" })}
              className="text-white/70 hover:text-white text-sm px-3 py-1.5 rounded-md border border-white/20 hover:border-white/50 transition"
            >
              Abmelden
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Navigation */}
      <div className="md:hidden border-t border-white/10 px-4 pb-3 pt-2 flex gap-1">
        {navLinks.map((link) => {
          const active = pathname === link.href;
          return (
            <Link
              key={link.href}
              href={link.href}
              className={`flex-1 text-center px-2 py-1.5 rounded text-xs font-medium transition ${
                active
                  ? "bg-[#5BA654] text-white"
                  : "text-white/60 hover:text-white hover:bg-white/10"
              }`}
            >
              {link.label}
            </Link>
          );
        })}
      </div>
    </nav>
  );
}
