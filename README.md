# Apache Avro - otwarte formaty danych

Specyfikacja: https://avro.apache.org/docs/1.11.1/specification/

## Zawartosc

| Plik | Co pokazuje |
| `schemas/user_v1.avsc` | schemat danych (record, union z null) |
| `schemas/user_v2.avsc` | nowa wersja schematu z polem `country` |
| `schemas/hello.avpr` | protokol RPC w JSON |
| `schemas/user.avdl` | ten sam schemat w Avro IDL |
| `data/users.json` | dane wejsciowe |
| `data/users.avro` | dane wyjsciowe (tworzy je `write.py`) |
| `src/write.py` | zapis JSON do Avro |
| `src/read.py` | odczyt Avro, schemat z naglowka pliku |
| `src/evolve.py` | odczyt starego pliku nowym schematem |
| `src/bytes_example.py` | rekord ze specyfikacji w 5 bajtach |
| `src/hexdump.py` | podglad bajtow pliku |

## Uruchomienie

Wymagany Python 3.9 lub nowszy. Polecenia uruchamiaj z glownego folderu repozytorium.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python src/write.py
python src/read.py
python src/evolve.py
python src/bytes_example.py
python src/hexdump.py data/users.avro
```