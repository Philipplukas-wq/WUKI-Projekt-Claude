import type { NextAuthOptions } from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";
import { prisma } from "./prisma";
import * as bcrypt from "bcryptjs";

export const authOptions: NextAuthOptions = {
  providers: [
    CredentialsProvider({
      name: "Zugangsdaten",
      credentials: {
        email: { label: "E-Mail", type: "email", placeholder: "name@example.de" },
        password: { label: "Passwort", type: "password" },
      },
      async authorize(credentials) {
        if (!credentials?.email || !credentials?.password) return null;

        const user = await prisma.user.findUnique({
          where: { email: credentials.email },
        });

        if (!user) return null;

        const isPasswordValid = await bcrypt.compare(
          credentials.password,
          user.passwordHash
        );

        if (!isPasswordValid) return null;

        return {
          id: user.id,
          email: user.email,
          name: user.name,
          plan: user.plan,
          isAdmin: user.isAdmin,
          wuSessionsThisMonth: user.wuSessionsThisMonth,
          departmentId: user.departmentId,
        };
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
        token.plan = user.plan;
        token.isAdmin = user.isAdmin;
        token.wuSessionsThisMonth = user.wuSessionsThisMonth;
        token.departmentId = user.departmentId;
      }
      return token;
    },
    async session({ session, token }) {
      if (token) {
        session.user = {
          ...session.user,
          email: token.email as string,
          id: token.id as string,
          plan: token.plan as string,
          isAdmin: token.isAdmin as boolean,
          wuSessionsThisMonth: token.wuSessionsThisMonth as number,
          departmentId: token.departmentId as string | null,
        };
      }
      return session;
    },
  },
};
