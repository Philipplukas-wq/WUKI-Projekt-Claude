import Link from "next/link";

export default function Footer() {
  return (
    <footer className="bg-[#1F3A45] text-white/40 text-xs text-center py-3">
      <div className="flex justify-center gap-4 flex-wrap">
        <span>WU-Berater · Wirtschaftlichkeitsuntersuchungen gemäß § 7 BHO · Nur für autorisierte Nutzer</span>
        <Link href="/impressum" className="text-white/50 hover:text-white/80 underline">
          Impressum
        </Link>
        <Link href="/datenschutz" className="text-white/50 hover:text-white/80 underline">
          Datenschutz
        </Link>
        <Link href="/nutzungsbedingungen" className="text-white/50 hover:text-white/80 underline">
          Nutzungsbedingungen
        </Link>
      </div>
    </footer>
  );
}
