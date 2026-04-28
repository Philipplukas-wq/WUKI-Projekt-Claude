#!/bin/bash
set -e

echo "=========================================="
echo "Setup-Script für wirtschaftlichkeitsassistent.de"
echo "=========================================="

# Systemaktualisierung
echo "Step 1: System aktualisieren..."
apt-get update
apt-get upgrade -y

# Node.js installieren
echo "Step 2: Node.js und npm installieren..."
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
apt-get install -y nodejs

# PostgreSQL installieren
echo "Step 3: PostgreSQL installieren..."
apt-get install -y postgresql postgresql-contrib

# Nginx installieren
echo "Step 4: Nginx installieren..."
apt-get install -y nginx

# Certbot für SSL-Zertifikate
echo "Step 5: Certbot installieren..."
apt-get install -y certbot python3-certbot-nginx

# PM2 global installieren (für Process-Management)
echo "Step 6: PM2 installieren..."
npm install -g pm2

# Git-Repository klonen
echo "Step 7: Website-Code klonen..."
cd /opt
git clone https://github.com/Philipplukas-wq/WUKI-Projekt-Claude.git wuki-projekt
cd wuki-projekt/website

# Dependencies installieren
echo "Step 8: npm Dependencies installieren..."
npm install

# PostgreSQL Benutzer und Datenbank erstellen
echo "Step 9: PostgreSQL Datenbank einrichten..."
sudo -u postgres psql << EOF
CREATE USER wu_user WITH PASSWORD 'wu_secure_password_change_this';
CREATE DATABASE wu_production OWNER wu_user;
ALTER ROLE wu_user SET client_encoding TO 'utf8';
ALTER ROLE wu_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE wu_user SET default_transaction_deferrable TO on;
ALTER ROLE wu_user SET default_transaction_read_only TO off;
GRANT ALL PRIVILEGES ON DATABASE wu_production TO wu_user;
EOF

# .env-Datei erstellen
echo "Step 10: .env-Datei konfigurieren..."
cat > /opt/wuki-projekt/website/.env << EOF
DATABASE_URL="postgresql://wu_user:wu_secure_password_change_this@localhost:5432/wu_production"
NEXTAUTH_URL="https://wirtschaftlichkeitsassistent.de"
NEXTAUTH_SECRET="$(openssl rand -base64 32)"
NODE_ENV="production"
EOF

# Prisma Migration
echo "Step 11: Prisma Migration ausführen..."
cd /opt/wuki-projekt/website
npx prisma migrate deploy

# Next.js Build
echo "Step 12: Next.js bauen..."
npm run build

# PM2 App starten
echo "Step 13: Anwendung mit PM2 starten..."
pm2 start "npm run start" --name "wu-website" --instances 1
pm2 startup
pm2 save

# Nginx konfigurieren
echo "Step 14: Nginx konfigurieren..."
cat > /etc/nginx/sites-available/wirtschaftlichkeitsassistent.de << 'EOF'
upstream wu_app {
    server 127.0.0.1:3000;
}

server {
    listen 80;
    server_name wirtschaftlichkeitsassistent.de www.wirtschaftlichkeitsassistent.de;

    location / {
        proxy_pass http://wu_app;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
EOF

# Nginx aktivieren
ln -sf /etc/nginx/sites-available/wirtschaftlichkeitsassistent.de /etc/nginx/sites-enabled/
rm -f /etc/nginx/sites-enabled/default
nginx -t
systemctl restart nginx

# SSL-Zertifikat mit Let's Encrypt
echo "Step 15: SSL-Zertifikat einrichten..."
certbot --nginx -d wirtschaftlichkeitsassistent.de --non-interactive --agree-tos --email Philipp.lukas@outlook.de --redirect

# Firewall konfigurieren (UFW)
echo "Step 16: Firewall konfigurieren..."
apt-get install -y ufw
ufw default deny incoming
ufw default allow outgoing
ufw allow 22/tcp
ufw allow 80/tcp
ufw allow 443/tcp
ufw --force enable

echo "=========================================="
echo "✅ Setup abgeschlossen!"
echo "=========================================="
echo ""
echo "Website läuft unter: https://wirtschaftlichkeitsassistent.de"
echo ""
echo "⚠️  WICHTIG - Passwort ändern:"
echo "sudo -u postgres psql -c \"ALTER USER wu_user WITH PASSWORD 'neues_sicheres_passwort';\""
echo ""
echo "Logs ansehen:"
echo "pm2 logs wu-website"
echo ""
echo "Status prüfen:"
echo "pm2 status"
