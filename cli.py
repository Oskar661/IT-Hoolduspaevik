from models.log_entry import LogEntry

def run_cli(logbook):
    while True:
        print("\n=== CLI MENÜÜ ===")
        print("1. Lisa kirje")
        print("2. Kustuta kirje")
        print("3. Muuda staatust")
        print("4. Otsi kirjeid")
        print("5. Filtreeri staatuse järgi")
        print("6. Näita kõiki")
        print("0. Välju")

        choice = input("Vali tegevus: ").strip()

        if choice == "1":
            add_entry(logbook)
        elif choice == "2":
            delete_entry(logbook)
        elif choice == "3":
            change_status(logbook)
        elif choice == "4":
            search_entries(logbook)
        elif choice == "5":
            filter_status(logbook)
        elif choice == "6":
            show_all(logbook)
        elif choice == "0":
            logbook.save_to_file()
            print("Programm suletud.")
            break
        else:
            print("Vale valik!")

def add_entry(logbook):
    title = input("Sisesta pealkiri (min 4 tähemärki): ").strip()
    if len(title) < 4:
        print("Pealkiri peab olema vähemalt 4 tähemärki!")
        input("Vajuta ENTER...")
        return

    description = input("Sisesta kirjeldus (min 10 tähemärki): ").strip()
    if len(description) < 10:
        print("Kirjeldus peab olema vähemalt 10 tähemärki!")
        input("Vajuta ENTER...")
        return

    entry = LogEntry(title, description)
    logbook.add_entry(entry)
    logbook.save_to_file()
    print("Kirje lisatud.")
    input("Vajuta ENTER...")

def delete_entry(logbook):
    show_all(logbook)
    try:
        index = int(input("Sisesta kustutatava kirje number: ")) - 1
        logbook.delete_entry(index)
        logbook.save_to_file()
        print("Kirje kustutatud.")
    except:
        print("Vigane number!")
    input("Vajuta ENTER...")

def change_status(logbook):
    show_all(logbook)
    try:
        index = int(input("Sisesta kirje number: ")) - 1
        logbook.change_status(index)
        logbook.save_to_file()
        print("Staatus muudetud.")
    except:
        print("Vigane number!")
    input("Vajuta ENTER...")

def search_entries(logbook):
    keyword = input("Sisesta otsingusõna (≥2 tähemärki): ").strip()
    if len(keyword) < 2:
        print("Otsing peab sisaldama vähemalt 2 tähemärki!")
        input("Vajuta ENTER...")
        return

    results = logbook.search(keyword)
    if not results:
        print("Kirjeid ei leitud.")
    else:
        print("Otsingu tulemused:")
        for i, entry in enumerate(results, 1):
            desc_display = (entry.description[:25] + "...") if len(entry.description) > 25 else entry.description
            print(f"{i}. {entry.created_at} | [{entry.status}] | {entry.title} | {desc_display}")
    input("Vajuta ENTER...")

def filter_status(logbook):
    status = input("Sisesta staatus (OPEN/DONE): ").strip().upper()
    if status not in ["OPEN", "DONE"]:
        print("Vale staatus!")
        input("Vajuta ENTER...")
        return
    results = logbook.filter_by_status(status)
    if not results:
        print("Kirjeid ei leitud.")
    else:
        for i, entry in enumerate(results, 1):
            desc_display = (entry.description[:25] + "...") if len(entry.description) > 25 else entry.description
            print(f"{i}. {entry.created_at} | [{entry.status}] | {entry.title} | {desc_display}")
    input("Vajuta ENTER...")

def show_all(logbook):
    if not logbook.entries:
        print("Kirjeid pole.")
        input("Vajuta ENTER...")
        return
    for i, entry in enumerate(logbook.entries, 1):
        desc_display = (entry.description[:25] + "...") if len(entry.description) > 25 else entry.description
        print(f"{i}. {entry.created_at} | [{entry.status}] | {entry.title} | {desc_display}")
    input("Vajuta ENTER...")
