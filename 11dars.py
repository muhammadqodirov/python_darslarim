son=int(input("Istagan butun son kiriting: "))
for n in range(2,11):
    if not(son%n):
        print(f"{son} soni {n}ga qoldiqsiz bo'linadi")
    else:
        print(f"Siz kiritgan {son} soni {n}ga qoldiqsiz bo'linmaydi!")
foydalanuvchilar=['muhammad','muhammad01','tello7097','abror','muhammad.me']
login=input("Yangi login kiriting: ")
if login in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print("Xush kelipsiz!")
mahsulotlar=['nok','olma', 'olcha','shaftoli', 'bodring', 'piyoz','tarvuz', 'go\'sht','qo\'y go\'shti','shakar']
savat=[]
print("Savatga 5ta mahsulot kiriting: ")
for n in range(5):
    savat.append(input(f"{n+1} chi mahsulotni kiriting: "))
bor_mahsulotlar=[]
mavjud_emas=[]
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if mavjud_emas:
    print("Quyidagi mahsulotlar do'konimizda yo'q.")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda mavjud!")
for n in range(5):
    savat.append(input(f"{n+1}chi mahsulotni kiriting: "))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
    else:
        print(f"Do'konimizda {mahsulot} yo'q.")
print("Ikkita son kiriting: ")
a=int(input('Birinchi sonni kiriting: '))
b=int(input("Ikkinchi sonni kiriting: "))
print(f"{a}>{b}") if a>b else print(f"{a}<{b}")
yosh=int(input("Yoshingizni kiriting: "))
if yosh<=4 or yosh>=60:
    print("Kirish bepul")
elif yosh<=18:
    print("Kirish 10000")
elif yosh>=18:
    print("Kirish 20000")
son=int(input("Jusft son kiriting: "))
if son%2:
    print("Bu juft son emas!")
else:
    print('Rahmat')