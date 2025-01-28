import os
import subprocess
from datetime import datetime
import shutil

# Konfiguracja
DB_NAME = "twoja_baza_danych"  # Zmień na nazwę swojej bazy danych
DB_USER = "twoj_uzytkownik"    # Zmień na swojego użytkownika bazy danych
DB_PASSWORD = "twoje_haslo"    # Zmień na swoje hasło do bazy danych
BACKUP_DIR = "/ścieżka/do/folderu/backupów"  # Zmień na docelowy folder backupów
MAX_BACKUP_AGE_DAYS = 30  # Usuń backupy starsze niż 30 dni

def create_backup():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"{DB_NAME}_backup_{timestamp}.sql")

    command = f"pg_dump -U {DB_USER} -d {DB_NAME} -f {backup_file}"

    try:
        # Ustawienie zmiennej środowiskowej z hasłem
        env = os.environ.copy()
        env["PGPASSWORD"] = DB_PASSWORD

        # Wykonaj backup
        subprocess.run(command, shell=True, check=True, env=env)
        print(f"Backup utworzony pomyślnie: {backup_file}")

        # Weryfikacja backupu (sprawdź, czy plik nie jest pusty)
        if os.path.getsize(backup_file) > 0:
            print("Backup został zweryfikowany.")
        else:
            print("Błąd: Plik backupu jest pusty!")
            os.remove(backup_file)  # Usuń nieprawidłowy backup
    except subprocess.CalledProcessError as e:
        print(f"Błąd podczas tworzenia backupu: {e}")

# Funkcja do usuwania starych backupów
def delete_old_backups():
    current_time = datetime.now()
    for filename in os.listdir(BACKUP_DIR):
        file_path = os.path.join(BACKUP_DIR, filename)
        if os.path.isfile(file_path):
            file_creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
            file_age_days = (current_time - file_creation_time).days

            if file_age_days > MAX_BACKUP_AGE_DAYS:
                print(f"Usuwanie starego backupu: {filename}")
                os.remove(file_path)

# Główna funkcja
def main():
    # Sprawdź, czy folder backupów istnieje
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
        print(f"Utworzono folder backupów: {BACKUP_DIR}")

    # Utwórz backup
    create_backup()

    # Usuń stare backupy
    delete_old_backups()

if __name__ == "__main__":
    main()
