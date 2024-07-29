import datetime

# Ваша метка времени в миллисекундах
timestamp_ms = 1720167415317

# Преобразуем метку времени из миллисекунд в секунды
timestamp_s = timestamp_ms / 1000.0

# Преобразуем в объект datetime
date_time = datetime.datetime.fromtimestamp(timestamp_s)

# Выводим результат
print(date_time.strftime('%Y-%m-%d %H:%M:%S'))