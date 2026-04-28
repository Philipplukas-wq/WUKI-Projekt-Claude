import { PrismaClient } from "../prisma/generated/client";

const globalForPrisma = global as unknown as { prisma?: PrismaClient };

export const prisma =
  globalForPrisma.prisma ||
  new PrismaClient({
    log: process.env.NODE_ENV === "development" ? ["error", "warn"] : [],
  } as any);

if (process.env.NODE_ENV !== "production") globalForPrisma.prisma = prisma;
