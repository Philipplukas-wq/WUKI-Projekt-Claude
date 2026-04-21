import type { Metadata } from "next";
import ChatWindow from "@/components/ChatWindow";

export const metadata: Metadata = {
  title: "WU erstellen – WU-Berater",
  description:
    "Erstellen Sie Ihre Wirtschaftlichkeitsuntersuchung im geführten Dialog. Wuki begleitet Sie von der Bedarfsforderung bis zur exportfertigen Dokumentation.",
};

export default function WuChatPage() {
  return (
    <div className="max-w-7xl mx-auto px-6 py-8 flex flex-col" style={{ height: "calc(100vh - 130px)" }}>
      {/* Seiten-Header */}
      <div className="mb-4 flex-shrink-0">
        <div className="flex items-center gap-3 mb-1">
          <div className="w-8 h-8 rounded-lg bg-[#5BA654] flex items-center justify-center text-white text-sm">
            💬
          </div>
          <h1 className="text-[#1F3A45] font-semibold text-xl">WU-Berater</h1>
        </div>
        <p className="text-[#4A90A4] text-xs">
          KI-gestützte Erstellung von Wirtschaftlichkeitsuntersuchungen gemäß § 7 BHO und AR A-2400/62 · Powered by Claude
        </p>
      </div>

      {/* Chat-Fenster füllt verbleibenden Platz */}
      <div className="flex-1 min-h-0">
        <ChatWindow />
      </div>
    </div>
  );
}
