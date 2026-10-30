import sys

path = sys.argv[1]
limit = int(sys.argv[2]) if len(sys.argv) > 2 else 256

with open(path, "rb") as f:
    data = f.read(limit)

for offset in range(0, len(data), 16):
    chunk = data[offset:offset + 16]
    hexes = " ".join(f"{b:02x}" for b in chunk)
    text = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
    print(f"{offset:08x}  {hexes:<47}  {text}")
