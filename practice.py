import random
def sontop(x):
    tasodifiy_son=random.randint(1,x)
    print(f"1dan {x}gacha son o'yladim topa olasizmi?")
    taxminlar=0
    while True:
        son=int(input('>>>'))
        taxminlar+=1
        if son > tasodifiy_son:
            print(f"Men o'ylagan son {son}dan kichik")
        elif son<tasodifiy_son:
            print(f"Men o'ylagan son {son}dan katta")
        else:
            break
    print(f"Tabriklayman, siz {taxminlar}ta taxmin bilan topdingiz!")
    return taxminlar

def sontop_pc(x):
    input(f"1dan {x}gacha son o'ylang va xohlagan tugmangizni bosing. Men topaman!\n>>>")
    quyi=1
    yuqori=x
    taxminlar=0
    while True:
        taxminlar+=1
        if quyi !=yuqori:
            taxmin=random.randint(quyi,yuqori)
        else:
            taxmin=quyi
        javob=input(f"Siz {taxmin} sonini o'yladingiz, agar javob to'g'ri bo'lsa(t), javob siz o'ylagan sondan katta bo'lsa(-), bo'lmasa (+)\n>>>".lower())
        if javob =='-':
            yuqori=taxmin-1
        elif javob == '+':
            quyi=taxmin+1
        else:
            break
    print(f"Topdim. Siz o'ylagan sonni {taxminlar}ta urinishda topdim")
    return taxminlar

def play(x):
    yana=True
    while yana:
        taxminlar_user=sontop(x)
        taxminlar_pc=sontop_pc(x)

        if taxminlar_user>taxminlar_pc:
            print("Men yutdim!")
        elif taxminlar_user<taxminlar_pc:
            print("Siz yutdingiz!")
        else:
            print("Durrang")
        yana =int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0): "))


