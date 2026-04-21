import type { Metadata } from "next";
import WissenshubCard from "@/components/WissenshubCard";

export const metadata: Metadata = {
  title: "Wissenshub – WU-Berater",
  description:
    "Rechtsgrundlagen, Methoden und Praxiswissen zu Wirtschaftlichkeitsuntersuchungen gemäß § 7 BHO und AR A-2400/62 für Bundeswehr und öffentliche Verwaltung.",
};

const categories = [
  {
    section: "Grundlagen",
    items: [
      {
        title: "Was ist eine WU?",
        description:
          "Eine Wirtschaftlichkeitsuntersuchung (WU) ist ein strukturiertes Verfahren zum Nachweis des wirtschaftlichen Mitteleinsatzes. Sie vergleicht Handlungsalternativen anhand monetärer und nicht-monetärer Kriterien und mündet in einem begründeten Entscheidungsvorschlag.",
        icon: "📖",
      },
      {
        title: "Rechtsgrundlagen",
        description:
          "§ 7 BHO verpflichtet alle Bundesbehörden zur WU bei finanzwirksamen Maßnahmen. § 6 BHO regelt die Notwendigkeit der Ausgaben. Die AR A-2400/62 der Bundeswehr konkretisiert Struktur, Inhalt und Dokumentationsanforderungen.",
        icon: "⚖️",
        badge: "Wichtig",
      },
      {
        title: "WU-Typen im Überblick",
        description:
          "Unterjährig: einmaliger Kauf ohne Folgekosten innerhalb eines Haushaltsjahres. Überjährig: mehrjährige Investitionen mit Kapitalwertberechnung. Dienstleistung: Make-or-Buy-Entscheidung bei externer Leistungserbringung (Reinigung, IT, Bewachung u. a.).",
        icon: "🗂️",
      },
    ],
  },
  {
    section: "Durchführung",
    items: [
      {
        title: "Bedarfsforderung formulieren",
        description:
          "Die Bedarfsforderung muss gemäß § 6 BHO funktional und lösungsneutral formuliert sein – sie beschreibt das Ziel, nicht die Lösung. Pflichtbestandteile: qualitative Anforderungen (Funktion, Mindeststandards) und quantitative Angaben (Stückzahl, Häufigkeit, Umfang).",
        icon: "✍️",
      },
      {
        title: "Marktpreisrecherche",
        description:
          "Aktuelle Marktpreise sind Grundlage jeder WU. Zu dokumentieren sind: Produktbezeichnung, Preis, Anbieter, URL und Abrufdatum. Der WU-Berater führt automatisch eine Webrecherche durch und legt die Ergebnisse strukturiert in der Anlage Marktrecherche ab.",
        icon: "🔍",
      },
      {
        title: "Personalkosten (PSK)",
        description:
          "Personalkosten werden auf Basis des Personalkosten-Sachkosten-Katalogs (PSK 2024) berechnet. Der WU-Berater schlägt automatisch die korrekten Vollkostensätze für alle Besoldungs- und Entgeltgruppen (E1–E15, A3–A16) vor.",
        icon: "👤",
      },
      {
        title: "Kapitalwertmethode",
        description:
          "Bei überjährigen WUs werden alle Zahlungsströme auf den Betrachtungsbeginn abgezinst und als Kapitalwert ausgewiesen. Kalkulationszinssatz: 1,2 % (BMF, April 2026). Preissteigerungsraten werden nach Kostenkategorie differenziert berücksichtigt.",
        icon: "📊",
      },
    ],
  },
  {
    section: "Häufige Fragen",
    items: [
      {
        title: "FAQ",
        description:
          "Wann ist eine WU Pflicht? Was unterscheidet eine unterjährige von einer überjährigen WU? Wie wird der Betrachtungszeitraum festgelegt? Muss immer eine Nutzwertanalyse durchgeführt werden? Antworten auf die häufigsten Fragen rund um die WU-Erstellung.",
        icon: "❓",
      },
      {
        title: "Typische Fehler",
        description:
          "Fehlende Quantifizierung in der Bedarfsforderung, vorab festgelegte Ergebnisse (keine Ergebnisoffenheit), unvollständige Optionsbetrachtung, fehlende Quellenangaben bei Marktpreisen oder unzureichende Risikobetrachtung – diese Mängel führen häufig zur Zurückweisung durch Vorgesetzte oder Prüfinstanzen.",
        icon: "⚠️",
        badge: "Hinweis",
      },
    ],
  },
  {
    section: "Downloads",
    items: [
      {
        title: "Template WU unterjährig",
        description:
          "Offizielle Excel-Vorlage für einmalige Beschaffungen innerhalb eines Haushaltsjahres. Enthält alle Pflichtfelder gemäß AR A-2400/62: Bedarfsforderung, Ausschluss von Alternativen, Kostenermittlung und Abschlusscheckliste.",
        icon: "📥",
        badge: "XLSM",
      },
      {
        title: "Template WU überjährig",
        description:
          "Word-Vorlage für mehrjährige Investitionen und komplexe Maßnahmen. Struktur nach den 9 Pflichtgliederungspunkten der AR A-2400/62: Bedarfsforderung, Ausgangslage, Optionen, Annahmen, Kapitalwertberechnung, Sensitivitätsanalyse und Entscheidungsvorschlag.",
        icon: "📥",
        badge: "DOCX",
      },
      {
        title: "Template Dienstleistung",
        description:
          "Excel-Vorlage für Make-or-Buy-Entscheidungen bei externer Leistungserbringung. Vorstrukturiert für die vier Standardoptionen: Eigenbetrieb, bundeswehrinterne Lösung, Inhousegesellschaft und externen Dienstleister – inkl. Kostenvergleich und Risikobetrachtung.",
        icon: "📥",
        badge: "XLSM",
      },
    ],
  },
];

export default function WissenshubPage() {
  return (
    <div className="max-w-7xl mx-auto px-6 py-10">

      {/* Seiten-Header */}
      <div className="mb-8">
        <div className="flex items-center gap-3 mb-2">
          <div className="w-8 h-8 rounded-lg bg-[#2d3142] flex items-center justify-center text-white text-sm">
            📚
          </div>
          <h1 className="text-[#2d3142] font-semibold text-xl">Wissenshub</h1>
        </div>
        <p className="text-[#4a4e69] text-sm max-w-2xl leading-relaxed">
          Fundiertes Praxiswissen zu Wirtschaftlichkeitsuntersuchungen gemäß § 7 BHO
          und AR A-2400/62 – von den Rechtsgrundlagen über Bewertungsmethoden bis zu
          häufigen Fehlern und offiziellen Vorlagen.
        </p>
        <div className="mt-3 h-0.5 bg-[#e0e0e0] rounded" />
      </div>

      {/* Kategorien */}
      <div className="space-y-8">
        {categories.map((cat) => (
          <div key={cat.section}>
            <h2 className="text-[#2d3142] font-semibold text-sm uppercase tracking-wider mb-3 flex items-center gap-2">
              <span className="w-4 h-0.5 bg-[#4a5c3c] rounded" />
              {cat.section}
            </h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
              {cat.items.map((item) => (
                <WissenshubCard
                  key={item.title}
                  title={item.title}
                  description={item.description}
                  icon={item.icon}
                  badge={item.badge}
                />
              ))}
            </div>
          </div>
        ))}
      </div>

    </div>
  );
}
