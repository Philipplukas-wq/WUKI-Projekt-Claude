"use client";

import { useState, useEffect, useRef } from "react";

const GREETING_TEXT = "Wirtschaftlichkeit beginnt mit der richtigen Analyse.";

export default function WukiHero() {
  const [displayedText, setDisplayedText] = useState("");
  const typingRef = useRef<ReturnType<typeof setInterval> | null>(null);

  useEffect(() => {
    let idx = 0;
    const t = setTimeout(() => {
      typingRef.current = setInterval(() => {
        idx++;
        setDisplayedText(GREETING_TEXT.slice(0, idx));
        if (idx >= GREETING_TEXT.length && typingRef.current) {
          clearInterval(typingRef.current);
        }
      }, 45);
    }, 600);
    return () => {
      clearTimeout(t);
      if (typingRef.current) clearInterval(typingRef.current);
    };
  }, []);

  return (
    <section
      className="relative overflow-hidden"
      style={{
        background:
          "linear-gradient(135deg, #1F3A45 0%, #2B5A6F 55%, #3B7A8F 100%)",
        minHeight: "500px",
      }}
    >
      <style>{`
        @keyframes drawAccent {
          from { stroke-dashoffset: 1200; }
          to   { stroke-dashoffset: 0; }
        }
        .accent-line {
          stroke-dasharray: 1200;
          animation: drawAccent 2s ease-out 0.2s forwards;
        }
        @keyframes figureIn {
          from { opacity: 0; transform: translateY(28px); }
          to   { opacity: 1; transform: translateY(0); }
        }
        .wuki-figure {
          animation: figureIn 1s cubic-bezier(.22,1,.36,1) 0.3s both;
        }
        @keyframes textIn {
          from { opacity: 0; transform: translateX(-14px); }
          to   { opacity: 1; transform: translateX(0); }
        }
        .wuki-text {
          animation: textIn 0.8s cubic-bezier(.22,1,.36,1) 0.5s both;
        }
      `}</style>

      {/* Hintergrund-Dekorlinien */}
      <svg
        className="absolute inset-0 w-full h-full pointer-events-none"
        viewBox="0 0 1200 500"
        preserveAspectRatio="xMidYMid slice"
        aria-hidden="true"
      >
        <line x1="0" y1="5" x2="1200" y2="5"
          stroke="#5BA654" strokeWidth="3" className="accent-line" />
        {[80,160,240,320,400,480].map(y => (
          <line key={y} x1="0" y1={y} x2="1200" y2={y}
            stroke="rgba(255,255,255,0.035)" strokeWidth="1" />
        ))}
        {[240,480,720,960].map(x => (
          <line key={x} x1={x} y1="0" x2={x} y2="500"
            stroke="rgba(255,255,255,0.025)" strokeWidth="1" />
        ))}
        <circle cx="1060" cy="80" r="140" fill="none"
          stroke="rgba(91,166,84,0.06)" strokeWidth="1.5" />
        <circle cx="1060" cy="80" r="90" fill="none"
          stroke="rgba(91,166,84,0.04)" strokeWidth="1" />
      </svg>

      {/* Inhalt */}
      <div className="relative z-10 max-w-7xl mx-auto px-6 sm:px-10
                      flex flex-col md:flex-row items-end gap-0 md:gap-8">

        {/* ── Figur ── */}
        <div className="wuki-figure order-1 md:order-2
                        flex-shrink-0 self-end
                        w-[12.1rem] sm:w-[14.3rem] md:w-[16.5rem] lg:w-[17.6rem]
                        -mb-1">
          {/*
            wuki-transparent.png hat echten Alpha-Kanal:
            Hintergrund vollständig entfernt, nur Linienzeichnung.
            Kein mix-blend-mode, kein filter nötig.
            drop-shadow gibt der freigestellten Figur Tiefe.
          */}
          <img
            src="/berater.png"
            alt="Ihr WU-Berater"
            className="w-full block"
            style={{
              filter: "drop-shadow(0 8px 32px rgba(91,166,84,0.25))",
              userSelect: "none",
              pointerEvents: "none",
            }}
            draggable={false}
          />
        </div>

        {/* ── Text ── */}
        <div className="wuki-text order-2 md:order-1
                        flex-1 text-white pb-10 pt-12 md:pt-16">

          <div className="inline-flex items-center gap-2
                          bg-[#5BA654]/30 border border-[#5BA654]/40
                          text-[#B8E0F0] text-xs font-medium
                          px-3 py-1 rounded-full mb-5 uppercase tracking-wider">
            <span className="w-1.5 h-1.5 rounded-full bg-[#5BA654] inline-block" />
            WU-Berater · Wirtschaftlichkeitsuntersuchungen
          </div>

          <h1 className="text-3xl sm:text-4xl font-semibold leading-tight mb-4 min-h-[2.8rem]">
            <span className={displayedText ? "typing-cursor" : ""}>
              {displayedText || <span className="opacity-0">—</span>}
            </span>
          </h1>

          <p className="text-white/45 text-sm sm:text-base leading-relaxed max-w-lg mb-8">
            Ihr KI-gestützter Assistent für rechtssichere Wirtschaftlichkeitsuntersuchungen
            gemäß&nbsp;§&nbsp;7&nbsp;BHO. Strukturiert, geführt und
            vollständig dokumentiert – vom Bedarf bis zur Erfolgskontrolle.
          </p>

          <div className="flex gap-3 flex-wrap">
            <a href="/wu-chat"
              className="bg-[#5BA654] hover:bg-[#4A8F47]
                         text-white text-sm font-medium
                         px-5 py-2.5 rounded-md transition-colors">
              WU erstellen
            </a>
            <a href="/wissenshub"
              className="border border-white/25 hover:border-white/55
                         text-white/75 hover:text-white
                         text-sm font-medium px-5 py-2.5 rounded-md transition-colors">
              Wissenshub
            </a>
          </div>
        </div>

      </div>
    </section>
  );
}
