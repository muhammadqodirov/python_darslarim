

# yoshingiz="Yoshingizni kiriting: "
# while True:
#     age=input(yoshingiz)
#     if age =='quit' or age=='exit':
#         break
#     yosh = int(age)
#     if yosh<=7:
#         narh=2000
#         yosh+=1
#     elif 7<yosh<=18:
#         narh=3000
#     elif 18<yosh<=65:
#         narh=10000
#     else:
#         narh=0
#     if narh == 0:
#         print('Sizga kirish bepul')
#     else:
#         print(f"Sizga kirish {narh} so'm")



# foydalanuvchi="Sevimli kitobingizni kiriting (to'xtatish uchun 'stop' tugmasini bosing): "
# while True:
#     kitoblar=input(foydalanuvchi)
#     if kitoblar == 'stop':
#         break
#     else:
#         print(kitoblar.title())
# print('Buyurtmangiz uchun tashakkur')

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)

# ism=input("Ismingiz nima? ")
# savol=f"Salom {ism.title()}, yoshingiz nechchida? "
# yosh = input(savol)
# yosh=int(yosh)
# height=input(f"{ism.title()} bo'yingiz nechchimetr? ")
# height=float(height)
# print(f"{ism.title()} sizga ma'lumotlar uchun rahmat!")


# olimlar={
#     'navoiy':{
#         'ism':'alisher navoiy',
#         't_yil':1441,
#         't_joyi':'timuriylarni davlatining xirot shahri',
#         'vafot':1501,
#         'umr':59
#         },
#     'buxoriy':{
#         'ism':'Abu Abdulloh Muhammad ibn Ismoil ibn Ibrohim al Buxoriy',
#         't_yil':810,
#         't_joyi':'Buxoro',
#         "vafot":870,
#         'umr':60
#         },
#     'avicenna':{
#         'ism':'Abu Ali ibn Sino',
#         't_yil':980,
#         't_joyi': 'Buxoro',
#         "vafot":1037,
#         'umr':57
#         },
#     'alfraganus':{
#         'ism':'Abul Abbos ibn Muhammad ibn Kasir al-Farg\'oniy',
#         't_yil':798,
#         't_joyi':'Farg\'ona',
#         'vafot':865,
#         'umr':67
#         }
#     }
# for ism, info in olimlar.items():
#     print(f"{info['ism'].title()} {info['t_yil']} yil {info['t_joyi'].title()}da tug'ilgan. {info['vafot']} yil vafot etgan. {info['umr']} umr ko'rgan.")

# menu={
#     'ice-cream':12000,
#     'lavash':23000,
#     'lavash-cheese':26000,
#     'hot-dog':18000,
#     'donar':32000,
#     'coca-cola 1.5l':12000,
#     'coca-cola 0.5l':6000,
#     'fanta 1l':10000,
#     'Dena 1l':12000,
#     'hamburger':17000
#     }
# foydalanuvchi=print("3ta o'zingizga ma'qul bo'lgan narsalarni buyurtma qilsangiz bo'ladi!")
# buyurtmalar=[]
# for buyurtma in range(3):
#     buyurtmalar.append(input(f"{buyurtma+1}chi buyurtmangizni qiling: "))
# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()}ning narhi {menu[buyurtma]}.")
#     else:
#         print(f"Afsuski bizda {buyurtma.title()} yo'q!")



#def increment(a):
#    a+=1
#a=2
#increment(a)
#print(a)
#import calendar
#print(calendar.month(2052, 7))



#davlatlar={
#    'uzbekistan':'tashkent',
#    'malayziya':'kuala-lumpur',
#    'rossiya':'moskva',
#    'aqsh':'vashington',
#    'angliya':'london',
#    'qozoxston':'nursultan',
#    'qirg\'iziston':'bishkek',
#    'tojikiston':'dushanbe'
#    }
#savol=input("Qaysi davlatning poytaxtini bilishni istaysiz?\n>>> ").lower()
#davlat=davlatlar.get(savol)
#if davlat==None:
#    print("Kechirasiz bizda bunday ma'lumot yo'q!")
#else:
#    print(f"{savol.upper()}ning poytaxti {davlat.title()}")

#print('Dunyo davlatlari:')
#for country, capital in sorted(davlatlar.items()):
#    print(country.upper())
#
#print('\nDavlatlarning poytaxtlari:')
#for country, capital in sorted(davlatlar.items()):
#    print(capital.title())


#lugat={'integer':'butun son',
#       'float':"o'nlik sonlar",
#       'sorted':'tartiblash',
#       'title':'katta harf bilan yozish',
#       'upper':'barchasini katta harfda',
#       'lower':'barcha harflarni kichik harfda',
#       'customize':'birinchi harfni katta harfda',
#       'string':'tekst shakli',
#       'for':'uchun',
#       'if':'agar',
#       'while':'toki'
#    }
#for name, value in sorted(lugat.items()):
#    print(f"{name} : {value}")
