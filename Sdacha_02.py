summa = int(input("Введите сумму покупки: "))
kupjura = int(input("Введите полученную сумму от покупателя: "))
sdacha = kupjura - summa
k_500 = sdacha//500
ost = sdacha%500
k_100 = ost//100
ost = ost%100
k_50 = ost//50
ost = ost%50
k_10 = ost//10
ost = ost%10
k_5 = ost//5
ost = ost%5
k_2 = ost//2
ost = ost%2
k_1 = ost//1
print("Сдача с покупки: ",sdacha)
if k_500>0:
	print("Купюры 500: ",k_500)
if k_100>0:
	print("Купюры 100: ",k_100)
if k_50>0:
	print("Купюры 50: ",k_50)
if k_10>0:
	print("Купюры 10: ",k_10)
if k_5>0:
	print("Монеты 5: ",k_5)
if k_2>0:
	print("Монеты 2: ",k_2)
if k_1>0:
	print("Монеты 1: ",k_1)
