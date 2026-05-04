import { NextRequest, NextResponse } from "next/server";

export async function GET(request: NextRequest) {
  const keycloakIssuer = process.env.KEYCLOAK_ISSUER;

  if (!keycloakIssuer) {
    return NextResponse.json(
      { error: "Keycloak not configured" },
      { status: 500 }
    );
  }

  // Redirect to Keycloak's account registration page directly
  // Keycloak should have registration enabled in Login settings
  const registrationUrl = `${keycloakIssuer}/login-actions/registration`;

  return NextResponse.redirect(registrationUrl, { status: 307 });
}
