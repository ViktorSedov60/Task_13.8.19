N = int(input("введите необходимое колличество билетов - "))
result = 0


for i in range(1, N+1):
    age = int(input(f"ведите возраст посетителя номер {i} - "))
    if 18 <= age < 25:
      result += 990
    if age >= 25:
      result += 1390
print(f"сумма к оплате - {result}  рублей")

