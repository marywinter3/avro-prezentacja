import io
import json
from fastavro import schemaless_writer, parse_schema

schema = parse_schema({
    "type": "record", "name": "test",
    "fields": [{"name": "a", "type": "long"},
               {"name": "b", "type": "string"}],
})
record = {"a": 27, "b": "foo"}

buf = io.BytesIO()
schemaless_writer(buf, schema, record)
data = buf.getvalue()

print("Avro:", data.hex(" "), f"({len(data)} B)")
as_json = json.dumps(record, separators=(",", ":")).encode()
print("JSON:", as_json.decode(), f"({len(as_json)} B)")
