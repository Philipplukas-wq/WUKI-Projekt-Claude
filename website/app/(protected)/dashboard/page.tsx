import type { Metadata } from "next";
import WukiHero from "@/components/WukiHero";
import Link from "next/link";

export const metadata: Metadata = {
  title: "Dashboard – WU-Berater",
  description:
    "Erstellen Sie Wirtschaftlichkeitsuntersuchungen gemäß § 7 BHO – geführt, rechtssicher und vollständig dokumentiert.",
};

const moduleCards = [
  {
    title: "WU-Berater",
    description:
      "Geführter Dialog zur Erstellung einer vollständigen, rechtssicheren Wirtschaftlichkeitsuntersuchung – von der Bedarfsforderung bis zur Abschlusscheckliste.",
    icon: "💬",
    href: "/wu-chat",
    color: "#5BA654",
  },
  {
    title: "Wissenshub",
    description:
      "Rechtsgrundlagen, Methoden und Praxiswissen rund um § 7 BHO, AR A-2400/62 und die korrekte Durchführung von Wirtschaftlichkeitsuntersuchungen.",
    icon: "📚",
    href: "/wissenshub",
    color: "#4A90A4",
  },
  {
    title: "Meine WUs",
    description:
      "Greifen Sie auf bereits erstellte Wirtschaftlichkeitsuntersuchungen zu, vergleichen Sie Versionen und verwalten Sie Ihre Dokumente zentral.",
    icon: "📁",
    href: "#",
    color: "#3B7A8F",
    disabled: true,
  },
];

export default function DashboardPage() {
  return (
    <div>
      <WukiHero />

      <div className="max-w-7xl mx-auto px-6 py-12">

        {/* Module */}
        <div className="mb-10">
          <h2 className="text-[#1F3A45] font-semibold text-lg mb-1">
            Ihre Arbeitsbereiche
          </h2>
          <p className="text-[#4A90A4] text-sm mb-6">
            Wählen Sie ein Modul, um direkt loszulegen. Der WU-Berater führt Sie
            Schritt für Schritt durch den gesamten Prozess.
          </p>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {moduleCards.map((card) => (
              <Link
                key={card.title}
                href={card.href}
                className={`group block bg-white rounded-lg border border-[#e0e0e0] p-6 transition-all ${
                  card.disabled
                    ? "opacity-50 cursor-not-allowed pointer-events-none"
                    : "hover:border-[#5BA654] hover:shadow-md"
                }`}
              >
                <div
                  className="w-10 h-10 rounded-lg flex items-center justify-center text-2xl mb-4"
                  style={{ background: `${card.color}15` }}
                >
                  {card.icon}
                </div>
                <h3 className="text-[#1F3A45] font-semibold text-sm mb-1.5">
                  {card.title}
                </h3>
                <p className="text-[#4A90A4] text-xs leading-relaxed">
                  {card.description}
                </p>
                {card.disabled && (
                  <span className="inline-block mt-3 text-[#4A90A4]/50 text-xs">
                    Demnächst verfügbar
                  </span>
                )}
                {!card.disabled && (
                  <span className="inline-block mt-4 text-[#5BA654] text-xs font-medium group-hover:underline">
                    Öffnen →
                  </span>
                )}
              </Link>
            ))}
          </div>
        </div>

        {/* Info-Banner */}
        <div className="bg-[#1F3A45] rounded-lg p-6 text-white">
          <div className="flex items-start gap-4">
            <div className="text-xl flex-shrink-0 mt-0.5">⚖️</div>
            <div>
              <h3 className="font-semibold text-sm mb-1.5">
                Wirtschaftlichkeitsuntersuchungen sind Pflicht
              </h3>
              <p className="text-white/60 text-xs leading-relaxed max-w-3xl">
                Gemäß § 7 Bundeshaushaltsordnung (BHO) sind für alle finanzwirksamen
                Maßnahmen Wirtschaftlichkeitsuntersuchungen durchzuführen. Für die
                Bundeswehr konkretisiert die AR A-2400/62 die Anforderungen an Inhalt,
                Struktur und Dokumentation. Der WU-Berater stellt sicher, dass Ihre
                Untersuchung alle Pflichtanforderungen erfüllt und prüfungssicher
                dokumentiert ist.
              </p>
            </div>
          </div>
        </div>

      </div>
    </div>
  );
}
