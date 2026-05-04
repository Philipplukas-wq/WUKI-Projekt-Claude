import { NextResponse } from "next/server";
import Database from "better-sqlite3";

export const dynamic = "force-dynamic";

export async function GET() {
  try {
    const db = new Database("dev.db");
    const stmt = db.prepare("SELECT id, email, status, isAdmin FROM User LIMIT 10");
    const users = stmt.all();
    db.close();

    return NextResponse.json({
      success: true,
      userCount: users.length,
      users: users,
    });
  } catch (error) {
    console.error("DB Error:", error);
    return NextResponse.json(
      { error: String(error), details: error instanceof Error ? error.message : "Unknown error" },
      { status: 500 }
    );
  }
}
