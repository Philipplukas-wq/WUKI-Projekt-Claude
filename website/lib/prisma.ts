import { PrismaClient } from "@prisma/client";
import { PrismaBetterSqlite3 } from "@prisma/adapter-better-sqlite3";
import Database from "better-sqlite3";

const globalForPrisma = global as unknown as { prisma?: PrismaClient };

function getPrismaClient() {
  if (!globalForPrisma.prisma) {
    try {
      let dbPath = "dev.db";
      const dbUrl = process.env.DATABASE_URL;
      if (dbUrl && typeof dbUrl === "string") {
        dbPath = dbUrl.startsWith("file:")
          ? dbUrl.slice(5)
          : dbUrl;
      }
      const db = new Database(dbPath);
      const adapter = new PrismaBetterSqlite3(db);
      globalForPrisma.prisma = new PrismaClient({
        adapter,
        log: process.env.NODE_ENV !== "production" ? ["query", "warn", "error"] : ["warn", "error"],
      });
    } catch (e) {
      console.error("Failed to initialize PrismaClient:", e);
      throw e;
    }
  }
  return globalForPrisma.prisma;
}

export const prisma = getPrismaClient();

if (process.env.NODE_ENV !== "production") {
  globalForPrisma.prisma = prisma;
}
