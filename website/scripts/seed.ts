import { prisma } from "../lib/prisma";
import * as bcrypt from "bcryptjs";

async function main() {
  const adminEmail = process.env.ADMIN_EMAIL || "philipp.lukas@outlook.de";
  const adminPassword = process.env.ADMIN_PASSWORD || "admin123";

  console.log(`Seeding database with admin user: ${adminEmail}`);

  const salt = await bcrypt.genSalt(10);
  const passwordHash = await bcrypt.hash(adminPassword, salt);

  const admin = await prisma.user.upsert({
    where: { email: adminEmail },
    update: {},
    create: {
      email: adminEmail,
      passwordHash,
      name: "Admin",
      plan: "PRO",
      isAdmin: true,
    },
  });

  console.log(`✓ Admin user created/updated: ${admin.email}`);
}

main()
  .then(async () => {
    await prisma.$disconnect();
  })
  .catch(async (e) => {
    console.error(e);
    await prisma.$disconnect();
    process.exit(1);
  });
