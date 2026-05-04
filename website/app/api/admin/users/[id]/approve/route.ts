import { getServerSession } from "next-auth";
import { NextRequest, NextResponse } from "next/server";
import { authOptions } from "@/lib/auth";
import { prisma } from "@/lib/prisma";

export async function POST(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  const session = await getServerSession(authOptions);

  // Check if user is authenticated and is admin
  if (!session?.user?.isAdmin) {
    return NextResponse.json(
      { error: "Unauthorized" },
      { status: 403 }
    );
  }

  try {
    const { id } = await params;
    const userId = id;

    const updatedUser = await prisma.user.update({
      where: { id: userId },
      data: { status: "ACTIVE" },
    });

    return NextResponse.json({
      message: "User approved",
      user: {
        id: updatedUser.id,
        email: updatedUser.email,
        status: updatedUser.status,
      },
    });
  } catch (error) {
    console.error("Error approving user:", error);
    return NextResponse.json(
      { error: "Internal server error" },
      { status: 500 }
    );
  }
}
