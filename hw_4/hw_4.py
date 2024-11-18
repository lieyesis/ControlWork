from decouple import Config

# Создаем объект Config, который будет читать из .env файла
config = Config()

# Потом нужно будет применять эти значения из .env файла
username = config('USERNAME')
password = config('PASSWORD')

#Потом просто принтуем
print(f"Username: {username}")
print(f"Password: {password}")
