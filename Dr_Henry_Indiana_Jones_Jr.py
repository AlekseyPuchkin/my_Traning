def generate_password(n):
    pairs = []
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if i != j:
                pairs.append((i, j))
    result = ""
    for pair in pairs:
        sum_pair = sum(pair)
        if n % sum_pair == 0:
            result += f"{pair[0]}{pair[1]}"
    return result
attempts = 3
while attempts > 0:
    try:
        n = int(input("Введите число от 3 до 20: "))
        if n < 3 or n > 20:
            print("Число должно быть в диапазоне от 3 до 20! Попробуйте снова.")
            attempts -= 1
            print(f"Количество оставшихся попыток: {attempts}")
            continue
        break
    except ValueError:
        print("Пожалуйста, введите целое число! Попробуйте снова.")
        attempts -= 1
        print(f"Количество оставшихся попыток:{attempts} ")
if attempts == 0:
    print("Потрачено!")
    exit()
password = generate_password(n)
print(f"Пароль для числа {n}: {password}")