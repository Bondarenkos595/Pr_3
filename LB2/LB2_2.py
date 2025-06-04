import hashlib

def generate_file_hashes(*file_paths):
    file_hashes = {}

    for path in file_paths:
        try:
            with open(path, 'rb') as f:
                file_data = f.read()
                sha256_hash = hashlib.sha256(file_data).hexdigest()
                file_hashes[path] = sha256_hash

        except FileNotFoundError:
            print(f"Помилка: Файл '{path}' не знайдено.")
        except IOError:
            print(f"Помилка: Не вдалося прочитати файл '{path}'.")

    return file_hashes

hashes = generate_file_hashes("document1.txt", "image.png", "not_exist.pdf")

for path, hash_value in hashes.items():
    print(f"{path}: {hash_value}")
