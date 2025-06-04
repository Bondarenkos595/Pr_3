def analyze_log_file(log_file_path):
    response_codes = {}

    try:
        with open(log_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 9:
                    code = parts[8]
                    if code.isdigit():
                        response_codes[code] = response_codes.get(code, 0) + 1
        return response_codes

    except FileNotFoundError:
        print(f"Помилка: Файл '{log_file_path}' не знайдено.")
    except IOError:
        print(f"Помилка: Не вдалося прочитати файл '{log_file_path}'.")

    return {}

log_stats = analyze_log_file("apache_logs.txt")
print("Статистика HTTP-кодів:")
print(log_stats)