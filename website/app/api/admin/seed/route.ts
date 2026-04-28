import { prisma } from "@/lib/prisma";
import * as bcrypt from "bcryptjs";
import { NextResponse } from "next/server";

export async function POST() {
  try {
   const adminEmail = process.env.ADMIN_EMAIL || "philipp.lukas@outlook.de";
   const adminPassword = process.env.ADMIN_PASSWORD || "admin123";

      const salt = await bcrypt.genSalt(10);
     const passwordHash = await bcrypt.hash(adminPassword, salt);
      const admin = await prisma.user.upsert({
       where: { email: adminEmail },
       update: { passwordHash },
       create: {
         email: adminEmail,
         passwordHash,
         name: "Admin",
         plan: "PRO",
         isAdmin: true,
       },
     });
      return NextResponse.json({
       success: true,
       message: `Admin user created/updated: ${admin.email}`,
       user: { email: admin.email, id: admin.id },
     });
   } catch (error) {
     console.error("Seed error:", error);
     return NextResponse.json(
       { error: "Seed failed", details: String(error) },
       { status: 500 }
     );
   }
 }