import json
from fastavro import reader

with open("data/users.avro", "rb") as f:
    avro_reader = reader(f)
    print("Schemat z naglowka pliku:")
    print(json.dumps(avro_reader.writer_schema, indent=2, ensure_ascii=False))
    print("Kodek:", avro_reader.codec)
    print("Rekordy:")
    for record in avro_reader:
        print(" ", record)
