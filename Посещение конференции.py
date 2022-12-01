tickets = int(input("Сколько билетов вы хотите приобрести?"))
count = 0
result = ''

for i in range(tickets):
    age = int(input(f"Какой возраст посетителя {i+1}?"))
    if age < 18:
        result = 0
    elif 18 <= age < 25:
        result += 990
    else:
        result += 1390
if tickets > 3:
    result = result * 0.9
    print("Итого стоимость билетов составила:" + str(round(result)) + " рублей с учетом скидки 10%")
else:
    print("Итого стоимость билетов составила:" + str(round(result)) + " рублей")


