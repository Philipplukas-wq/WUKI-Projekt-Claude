export default function AwaitingApprovalPage() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-900 to-slate-800">
      <div className="bg-white rounded-lg shadow-2xl p-8 w-full max-w-md text-center">
        <div className="mb-6">
          <div className="w-16 h-16 bg-yellow-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <svg
              className="w-8 h-8 text-yellow-600"
              fill="currentColor"
              viewBox="0 0 20 20"
            >
              <path
                fillRule="evenodd"
                d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z"
                clipRule="evenodd"
              />
            </svg>
          </div>
        </div>

        <h1 className="text-2xl font-bold text-slate-900 mb-4">
          Konto ausstehend
        </h1>

        <p className="text-slate-600 mb-6">
          Vielen Dank für Ihre Registrierung! Ihr Konto wurde erfolgreich
          angelegt.
        </p>

        <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-6">
          <p className="text-blue-900 font-semibold text-sm">
            Ein Administrator überprüft Ihre Anmeldung und gibt Ihren Zugang
            bald frei.
          </p>
        </div>

        <p className="text-slate-500 text-sm">
          Überprüfen Sie regelmäßig Ihre E-Mail auf eine Benachrichtigung zur
          Freigabe.
        </p>

        <p className="text-slate-500 text-sm mt-4">
          Haben Sie Fragen? Kontaktieren Sie bitte{" "}
          <a
            href="mailto:support@example.de"
            className="text-blue-600 hover:underline"
          >
            den Support
          </a>
          .
        </p>
      </div>
    </div>
  );
}
