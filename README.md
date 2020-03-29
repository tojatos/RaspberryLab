Użyte narzędzia: python3, sqlite3

Szkic przypadków użycia i relacji w bazie danych znajduje się w pliku `RaspberryLab.pdf`.

Przed testowaniem aplikacji należy przejść do katalogu `src` i przygotować środowisko.

```
cd src
./setupenv.sh
source venv/bin/activate
```

Można teraz uruchomić testy (`./test.sh`), które wyświetlą zawartość bazy danych.
Można też ręcznie przetestować funkcje serwera:
```
python3
from app import server
(...)
```
