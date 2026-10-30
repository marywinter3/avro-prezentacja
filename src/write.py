import json
from fastavro import writer, parse_schema

with open("schemas/user_v1.avsc", encoding="utf-8") as f:
    schema = parse_schema(json.load(f))

with open("data/users.json", encoding="utf-8") as f:
    records = json.load(f)

with open("data/users.avro", "wb") as out:
    writer(out, schema, records, codec="deflate")

print(f"Zapisano {len(records)} rekordy do data/users.avro")
