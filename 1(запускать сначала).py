user_name = (input("Введите ваше имя : "))
user_data = int(input("Введите ваш возраст : "))

if user_data < 18:
    print(f"Ваше имя : {user_name}")
    print(f"Ваш возраст : {user_data}")
    print("К сожелению вы не проходите по возрасту, минимальный возраст 18 лет")
else :
    print(f"Ваше имя : {user_name}")
    print(f"Ваш возраст : {user_data}")
    print("Поздравляем вы прошли проверку")


with open("main.txt", "w", encoding="utf-8") as file:
    file.write(f"Имя: {user_name}\n")
    file.write(f"Возраст: {user_data}\n")