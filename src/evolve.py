import json
from fastavro import reader, parse_schema

with open("schemas/user_v2.avsc", encoding="utf-8") as f:
    schema_v2 = parse_schema(json.load(f))

with open("data/users.avro", "rb") as f:
    for record in reader(f, reader_schema=schema_v2):
        print(record)  # nowe pole country dostaje wartosc domyslna "PL"
