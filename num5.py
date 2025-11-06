from datetime import datetime


def read_data_from_file(filename):
    orders = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line:
                    continue

                parts = line.split(',')
                if len(parts) != 3:
                    print(f"Ошибка в строке {line_num}: неверный формат данных")
                    continue

                date_str, pizza, price_str = parts

                try:
                    date = datetime.strptime(date_str.strip(), '%d.%m.%Y').date()
                    pizza_name = pizza.strip()
                    price = int(float(price_str.strip()))

                    orders.append({
                        'date': date,
                        'pizza': pizza_name,
                        'price': price
                    })
                except ValueError as e:
                    print(f"Ошибка в строке {line_num}: {e}")
                    continue

    except FileNotFoundError:
        print(f"Файл '{filename}' не найден")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []

    return orders


def analyze_orders(orders):
    if not orders:
        print("Нет данных для анализа")
        return

    # а)
    pizza_stats = {}
    for order in orders:
        pizza_name = order['pizza']
        if pizza_name in pizza_stats:
            pizza_stats[pizza_name] += 1
        else:
            pizza_stats[pizza_name] = 1

    print("\nПИЦЦЫ (по популярности):")

    for pizza, count in sorted(pizza_stats.items(), key=lambda x: x[1], reverse=True):
        print(f"{pizza}: {count}")

    # б)
    date_stats = {}
    for order in orders:
        date = order['date']
        if date in date_stats:
            date_stats[date] += order['price']
        else:
            date_stats[date] = order['price']

    print("\nДАТЫ (хронологически):")

    for date in sorted(date_stats.keys()):
        formatted_date = date.strftime('%d.%m.%Y')
        print(f"{formatted_date}, {date_stats[date]} руб.")

    # в)
    most_expensive = max(orders, key=lambda x: x['price'])
    print("\nСАМЫЙ ДОРОГОЙ ЗАКАЗ:")

    formatted_date = most_expensive['date'].strftime('%d.%m.%Y')
    print(f"Дата: {formatted_date}")
    print(f"Пицца: {most_expensive['pizza']}")
    print(f"Стоимость: {most_expensive['price']} руб.")

    # г)
    total_price = sum(order['price'] for order in orders)
    average_price = total_price / len(orders)
    print("\nСРЕДНЯЯ СТОИМОСТЬ ЗАКАЗА:")
    print(f"{int(average_price)} руб.")


def main():
    filename = "filename.txt"

    orders = read_data_from_file(filename)

    if orders:
        analyze_orders(orders)
    else:
        print("Не удалось загрузить данные для анализа")


if __name__ == "__main__":
    main()