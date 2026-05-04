import type { NextAuthOptions } from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";
import Database from "better-sqlite3";
import { randomUUID } from "crypto";

const getDb = () => new Database("dev.db");

export const authOptions: NextAuthOptions = {
  providers: [
    CredentialsProvider({
      name: "Test Credentials",
      credentials: {
        email: { label: "Email", type: "email" },
        password: { label: "Password", type: "password" },
      },
      async authorize(credentials) {
        if (!credentials?.email || !credentials?.password) return null;

        const ADMIN_USERS = process.env.ADMIN_USERS || "philipp.lukas@outlook.de:Wirtschaftlichkeitsuntersuchung.2026/Wuki";
        const adminPairs = ADMIN_USERS.split(",").map((pair) => {
          const [email, pwd] = pair.split(":");
          return { email: email.trim(), password: pwd.trim() };
        });

        const adminMatch = adminPairs.find(
          (pair) =>
            pair.email === credentials.email &&
            pair.password === credentials.password
        );

        if (!adminMatch) return null;

        try {
          const db = getDb();

          // Check if user exists
          const stmt = db.prepare("SELECT id FROM User WHERE email = ?");
          let user = stmt.get(credentials.email) as { id: string } | undefined;

          // Create user if doesn't exist
          if (!user) {
            const userId = randomUUID();
            const insertStmt = db.prepare(
              "INSERT INTO User (id, keycloakId, email, name, status, isAdmin, createdAt, updatedAt) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            );
            insertStmt.run(
              userId,
              `test-${credentials.email}`,
              credentials.email,
              credentials.email.split("@")[0],
              "ACTIVE",
              1,
              new Date().toISOString(),
              new Date().toISOString()
            );
            user = { id: userId };
          }

          db.close();

          return {
            id: user.id,
            email: credentials.email,
            name: credentials.email.split("@")[0],
            keycloakId: `test-${credentials.email}`,
            status: "ACTIVE" as const,
            isAdmin: true,
          };
        } catch (error) {
          console.error("Auth DB Error:", error);
          return null;
        }
      },
    }),
  ],
  session: {
    strategy: "jwt",
    maxAge: 8 * 60 * 60,
  },
  pages: {
    signIn: "/login",
    error: "/login",
  },
  callbacks: {
    async jwt({ token, user }) {
      if (user) {
        token.id = user.id;
        token.email = user.email;
        token.name = user.name || user.email.split("@")[0];
        token.status = "ACTIVE";
        token.isAdmin = true;
      }
      return token;
    },
    async session({ session, token }) {
      if (token && session.user) {
        session.user = {
          ...session.user,
          id: token.id as string,
          email: token.email as string,
          status: "ACTIVE",
          isAdmin: true,
          orgMemberships: [],
          deptMemberships: [],
        };
      }
      return session;
    },
  },
};
