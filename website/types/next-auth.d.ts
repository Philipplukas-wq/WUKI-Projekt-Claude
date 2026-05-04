import type { DefaultSession } from "next-auth";
import type { JWT } from "next-auth/jwt";

declare module "next-auth" {
  interface Session {
    user: {
      id: string;
      keycloakId: string;
      name: string;
      email: string;
      status: "PENDING" | "ACTIVE" | "SUSPENDED";
      isAdmin: boolean;
      orgMemberships: Array<{
        orgId: string;
        orgName: string;
        role: string;
      }>;
      deptMemberships: Array<{
        deptId: string;
        deptName: string;
        role: string;
      }>;
    } & DefaultSession["user"];
  }

  interface User {
    id: string;
    keycloakId: string;
    name?: string;
    email: string;
    status: "PENDING" | "ACTIVE" | "SUSPENDED";
    isAdmin: boolean;
  }
}

declare module "next-auth/jwt" {
  interface JWT {
    id: string;
    keycloakId: string;
    name: string;
    email: string;
    status: "PENDING" | "ACTIVE" | "SUSPENDED";
    isAdmin: boolean;
    orgMemberships: Array<{
      orgId: string;
      orgName: string;
      role: string;
    }>;
    deptMemberships: Array<{
      deptId: string;
      deptName: string;
      role: string;
    }>;
  }
}
