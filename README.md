# Auto DB Backup

Projekt automatyzacji backupów bazy danych. Skrypt tworzy kopie zapasowe bazy danych, weryfikuje ich poprawność i zarządza harmonogramem backupów.

## Wymagania

- Python 3.x
- Narzędzie `pg_dump` (dla PostgreSQL) lub `mysqldump` (dla MySQL)
- Dostęp do bazy danych

## Instalacja

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/milekv/auto-db-backup.git
   cd auto-db-backup
