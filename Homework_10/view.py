import tb


while True:
    data = tb.read(2)
    if not data or len(data) < 2:
        break
    key, value = data
    if isinstance(value, bytes):
        text = value.decode('utf-8', errors='replace')
    else:
        text = str(value)
    print(text.strip())