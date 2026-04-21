# Supabase-Integrationsanleitung

## Schritt 1: Supabase-Projekt erstellen
1. Gehe zu https://supabase.com
2. Melde dich an oder registriere dich
3. Erstelle ein neues Projekt
4. Kopiere die **Project URL** und den **anon key** (API keys → anon public)

## Schritt 2: Environment-Variablen hinzufügen
Füge zu `.env.local` hinzu:
```
NEXT_PUBLIC_SUPABASE_URL=<deine-supabase-url>
NEXT_PUBLIC_SUPABASE_ANON_KEY=<dein-anon-key>
```

## Schritt 3: Datenbank-Tabellen erstellen
In der Supabase-Console (SQL Editor):

### Users Tabelle
```sql
create table users (
  id uuid primary key default uuid_generate_v4(),
  email text unique not null,
  password_hash text not null,
  name text,
  plan text default 'FREE' check (plan in ('FREE', 'PRO', 'DEPARTMENT')),
  wu_sessions_this_month integer default 0,
  month_reset_date timestamp default now(),
  department_id uuid references departments(id),
  is_admin boolean default false,
  created_at timestamp default now(),
  updated_at timestamp default now()
);

create index idx_users_email on users(email);
create index idx_users_department on users(department_id);
```

### Departments Tabelle
```sql
create table departments (
  id uuid primary key default uuid_generate_v4(),
  name text not null,
  invite_code text unique not null,
  seats integer,
  active boolean default true,
  created_at timestamp default now(),
  updated_at timestamp default now()
);

create index idx_departments_invite on departments(invite_code);
```

## Schritt 4: Dateien, die aktualisiert werden müssen

### `lib/auth.ts`
- Nutzer-Authentifizierung gegen Supabase `users` Tabelle

### `app/api/register/route.ts`
- Neuer Nutzer wird in Supabase erstellt

### `app/api/chat/route.ts`
- WU-Session-Limit wird in Supabase geprüft und aktualisiert

### `app/(protected)/dashboard/page.tsx`
- WU-Count wird von Supabase abgerufen

### Admin-Panel
- `app/(protected)/admin/page.tsx` (neu)
- `app/api/admin/users/route.ts` (neu)
- `app/api/admin/departments/route.ts` (neu)

## Schritt 5: Authentifizierung und RLS (Row-Level Security)
- Optional: RLS-Policies für Datenschutz einrichten
- Für MVP reicht der anon-key ohne RLS

## Nächste Schritte
1. Tabellen in Supabase erstellen
2. `.env.local` aktualisieren
3. Auth-API gegen Supabase anpassen
4. WU-Limit-Tracking in Chat-API hinzufügen
5. Dashboard aktualisieren
6. Admin-Panel bauen
