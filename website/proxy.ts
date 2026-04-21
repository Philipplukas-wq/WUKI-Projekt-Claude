import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

// Geschützte Routen — nur für eingeloggte Nutzer
const PROTECTED = ["/dashboard", "/wissenshub", "/wu-chat"];

export function proxy(request: NextRequest) {
  const { pathname } = request.nextUrl;
  const isProtected = PROTECTED.some((p) => pathname.startsWith(p));

  if (!isProtected) return NextResponse.next();

  // next-auth setzt das Session-Cookie mit diesem Namen
  const sessionCookie =
    request.cookies.get("__Secure-next-auth.session-token") ||
    request.cookies.get("next-auth.session-token");

  if (!sessionCookie) {
    const loginUrl = new URL("/login", request.url);
    loginUrl.searchParams.set("callbackUrl", pathname);
    return NextResponse.redirect(loginUrl);
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/dashboard/:path*", "/wissenshub/:path*", "/wu-chat/:path*"],
};
