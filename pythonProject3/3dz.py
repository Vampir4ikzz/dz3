result = []
def divider(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Передано невірні типи даних для ділення")
    if a < b:
        raise ValueError("Помилка: 'a' менше за 'b'")
    if b > 100:
        raise IndexError("Помилка: 'b' більше за 100")
    return a / b
data = {10: 2, 2: 5, "123": 4, 18: 0, (1, 2): 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as e:
        print(f"Перехоплено виняток для ключа '{key}': {type(e).__name__} — {e}")
print("\nПідсумковий результат успішних ділень:")
print(result)