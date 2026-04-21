import Link from "next/link";

export default function NutzungsbedingungenPage() {
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
          <h1 className="text-3xl font-bold text-[#1a1a1a]">Nutzungsbedingungen</h1>
        </div>
      </header>

      {/* Content */}
      <main className="max-w-4xl mx-auto px-8 py-12">
        <div className="bg-white rounded-lg shadow-sm p-8 space-y-6">
          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">1. Geltungsbereich und Nutzerkreis</h2>
            <p className="text-sm text-[#555]">
              Diese Nutzungsbedingungen regeln die Nutzung der Plattform WU-Berater. Die Plattform ist nur für autorisierte Nutzer zugänglich. Der Zugriff ist auf Personen beschränkt, denen dies ausdrücklich gestattet wurde. Mit der Anmeldung und Nutzung der Plattform erkennen Sie diese Nutzungsbedingungen an.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">2. Registrierung und Authentifizierung</h2>
            <div className="text-sm text-[#555] space-y-3">
              <p>
                <strong>2.1 Erforderliche Informationen:</strong><br />
                Zur Registrierung müssen Sie gültige Anmeldedaten bereitstellen. Sie sind allein verantwortlich für die Richtigkeit der von Ihnen angegebenen Informationen.
              </p>
              <p>
                <strong>2.2 Geheimhaltung von Zugangsdaten:</strong><br />
                Sie verpflichten sich, Ihr Passwort geheim zu halten und es niemandem mitzuteilen. Sie sind verantwortlich für alle Aktivitäten, die unter Ihrem Benutzerkonto stattfinden. Melden Sie unerlaubten Zugriff umgehend dem Administrator.
              </p>
              <p>
                <strong>2.3 Gültigkeit der Berechtigung:</strong><br />
                Die Berechtigung zur Nutzung der Plattform ist nicht übertragbar und endet sofort bei Entzug der Zugangserlaubnis.
              </p>
            </div>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">3. Geboten und Verboten</h2>
            <div className="text-sm text-[#555]">
              <p className="mb-3"><strong>Sie erklären sich damit einverstanden, NICHT:</strong></p>
              <ul className="space-y-2 ml-4">
                <li>• Die Plattform für rechtswidrige Zwecke zu nutzen oder Gesetze zu verletzen</li>
                <li>• Inhalte zu erstellen, die beleidigend, verleumderisch oder verleumderisch sind</li>
                <li>• Unbefugten Zugriff auf Systemressourcen zu versuchen</li>
                <li>• Malware, Viren oder andere schädliche Code hochzuladen</li>
                <li>• Andere Nutzer zu belästigen, zu bedrohen oder zu deswegen</li>
                <li>• Inhalte ohne Genehmigung zu verbreiten oder zu teilen</li>
                <li>• Die Plattform zu überlasten oder zu stören</li>
                <li>• Automatisierte Tools oder Bots zu verwenden, um auf die Plattform zuzugreifen</li>
              </ul>
            </div>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">4. Erstellung und Verwaltung von Wirtschaftlichkeitsuntersuchungen</h2>
            <div className="text-sm text-[#555] space-y-3">
              <p>
                <strong>4.1 Verantwortung für Inhalte:</strong><br />
                Sie tragen allein die Verantwortung für die Richtigkeit, Vollständigkeit und Rechtmäßigkeit der von Ihnen erstellten Wirtschaftlichkeitsuntersuchungen. Die Plattform und der Betreiber haften nicht für fehlerhafte oder unvollständige Inhalte.
              </p>
              <p>
                <strong>4.2 KI-Unterstützung:</strong><br />
                Die KI-Funktionen dienen als Hilfsmittel. Sie sind nicht verpflichtet, die von der KI bereitgestellten Vorschläge zu übernehmen. Die endgültige Verantwortung für die Inhalte liegt bei Ihnen.
              </p>
              <p>
                <strong>4.3 Rechtliche Konformität:</strong><br />
                Sie bestätigen, dass die erstellten Wirtschaftlichkeitsuntersuchungen mit der Verwaltungsvorschrift für Wirtschaftlichkeitsuntersuchungen (VV WU) gemäß § 7 BHO und allen geltenden Rechtsvorschriften konform sind.
              </p>
            </div>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">5. Verfügbarkeit und Wartung</h2>
            <p className="text-sm text-[#555]">
              Die Plattform wird bereitgestellt auf „wie vorhanden"-Basis. Wir bemühen uns, die Verfügbarkeit aufrechtzuerhalten, können aber nicht garantieren, dass die Plattform zu jeder Zeit verfügbar ist. Wartungsarbeiten und Updates können zu vorübergehenden Ausfallzeiten führen.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">6. Haftungsausschluss</h2>
            <p className="text-sm text-[#555] mb-3">
              <strong>Die Plattform wird ohne jegliche Garantie bereitgestellt.</strong> Der Betreiber haftet nicht für:
            </p>
            <ul className="text-sm text-[#555] space-y-2 ml-4">
              <li>• Fehler, Mängel oder Unterbrechungen der Plattform</li>
              <li>• Verlust oder Beschädigung von Daten</li>
              <li>• Indirekte, zufällige oder Folgeschäden</li>
              <li>• Fehler in den KI-generierten Vorschlägen oder Inhalten</li>
              <li>• Schäden durch Nutzung oder Nichtnutzung der Plattform</li>
            </ul>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">7. Datensicherung</h2>
            <p className="text-sm text-[#555]">
              Es ist Ihre Verantwortung, regelmäßige Sicherungen Ihrer erstellten Wirtschaftlichkeitsuntersuchungen zu erstellen. Der Betreiber haftet nicht für den Verlust von Daten aufgrund von technischen Fehlern oder anderen Umständen, die außerhalb seiner Kontrolle liegen.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">8. Beendigung und Kündigung</h2>
            <div className="text-sm text-[#555] space-y-3">
              <p>
                <strong>8.1 Beendigung durch Nutzer:</strong><br />
                Sie können Ihren Zugang jederzeit beenden, indem Sie sich abmelden oder den Administrator benachrichtigen.
              </p>
              <p>
                <strong>8.2 Beendigung durch Betreiber:</strong><br />
                Der Betreiber kann Ihren Zugang jederzeit ohne Angabe von Gründen beenden, wenn Sie gegen diese Nutzungsbedingungen verstoßen.
              </p>
              <p>
                <strong>8.3 Folgen der Beendigung:</strong><br />
                Nach Beendigung des Zugriffs haben Sie kein Recht, auf die Plattform oder Ihre Daten zuzugreifen, es sei denn, es gelten gesetzliche Aufbewahrungspflichten.
              </p>
            </div>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">9. Änderungen dieser Bedingungen</h2>
            <p className="text-sm text-[#555]">
              Der Betreiber behält sich das Recht vor, diese Nutzungsbedingungen jederzeit zu ändern. Änderungen werden auf dieser Seite veröffentlicht. Ihre weitere Nutzung der Plattform nach Veröffentlichung von Änderungen bedeutet Ihre Zustimmung zu den geänderten Bedingungen.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">10. Anwendbares Recht und Gerichtsstand</h2>
            <p className="text-sm text-[#555]">
              Diese Nutzungsbedingungen unterliegen deutschem Recht. Gerichtsstand für alle Streitigkeiten ist Bonn. Die Bestimmungen der DSGVO und des TMG bleiben unberührt.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">11. Kontakt</h2>
            <p className="text-sm text-[#555]">
              Für Fragen oder Bedenken zu diesen Nutzungsbedingungen kontaktieren Sie bitte:<br />
              <a href="mailto:Philipp.lukas@outlook.de" className="text-[#5BA654] hover:underline">Philipp.lukas@outlook.de</a>
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
