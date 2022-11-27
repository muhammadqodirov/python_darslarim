# def daraja(n):
#     return lambda x:x**n
# kvadrat=daraja(2)
# kub=daraja(3)
# print(f"3-ning kvadrati {kvadrat(3)}ga teng, kubi {kub(3)}ga teng")

#map() - funksiyasi
# from math import sqrt
# sonlar=list(range(21))
# ildizlar=list(map(sqrt, sonlar))
# print(sonlar)
# print(ildizlar)
# sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
# # def daraja(x):
# #     return x*x
# # print(list(map(daraja, sonlar)))
# kvadratlar=list(map(lambda x:x*x, sonlar))
# print(kvadratlar)

# a=[3,4,7,21]
# b=[7,8,17,21]
# a_plus_b=list(map(lambda x,y:x+y,a,b))
# print(sum(a_plus_b))

# filter() -funksiyasi
# import random as r
# sonlar=r.sample(range(121),21)
#
# juft_sonlar=list(filter(lambda x:x%2==0, sonlar))
# print(sonlar)
# print(juft_sonlar)

mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]
b=list(filter(lambda meva:len(meva)>4, mevalar))
print(b)
