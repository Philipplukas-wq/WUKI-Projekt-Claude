import Link from "next/link";

export default function ImpressumPage() {
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
          <h1 className="text-3xl font-bold text-[#1a1a1a]">Impressum</h1>
        </div>
      </header>

      {/* Content */}
      <main className="max-w-4xl mx-auto px-8 py-12">
        <div className="bg-white rounded-lg shadow-sm p-8 space-y-6">
          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">Zweck und Beschreibung der Plattform</h2>
            <p className="text-sm text-[#555]">
              Diese Plattform dient als Wissensplattform für Wirtschaftlichkeitsuntersuchungen im Kontext der öffentlichen Beschaffung. In einem passwortgeschützten internen Bereich wird Benutzern die Möglichkeit eröffnet, unter Unterstützung von künstlicher Intelligenz Wirtschaftlichkeitsuntersuchungen gemäß der einschlägigen Rechtsvorschriften zu erstellen und zu dokumentieren.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">Angaben gemäß § 5 TMG</h2>
            <div className="space-y-2 text-sm">
              <p>
                <strong>Betreiber:</strong><br />
                Philipp Lukas<br />
                Kölnstraße 70<br />
                53111 Bonn<br />
                Deutschland
              </p>
              <p>
                <strong>Kontakt:</strong><br />
                E-Mail: <a href="mailto:Philipp.lukas@outlook.de" className="text-[#5BA654] hover:underline">Philipp.lukas@outlook.de</a>
              </p>
            </div>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">Vertreter</h2>
            <p className="text-sm">
              Vertreter des Betreibers i.S.d. § 7 Abs. 1 TMG:<br />
              Philipp Lukas
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">Haftung für Inhalte</h2>
            <p className="text-sm text-[#555]">
              Die Inhalte unserer Seiten wurden mit größter Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität der Inhalte können wir jedoch keine Gewähr übernehmen. Als Diensteanbieter sind wir gemäß § 7 Abs.1 TMG für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Nach § 8 bis 10 des TMG sind wir als Diensteanbieter jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen. Verpflichtungen zur Entfernung oder Sperrung der Nutzung von Informationen bleiben hiervon unberührt. Eine diesbezügliche Haftung ist jedoch erst ab dem Zeitpunkt der Kenntnis einer konkreten Rechtsverletzung möglich.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">Haftung für Links</h2>
            <p className="text-sm text-[#555]">
              Unser Angebot enthält Links zu externen Websites Dritter, auf deren Inhalte wir keinen Einfluss haben. Deshalb können wir für diese fremden Inhalte auch keine Gewähr übernehmen. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber der Seiten verantwortlich. Die verlinkten Seiten wurden zum Zeitpunkt der Verlinkung auf mögliche Rechtsverstöße überprüft. Rechtswidrige Inhalte waren zum Zeitpunkt der Verlinkung nicht erkennbar. Eine permanente inhaltliche Kontrolle der verlinkten Seiten ist jedoch ohne konkrete Anhaltspunkte einer Rechtsverletzung nicht zumutbar. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige Links umgehend entfernen.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">Urheberrecht</h2>
            <p className="text-sm text-[#555]">
              Die durch die Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht. Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der Grenzen des Urheberrechtes bedürfen der schriftlichen Zustimmung des Autors oder Rechteinhabers. Downloads und Kopien dieser Seite sind nur für den privaten, nicht kommerziellen Gebrauch gestattet. Soweit die Inhalte auf dieser Seite nicht vom Betreiber erstellt wurden, werden die Urheberrechte Dritter beachtet. Insbesondere werden Inhalte Dritter als solche gekennzeichnet. Sollten Sie trotzdem auf eine Urheberrechtsverletzung aufmerksam werden, bitten wir um einen entsprechenden Hinweis. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige Inhalte umgehend entfernen.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">Datenschutz</h2>
            <p className="text-sm text-[#555]">
              Die Nutzung unserer Website ist in der Regel ohne Angabe personenbezogener Daten möglich. Soweit auf unseren Seiten personenbezogene Daten (beispielsweise Name, Anschrift oder E-Mail-Adressen) erhoben werden, erfolgt dies, soweit möglich, stets auf freiwilliger Basis. Diese Daten werden ohne Ihre ausdrückliche Zustimmung nicht an Dritte weitergegeben. Wir weisen darauf hin, dass die Datenübertragung im Internet (z.B. bei der Kommunikation per E-Mail) Sicherheitslücken aufweisen kann. Ein lückenloser Schutz der Daten vor dem Zugriff durch Dritte ist nicht möglich.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-[#1a1a1a] mb-4">Rechtliche Hinweise</h2>
            <p className="text-sm text-[#555]">
              Diese Website und deren Inhalte unterliegen der Verwaltungsvorschrift für Wirtschaftlichkeitsuntersuchungen (VV WU) gemäß § 7 BHO. Die Nutzung ist nur für autorisierte Benutzer gestattet.
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
