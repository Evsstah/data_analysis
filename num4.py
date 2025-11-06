def main():
    # Чтение данных из файла
    with open('input.txt', 'r', encoding='utf-8') as f:
        participants = f.readline().split()
        n = int(f.readline())
        purchases = []
        for i in range(n):
            name, amount = f.readline().split()
            purchases.append((name, int(amount)))

    # Расчет расходов
    expenses = {name: 0 for name in participants}
    for name, amount in purchases:
        expenses[name] += amount

    # Расчет среднего и балансов
    total = sum(expenses.values())
    average = total / len(participants)

    print("РАСЧЕТ ДОЛГОВ ДЛЯ ПОХОДА")
    print(f"Участники: {', '.join(participants)}")
    print(f"Общие расходы: {total} руб.")
    print(f"Средние затраты на человека: {average:.2f} руб.\n")

    # Разделение на тех, кто заплатил больше/меньше среднего
    debts = []
    creditors = []

    for name in participants:
        balance = expenses[name] - average
        if balance < -0.01:
            debts.append((name, -balance))
        elif balance > 0.01:
            creditors.append((name, balance))

    # Минимизация переводов
    debts.sort(key=lambda x: x[1], reverse=True)
    creditors.sort(key=lambda x: x[1], reverse=True)

    transfers = []
    i = j = 0

    while i < len(debts) and j < len(creditors):
        debtor, debt_amount = debts[i]
        creditor, credit_amount = creditors[j]
        amount = min(debt_amount, credit_amount)

        transfers.append((debtor, creditor, round(amount, 2)))

        debts[i] = (debtor, debt_amount - amount)
        creditors[j] = (creditor, credit_amount - amount)

        if debts[i][1] < 0.01:
            i += 1
        if creditors[j][1] < 0.01:
            j += 1

    # Вывод результатов
    print(f"Минимальное количество переводов: {len(transfers)}")
    print("\nСписок переводов:")
    for debtor, creditor, amount in transfers:
        print(f"{debtor} => {creditor}: {amount:.2f} руб.")


if __name__ == "__main__":
    main()
