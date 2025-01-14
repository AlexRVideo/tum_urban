def generate_password(n):
    result = ""
    used_numbers = set()

    for i in range(1,21):
        if i in used_numbers:
            continue
        for j in range(i + 1, 21):
            if j in used_numbers:
                continue
            if  (i + j) % n == 0 and (i + j) <= n:
                result += f"{i}{j}"
                used_numbers.add(i)
                used_numbers.add(j)
                break


    return result

n = int(input("Введите число от 3 до 20: "))

if n < 3 or n > 20:
    print("Введенное число должно быть в диапазоне от 3 до 20.")
else:
    password = generate_password(n)
    print(f"{n}: {password}")