with open("main.txt", "r", encoding="utf-8") as file:
  lines = file.readlines()


user_name = lines[0].strip()
user_data = (lines[1].strip())

print(f"Имя: {user_name}, Возраст: {user_data}")