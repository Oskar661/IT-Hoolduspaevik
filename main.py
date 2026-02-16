from models.log_book import LogBook
from cli import run_cli
from import_csv import import_csv_file

def main():
    logbook = LogBook()
    logbook.load_from_file()

    while True:
        print("\n=== IT HOOLDUSPÄEVIK ===")
        print("1. Kasuta olemasolevat logbook.json")
        print("2. Impordi CSV fail")
        print("0. Välju")
        choice = input("Vali tegevus: ").strip()

        if choice == "1":
            run_cli(logbook)
            break
        elif choice == "2":
            filepath = input("Sisesta CSV faili nimi (näiteks sample_import.csv): ").strip()
            import_csv_file(filepath, logbook)
            input("Vajuta ENTER, et jätkata CLI-ga...")
            run_cli(logbook)
            break
        elif choice == "0":
            print("Programm suletud.")
            break
        else:
            print("Vale valik! Proovi uuesti.")

if __name__ == "__main__":
    main()
