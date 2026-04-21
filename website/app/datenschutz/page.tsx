import Link from "next/link";

export default function DatenschutzPage() {
  return (
    <div className="min-h-screen bg-[#f5f5f5] text-[#1a1a1a]">
      {/* Header */}
      <header className="bg-white border-b border-[#e0e0e0] px-8 py-6">
        <div className="max-w-4xl mx-auto">
          <Link href="/login" className="flex items-center gap-3 mb-4 w-fit hover:opacity-80">
            <div className="w-8 h-8 rounded-lg overflow-hidden flex items-center justify-center">
              <img
                src="/wappen.png"
                alt="WU-Berater"
                className="w-full h-full object-contain"
              />
            </div>
            <span className="font-semibold text-[#1a1a1a]">WU-Berater</span>
          </Link>
          <h1 className="text-3xl font-bold text-[#1a1a1a]">Datenschutzerklärung</h1>
        </div>
      </header>

      {/* Content */}
      <main className="max-w-4xl mx-auto px-8 py-12">
        <div className="bg-white rounded-lg shadow-sm p-8 space-y-6">
          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">1. Datenschutzverantwortlicher</h2>
            <div className="text-sm text-[#555] space-y-2">
              <p>
                <strong>Verantwortlich für die Datenverarbeitung:</strong><br />
                Philipp Lukas<br />
                Kölnstraße 70<br />
                53111 Bonn<br />
                E-Mail: <a href="mailto:Philipp.lukas@outlook.de" className="text-[#5BA654] hover:underline">Philipp.lukas@outlook.de</a>
              </p>
            </div>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">2. Erfassung und Verarbeitung personenbezogener Daten</h2>
            <p className="text-sm text-[#555] mb-4">
              Diese Plattform erhebt und verarbeitet personenbezogene Daten nur insoweit, als dies zur Bereitstellung der Dienste erforderlich ist:
            </p>
            <ul className="text-sm text-[#555] space-y-2 ml-4">
              <li><strong>Authentifizierungsdaten:</strong> E-Mail-Adresse und Authentifizierungsinformationen für den Zugriff auf den geschützten Bereich</li>
              <li><strong>Nutzungsdaten:</strong> Informationen über die Verwendung der Plattform zur Verbesserung des Dienstes</li>
              <li><strong>Inhalte:</strong> Von Ihnen erstellte Wirtschaftlichkeitsuntersuchungen und damit verbundene Dokumentationen</li>
            </ul>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">3. Rechtsgrundlage der Verarbeitung</h2>
            <p className="text-sm text-[#555]">
              Die Verarbeitung personenbezogener Daten erfolgt auf Grundlage Ihrer ausdrücklichen Zustimmung (Art. 6 Abs. 1 a) DSGVO) und insoweit erforderlich zur Erfüllung vertraglicher Verpflichtungen (Art. 6 Abs. 1 b) DSGVO). Darüber hinaus beruht die Verarbeitung auf berechtigten Interessen zur Gewährleistung der Sicherheit und zum ordnungsgemäßen Betrieb der Plattform (Art. 6 Abs. 1 f) DSGVO).
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">4. Speicherdauer</h2>
            <p className="text-sm text-[#555]">
              Ihre personenbezogenen Daten werden gespeichert, solange Ihr Benutzerkonto aktiv ist. Nach Beendigung der Nutzung werden Ihre Daten gelöscht, soweit gesetzliche Aufbewahrungspflichten nicht entgegenstehen. Von Ihnen erstellte Wirtschaftlichkeitsuntersuchungen werden entsprechend Ihren Anweisungen verwaltet und können auf Anfrage gelöscht werden.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">5. Empfänger der Daten</h2>
            <p className="text-sm text-[#555]">
              Ihre Daten werden nicht an Dritte weitergegeben, außer wenn dies gesetzlich erforderlich ist oder Sie ausdrücklich zugestimmt haben. Die technische Verarbeitung erfolgt durch Dienstleister, die unter strikten Datenschutzvereinbarungen tätig sind.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">6. Ihre Rechte</h2>
            <p className="text-sm text-[#555] mb-3">
              Sie haben das Recht:
            </p>
            <ul className="text-sm text-[#555] space-y-2 ml-4">
              <li><strong>Recht auf Auskunft:</strong> Sie können jederzeit Auskunft über die von uns gespeicherten personenbezogenen Daten verlangen.</li>
              <li><strong>Recht auf Berichtigung:</strong> Sie können die Berichtigung unrichtiger Daten verlangen.</li>
              <li><strong>Recht auf Löschung:</strong> Sie können die Löschung Ihrer Daten verlangen, sofern keine gesetzlichen Aufbewahrungspflichten bestehen.</li>
              <li><strong>Recht auf Einschränkung:</strong> Sie können die Einschränkung der Verarbeitung verlangen.</li>
              <li><strong>Recht auf Datenübertragbarkeit:</strong> Sie können verlangen, dass Ihre Daten in einem strukturierten Format zur Verfügung gestellt werden.</li>
              <li><strong>Widerspruchsrecht:</strong> Sie können der Verarbeitung widersprechen.</li>
            </ul>
            <p className="text-sm text-[#555] mt-4">
              Zur Ausübung dieser Rechte kontaktieren Sie bitte: <a href="mailto:Philipp.lukas@outlook.de" className="text-[#5BA654] hover:underline">Philipp.lukas@outlook.de</a>
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">7. Datensicherheit</h2>
            <p className="text-sm text-[#555]">
              Wir setzen technische und organisatorische Maßnahmen ein, um Ihre Daten vor unbefugtem Zugriff, Verlust oder Verfälschung zu schützen. Dazu gehören Verschlüsselung, sichere Authentifizierung und regelmäßige Sicherheitsüberprüfungen. Trotz aller Bemühungen können wir absolute Sicherheit nicht garantieren.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">8. Cookies und Tracking</h2>
            <p className="text-sm text-[#555]">
              Diese Plattform verwendet Cookies nur insoweit erforderlich für die Authentifizierung und zur Aufrechterhaltung Ihrer Sitzung. Wir verwenden kein Tracking oder Analyse-Tools, die personenbezogene Daten über Dritte hinweg verfolgen.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">9. Kontakt und Beschwerden</h2>
            <p className="text-sm text-[#555]">
              Für Fragen zum Datenschutz oder zur Ausübung Ihrer Rechte kontaktieren Sie bitte:<br />
              <a href="mailto:Philipp.lukas@outlook.de" className="text-[#5BA654] hover:underline">Philipp.lukas@outlook.de</a>
            </p>
            <p className="text-sm text-[#555] mt-4">
              Sie haben das Recht, sich bei der zuständigen Datenschutzbehörde zu beschweren, wenn Sie der Ansicht sind, dass Ihre Daten nicht gemäß dieser Datenschutzerklärung und der geltenden Datenschutzgesetze verarbeitet werden.
            </p>
          </section>

          <section className="border-t pt-6">
            <p className="text-xs text-[#999]">
              Letzte Aktualisierung: April 2026
            </p>
          </section>
        </div>

        <div className="mt-8 text-center">
          <Link
            href="/login"
            className="inline-block px-6 py-2 bg-[#5BA654] text-white rounded-md hover:bg-[#4A8F47] transition text-sm font-medium"
          >
            Zurück zur Anmeldung
          </Link>
        </div>
      </main>
    </div>
  );
}
