import csv
import os
from datetime import datetime
from models.log_entry import LogEntry

def import_csv_file(filepath, logbook):
    # Tee errors kaust, kui seda ei ole
    if not os.path.exists("errors"):
        os.makedirs("errors")

    errors_file = os.path.join("errors", "import_errors.log")
    errors = []

    # Kontrolli, kas fail olemas
    if not os.path.isfile(filepath):
        print(f"CSV faili ei leitud: {filepath}")
        input("Vajuta ENTER, et jätkata...")
        return

    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            full_line = ';'.join(row)
            # Kontrollime, et oleks täpselt 4 välja
            if len(row) != 4:
                errors.append(f"{full_line} -> Vale arv välju")
                continue

            date_str, title, description, status = row
            # Trim tühikud
            date_str = date_str.strip()
            title = title.strip()
            description = description.strip()
            status = status.strip().upper()

            try:
                # Kuupäeva valideerimine
                datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
                # Pealkiri ja kirjeldus
                if len(title) < 4:
                    raise ValueError("Pealkiri liiga lühike või puudub")
                if len(description) < 10:
                    raise ValueError("Kirjeldus liiga lühike või puudub")
                if status not in ["OPEN", "DONE"]:
                    raise ValueError("Staatus peab olema OPEN või DONE")

                # Kui kõik korras, lisa LogBooki
                entry = LogEntry(title, description, status=status, created_at=date_str)
                logbook.add_entry(entry)

            except ValueError as ve:
                errors.append(f"{full_line} -> {ve}")

    # Kirjuta vigade fail AINA
    with open(errors_file, "w", encoding="utf-8") as f:
        if errors:
            for err in errors:
                f.write(err + "\n")
            print(f"Leiti vigu! Vaata vigade faili: {errors_file}")
        else:
            f.write("")  # Tühi fail, kui vigu pole
            print("Kõik read korrektsed ja imporditud! Vigade fail tühi.")

    input("Vajuta ENTER, et jätkata...")
