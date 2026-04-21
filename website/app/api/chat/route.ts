import { getToken } from "next-auth/jwt";
import { anthropic, WU_SYSTEM_PROMPT } from "@/lib/claude";
import type { NextRequest } from "next/server";

export async function POST(req: NextRequest) {
  // Session prüfen
  const token = await getToken({
    req,
    secret: process.env.NEXTAUTH_SECRET,
  });

  if (!token) {
    return Response.json({ error: "Unauthorized" }, { status: 401 });
  }

  const body = await req.json();
  const { messages } = body;

  if (!Array.isArray(messages) || messages.length === 0) {
    return Response.json({ error: "Bad Request" }, { status: 400 });
  }

  const message = await anthropic.messages.create({
    model: "claude-sonnet-4-6",
    max_tokens: 4096,
    system: WU_SYSTEM_PROMPT,
    messages,
  });

  const text =
    message.content[0]?.type === "text" ? message.content[0].text : "";

  return Response.json({ text });
}
