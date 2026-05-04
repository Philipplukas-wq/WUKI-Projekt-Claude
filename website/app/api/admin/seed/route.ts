import { prisma } from "@/lib/prisma";
import { NextResponse } from "next/server";
import { getToken } from "next-auth/jwt";
import type { NextRequest } from "next/server";

export const dynamic = "force-dynamic";

export async function POST(req: NextRequest) {
  const token = await getToken({
    req,
    secret: process.env.NEXTAUTH_SECRET,
  });

  if (!token || !token.isAdmin) {
    return NextResponse.json(
      { error: "Unauthorized" },
      { status: 401 }
    );
  }

  try {
    const org = await prisma.organization.upsert({
      where: { slug: "test-org" },
      update: {},
      create: {
        name: "Test Organization",
        slug: "test-org",
      },
    });

    return NextResponse.json({
      success: true,
      message: "Seed data created",
      organization: { id: org.id, name: org.name },
    });
  } catch (error) {
    console.error("Seed error:", error);
    return NextResponse.json(
      { error: "Seed failed" },
      { status: 500 }
    );
  }
}