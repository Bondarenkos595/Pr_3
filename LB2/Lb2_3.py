def filter_ips(input_file_path, output_file_path, allowed_ips):
    ip_counts = {}

    try:
        with open(input_file_path, 'r', encoding='utf-8') as infile:
            for line in infile:
                parts = line.strip().split()
                if len(parts) > 0:
                    ip = parts[0]
                    if ip in allowed_ips:
                        ip_counts[ip] = ip_counts.get(ip, 0) + 1

    except FileNotFoundError:
        print(f"Помилка: Вхідний файл '{input_file_path}' не знайдено.")
        return
    except IOError:
        print(f"Помилка: Не вдалося прочитати вхідний файл '{input_file_path}'.")
        return

    try:
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            for ip, count in ip_counts.items():
                outfile.write(f"{ip} - {count}\n")

    except IOError:
        print(f"Помилка: Не вдалося записати у файл '{output_file_path}'.")

allowed_ips = ["66.249.73.135", "218.30.103.62", "178.191.44.227"]
filter_ips("apache_logs.txt", "filtered_ips.txt", allowed_ips)
