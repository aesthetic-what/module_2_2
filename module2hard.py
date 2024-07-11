def password_unlocker(n): # создаем функцию по подбору пароля
    new_pass = [] # создаем список куда будем вписывать пароль
    for i in range(1, n): # создаем цикл для подбора первого числа
        for j in range(i + 1, n): # создаем цикл для подбора второго числа
            if i == n:
                continue
            elif n % (i + j) == 0: # устанавливаем условие по которому будет вестись подбор чисел
                new_pass.append(f"{i}, {j}") # добавляем подобранные числа в список
    result = new_pass
    return result

n = int(input("Введите число от 3 до 20: "))
print(f"ваше число: {n}, шифр от него: {password_unlocker(n)}")