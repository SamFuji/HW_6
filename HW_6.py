

# 45. Найти сумму чисел списка стоящих на нечетной позиции

# import random 
# lst = [random.randint(1,100) for i in range (5)]
# print(lst)
# lst_srtd = list(filter(lambda x: not x if lst.index(x)%2==0 else True, lst)) 
# print(lst_srtd)
# res = sum(lst_srtd)
# print(res)



# **44. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21



# a = [int(input(f"Введи {i} координату точки a ")) for i in "xy"]
# b = [int(input(f"Введи {i} координату точки b ")) for i in "xy"]
#
# res = sum([(element[1] - element[0])**2 for element in zip(a,b)])**0.5
#
# print(res)


# 46 Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)



# import random
# a = [random.randint(1,10) for i in range(5)]
# res = [a[indx]*a[-indx-1] for indx in range(len(a)//2+len(a)%2)]
# print(a)
# print(res)


# 47.Сформировать список из N членов последовательности
# Для N=5: 1,-3,9,-27,81 (каждый член больше предыдущего в три раза, знак чередуется)

# a = [(-3)**i for i in range(int(input("Введите число N: ")))]
# print(a)