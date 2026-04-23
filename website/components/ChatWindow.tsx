"use client";

import { useState, useRef, useEffect } from "react";
import Image from "next/image";

type Role = "user" | "assistant";

interface Message {
  role: Role;
  content: string;
}

export default function ChatWindow() {
  const [messages, setMessages] = useState<Message[]>([
    {
      role: "assistant",
      content: `Willkommen bei Wuki, Ihrem digitalen Assistenten für Wirtschaftlichkeitsuntersuchungen gemäß § 7 BHO und AR A-2400/62.

Ich führe Sie strukturiert durch die Erstellung einer vollständigen WU.

Wie lautet Ihr vollständiger Name?
(Sie können diesen auch später manuell im Dokument anpassen.)`,
    },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  async function sendMessage() {
    const text = input.trim();
    if (!text || loading) return;

    const newMessages: Message[] = [...messages, { role: "user", content: text }];
    setMessages(newMessages);
    setInput("");
    setLoading(true);

    // Platzhalter für Lade-Indikator
    setMessages((prev) => [...prev, { role: "assistant", content: "" }]);

    try {
      const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages: newMessages }),
      });

      if (!res.ok) throw new Error(`Fehler: ${res.status}`);

      const data = await res.json();
      const assistantText = data.text ?? "";

      setMessages((prev) => {
        const updated = [...prev];
        updated[updated.length - 1] = { role: "assistant", content: assistantText };
        return updated;
      });
    } catch {
      setMessages((prev) => {
        const updated = [...prev];
        updated[updated.length - 1] = {
          role: "assistant",
          content: "Es ist ein Fehler aufgetreten. Bitte versuchen Sie es erneut.",
        };
        return updated;
      });
    } finally {
      setLoading(false);
      textareaRef.current?.focus();
    }
  }

  function handleKeyDown(e: React.KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  }

  return (
    <div className="flex flex-col h-full bg-white rounded-lg border border-[#e0e0e0] overflow-hidden shadow-sm">
      {/* Chat-Header */}
      <div className="flex items-center gap-3 px-4 py-3 bg-white border-b border-[#e0e0e0] flex-shrink-0">
        <div className="relative w-10 h-12 flex-shrink-0 bg-white rounded-lg p-0.5">
          <Image src="/wappen.png" alt="Wuki" fill className="object-contain" />
        </div>
        <div>
          <p className="text-[#1F3A45] text-sm font-medium">Wuki — WU-Berater</p>
          <p className="text-[#4A90A4] text-xs">Wirtschaftlichkeitsuntersuchungen nach § 7 BHO</p>
        </div>
        <div className="ml-auto flex items-center gap-1.5">
          <span className="w-2 h-2 rounded-full bg-green-400 animate-pulse" />
          <span className="text-[#4A90A4] text-xs">Online</span>
        </div>
      </div>

      {/* Nachrichten */}
      <div className="flex-1 overflow-y-auto chat-messages p-4 space-y-4 bg-[#f9f9f9]">
        {messages.length === 0 && (
          <div className="flex flex-col items-center justify-center h-full text-center py-12">
            <div className="relative w-20 h-20 mb-4 opacity-60 bg-transparent">
              <Image src="/wappen.png" alt="Wuki" fill className="object-contain" />
            </div>
            <p className="text-[#4a4e69] text-sm font-medium">Bereit für Ihre WU</p>
            <p className="text-[#4a4e69]/60 text-xs mt-1 max-w-xs">
              Schreiben Sie eine Nachricht um zu starten. Wuki führt Sie strukturiert durch die Erstellung.
            </p>
          </div>
        )}

        {messages.map((msg, i) => (
          <div
            key={i}
            className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"} gap-2`}
          >
            {msg.role === "assistant" && (
              <div className="relative w-12 h-14 flex-shrink-0 bg-[#f9f9f9] rounded-lg p-1 shadow-sm">
                <Image src="/wappen.png" alt="Wuki" fill className="object-contain" />
              </div>
            )}

            <div
              className={`max-w-[75%] rounded-2xl px-4 py-2.5 text-sm leading-relaxed whitespace-pre-wrap ${
                msg.role === "user"
                  ? "bg-[#5BA654] text-white rounded-tr-sm"
                  : "bg-white border border-[#e0e0e0] text-[#1a1a1a] rounded-tl-sm shadow-sm"
              }`}
            >
              {msg.content}
              {msg.role === "assistant" && loading && i === messages.length - 1 && msg.content === "" && (
                <span className="inline-flex gap-1 items-center">
                  <span className="w-1.5 h-1.5 bg-[#4a4e69]/50 rounded-full animate-bounce" style={{ animationDelay: "0ms" }} />
                  <span className="w-1.5 h-1.5 bg-[#4a4e69]/50 rounded-full animate-bounce" style={{ animationDelay: "150ms" }} />
                  <span className="w-1.5 h-1.5 bg-[#4a4e69]/50 rounded-full animate-bounce" style={{ animationDelay: "300ms" }} />
                </span>
              )}
            </div>

            {msg.role === "user" && (
              <div className="w-7 h-7 rounded-full bg-[#4a4e69] flex items-center justify-center text-white text-xs flex-shrink-0 mt-0.5">
                👤
              </div>
            )}
          </div>
        ))}
        <div ref={bottomRef} />
      </div>

      {/* Eingabe */}
      <div className="flex-shrink-0 px-4 py-3 bg-white border-t border-[#e0e0e0]">
        <div className="flex items-end gap-2">
          <textarea
            ref={textareaRef}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            disabled={loading}
            rows={1}
            placeholder="Nachricht eingeben … (Enter zum Senden, Shift+Enter für neue Zeile)"
            className="flex-1 resize-none px-3 py-2.5 border border-[#e0e0e0] rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-[#5BA654] focus:border-transparent transition disabled:opacity-50"
            style={{ maxHeight: "120px", overflowY: "auto" }}
          />
          <button
            onClick={sendMessage}
            disabled={loading || !input.trim()}
            className="bg-[#5BA654] hover:bg-[#4A8F47] disabled:opacity-40 disabled:cursor-not-allowed text-white rounded-lg px-4 py-2.5 text-sm font-medium transition flex-shrink-0"
          >
            {loading ? "…" : "Senden"}
          </button>
        </div>
        <p className="text-[#4a4e69]/40 text-xs mt-1.5 text-center">
          Powered by Claude · Inhalte immer prüfen und anpassen
        </p>
      </div>
    </div>
  );
}
