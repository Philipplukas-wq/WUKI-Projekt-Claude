import type { Metadata } from "next";
import "./globals.css";
import SessionProvider from "@/components/SessionProvider";

export const metadata: Metadata = {
  title: "WU-Berater – Wirtschaftlichkeitsuntersuchungen nach § 7 BHO",
  description:
    "Der WU-Berater führt Sie strukturiert durch die Erstellung rechtssicherer Wirtschaftlichkeitsuntersuchungen gemäß § 7 BHO und AR A-2400/62. Für Bundeswehr und öffentliche Verwaltung.",
  keywords: [
    "Wirtschaftlichkeitsuntersuchung",
    "§ 7 BHO",
    "AR A-2400/62",
    "WU Bundeswehr",
    "Wirtschaftlichkeitsbetrachtung",
    "öffentliche Verwaltung",
    "Kapitalwertmethode",
    "Bedarfsforderung",
  ],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="de" className="h-full">
      <body className="min-h-full flex flex-col bg-[#f5f5f5] text-[#1a1a1a]">
        <SessionProvider>{children}</SessionProvider>
      </body>
    </html>
  );
}
