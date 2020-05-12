Użyte narzędzia: python3, sqlite3, tkinter, mqtt
Testowane na Linuxie x86_64 z pythonem 3.8.2

Szkic przypadków użycia i relacji w bazie danych znajduje się w pliku `RaspberryLab.pdf`.
Przykłady (raport i screeny) znajdują się w folderze `examples`.

Przed testowaniem aplikacji należy przejść do katalogu `src` i przygotować środowisko.

```
cd src
./setupenv.sh
source venv/bin/activate
```

Wymagana jest także poprawna konfiguracja mosquitto, dodając uwierzytelnienie i autoryzację.

Zawartość aclfile.conf:

```
user server
topic read app/card_reading

user client
topic app/card_reading
```

Można teraz uruchomić testy (`./test.sh`), które wyświetlą zawartość bazy danych.
Można także uruchomić serwer (`./server.py`) lub klienta (`./client.py`).

Wygenerowany raport w formacie csv znajdzie się w pliku `time_report.csv`.
Generowany jest on z założeniem że każdy pracownik musi użyć raz karty przy każdym wejściu i wyjściu z pracy.
Zawiera on 5 kolumn, kolejno: ID pracownika (lub None jeśli została użyta nieprzypisana karta), nazwa terminalu użytego po przybyciu do pracy, data przybycia do pracy, nazwa terminalu użytego przy wyjściu z pracy, data wyjścia z pracy.
