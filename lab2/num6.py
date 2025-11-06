file_path = r'C:\Users\Jane\Desktop\mbox.txt'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        author_counts = {}

        for line in file:
            if line.startswith('From '):
                parts = line.split()
                if len(parts) > 2 and '@' in parts[1]:
                    email = parts[1]
                    author_counts[email] = author_counts.get(email, 0) + 1

        print("Адреса всех авторов сообщений:")
        for author in author_counts:
            print(author)

        if author_counts:
            max_author = max(author_counts.items(), key=lambda x: x[1])
            print(f"\nАвтор с наибольшим количеством писем: {max_author[0]}")
            print(f"Количество его писем: {max_author[1]}")
        else:
            print("Авторы не найдены")

except Exception as e:
    print(f"Ошибка при чтении файла: {e}")