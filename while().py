savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    son=int(qiymat)
    if son<0:
        print('Bu son musbat emas!')
        continue

    else:
        ildiz = float((son)**(0.5))
        print(f"{son} ning ildizi {ildiz} ga teng")
print("Tugadi!")









#savol="Yoshingizni kiriting: "
#while True:
#    qiymat=input(savol)
#    if qiymat=="exit" or qiymat == 'quit':
#        break
#    yosh=int(qiymat)
#    if yosh <=7:
#        narh=2000
#    elif 7<yosh<=18:
#        narh=3000
#    elif 18<yosh<=65:
#        narh=10000
#    elif yosh>65:
#        narh=0
#    if narh==0:
#        print("Sizga kirish bepul!")
#    else:
#        print(f"Sizga kirish {narh} so'm")

#print("Rahmat!")








#kitoblar="Yaxshi ko'rgan kitoblaringizni kiriting "
#kitoblar+="(Agar dastturni to'xtatmoqchi bo'lsangiz 'stop' so'zini yozing!) :"
#kitob=''
#while kitob !='stop':
#    kitob=input(kitoblar)
#    print(kitob)
#print("Tugadi!")