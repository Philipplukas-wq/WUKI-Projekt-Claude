import type { DefaultSession } from "next-auth";
import type { JWT } from "next-auth/jwt";

declare module "next-auth" {
  interface Session {
    user: {
      id: string;
      email: string;
      plan: string;
      isAdmin: boolean;
      wuSessionsThisMonth: number;
      departmentId: string | null;
    } & DefaultSession["user"];
  }

  interface User {
    id: string;
    email: string;
    plan: string;
    isAdmin: boolean;
    wuSessionsThisMonth: number;
    departmentId: string | null;
  }
}

declare module "next-auth/jwt" {
  interface JWT {
    id: string;
    email: string;
    plan: string;
    isAdmin: boolean;
    wuSessionsThisMonth: number;
    departmentId: string | null;
  }
}
