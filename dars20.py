# def fibonacci(a):
#     """Fibonacci ketma-ketligi bo'yicha ro'yxatdagi sonlarni qaytaruvchi funksiya"""
#     sonlar=[]
#     for x in range(a):
#         if x ==0 or x==1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar
# print(len(fibonacci(50)))

# def tubson(a,b):
#     """Tub sonlarni qaytaruvchi funksiya"""
#     tub_sonlar=[]
#     for x in range(a, b+1):
#         tub=True
#         if x == 1 or x==0:
#             tub=False
#         elif x == 2:
#             tub=True
#         else:
#             for y in range(2,x):
#                 if x % y ==0:
#                     tub=False
#         if tub:
#             tub_sonlar.append(x)
#     return tub_sonlar
# print(len(tubson(0,1000)))


# def radius(r, p=3.14):
#     """Aylaning radiusi, diametri, perimetri va yuzasini aniqlovchi funksiya"""
#     calculator={
#         'radius':r,
#         'yuza':p*(r**2),
#         'perimetr':2*p*r,
#         'diametr':2*r
#     }
#     return calculator
# # a=radius(41)
# # print(a)
# sonlar=[]
# while True:
#     r=int(input("Radiusni kiriting: "))
#     sonlar.append(radius(r))
#     javob=input("Yana son kiritiasizmi? (ha/yo'q)")
#     if javob !='ha':
#         break
# for calculator in sonlar:
#     print(f"Aylaning radiusi {calculator['radius']}ga teng bo'lganda,"
#           f" aylaning yuzasi {calculator['yuza']}ga, "
#           f"perimetri {calculator['perimetr']}ga, "
#           f"diametri esa {calculator['diametr']}ga teng bo'ladi.")



# def maksimum(a,b,c):
#     """Eng katta sonni chiqaruvchi funksiya"""
#     max=a
#     if b>=max:
#         max=b
#     if c>=max:
#         max=c
#     return max
# maks=maksimum(154,8114,554547)
# print(maks)
# def information(ism,familiya,tyil,tjoy,email='',telefon=None):
#     """Ma'lumotni lug'at ko'rinishida qaytaruvchi funksiya"""
#     info={
#         'ism':ism,
#         'familiya':familiya,
#         'tyil':tyil,
#         'yoshi':2022-tyil,
#         'tjoy':tjoy,
#         'email':email,
#         'telefon':telefon,
#     }
#     return info
# print("Mijoz haqida ma'lumotlarni kiriting:")
# mijozlar=[]
# while True:
#     ism=input("Ismi: ")
#     familiya=input('Familiya: ')
#     tyil=int(input("Tug'ilgan yili: "))
#     tjoy=input("Tug'ilgan joyi: ")
#     email=input("e-mail pochta manzili: ")
#     telefon=input("Telefon raqami: ")
#     mijozlar.append(information(ism,familiya,tyil,tjoy,email,telefon))
#     javob=input("Yana ma'lumot kiritisizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         break
# for info in mijozlar:
#     print(f"{info['ism'].title()} {info['familiya'].title()}, "
#           f"{info['yoshi']} yoshda, {info['tjoy'].title()}dan. "
#           f"e-mail pochta manzili {info['email']}, telefon raqami {info['telefon']} ")



# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto
#
#
# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar = []  # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting ")
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rangi = input("Rangi: ")
#     korobka = input("Korobka: ")
#     yili = input("Ishlab chiqarilgan yili: ")
#     narhi = input("Narhi: ")

    # Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida
    # lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
#
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob == 'no':
#         break
# print(avtolar)
# def oraliq(min,max,c):
#     sonlar = [] # bo'sh ro'yxat
#     while min<max:
#         sonlar.append(min)
#         min +=c
#     return sonlar
# # print(oraliq(0,10))
# print(oraliq(0,21,2))