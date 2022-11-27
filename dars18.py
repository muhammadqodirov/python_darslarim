buyurtmalar=[]
print("O'zingizga kerakli bo'lgan mahsulotlar nomini kiriting")
n=1
while True:
    savol=input(f"{n}chi mahsulotni kiriting: ")
    buyurtmalar.append(savol)
    javob=input("Yana mahslot kiritasizmi?(ha/yo'q)")
    if javob=='ha':
        n += 1
        continue
    else:
        break
print(f"Buyurtmalaringiz ro'yhati:")
for buyurtma in buyurtmalar:
    print(buyurtma)

print("Mahsulotlar va ularning narhlarini kiriting")
e_bozor={}
ishora=True
while ishora:
    mahsulot = input("Mahsulotni kiriting: ")
    narh = input("Mahsulotning narhini kiriting: ")
    e_bozor[mahsulot] = int(narh)
    javob = input("Yana mahsulot kiritasizmi?(ha/yo'q) >>")
    if javob =="yo'q":
        ishora=False
while buyurtmalar:
    buyurtma=buyurtmalar.pop()
    if buyurtma in e_bozor.keys():
        narh=e_bozor[buyurtma]
        print(f"{buyurtma.customize()}ning narhi {narh}")
    else:
        print(f"Bizda {buyurtma} yo'q")


# for bozorlik,narh in e_bozor.items():
#     if bozorlik in buyurtmalar:
#         print(f"{bozorlik}ning narhi {narh} so'm")
#     else:
#         print(f"Bizda {buyurtma} mavjud emas!")



# while True:
#     mahsulot=input("Mahsulotni kiriting: ")
#     narh=input("Mahsulotning narhini kiriting: ")
#     e_bozor[mahsulot]=int(narh)
#     javob=input("Yana mahsulot kiritasizmi?(ha/yo'q)")
#     if javob =='ha':
#         continue
#     else:
#         break
# for zakaz, narh in e_bozor.items():
#     print(f"{zakaz}ning narhi {narh} so'm")


