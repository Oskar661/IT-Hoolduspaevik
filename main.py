import os
from models.log_book import LogBook
from cli import run_cli

def main():
    logbook = LogBook()
    filename = "logbook.json"

    # Kui fail olemas
    if os.path.exists(filename):

        logbook.load_from_file()

        if logbook.entries:
            print("Leiti olemasolev logbook.json fail koos kirjetega.")
            choice = input("Kas soovid neid kasutada? (Y/N): ").strip().upper()

            if choice == "Y":
                print("Laen olemasolevad kirjed...")
            else:
                logbook.entries = []
                print("Alustan tühja logiraamatuga.")
        else:
            print("logbook.json fail on olemas, kuid see on tühi.")
    else:
        print("logbook.json faili ei leitud. Luuakse uus fail.")

    input("Vajuta ENTER, et jätkata...")
    run_cli(logbook)

if __name__ == "__main__":
    main()