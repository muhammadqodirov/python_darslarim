import random
print("Keling o'ylagan sonni topish o'yaymiz")
def sontop(x):
    print(f"1dan {x}gacha son o'yladim, topa olasizmi?")
    pc_sonlar = random.randint(1, x)
    taxminlar=0
    while True:
        taxmin=int(input(f">>>"))
        taxminlar+=1
        if taxmin >pc_sonlar:
            print(f"Men o'ylagan son {taxmin}dan kichik")
        elif taxmin<pc_sonlar:
            print(f"Men o'ylagan son {taxmin}dan katta")
        else:
            break
    print(f"Tabriklayman, siz men o'ylagan sonni {taxminlar}ta urinishda topdingiz")
    return taxminlar


def sontop_pc(x):
    input(f"Endi siz 1dan {x}gacha bo'lgan sonni o'ylang va xohlagan tugmangizni bosing. Men topaman.\n>>>")
    taxminlar = 0
    quyi=1
    yuqori=x
    while True:
        taxminlar+=1
        if yuqori!=quyi:
            pc=random.randint(quyi, yuqori)
        else:
            pc=quyi
        javob=input(f"Siz {pc} sonini o'yladingiz, agar to'g'ri bo'lsa (yes) tugmasini bosing, agar siz o'ylagan sondan katta bo'lsa (-), bo'lmasa (+).\n>>>")
        if javob =='-':
            yuqori=pc-1
        elif javob =='+':
            quyi=pc+1
        else:
            print(f"Topdim, men siz o'ylagan sonni {taxminlar}ta urinishda topdim!")
            return taxminlar

def play(x):
    yana=True
    while yana:
        taxmin_user=sontop(x)
        taxmin_pc=sontop_pc(x)
        if taxmin_user>taxmin_pc:
            print(f"Men yutdim, siz o'ylagan sonni {taxmin_pc} urinishda topdim")
        elif taxmin_user<taxmin_pc:
            print(f"Siz yutdingiz, siz men o'ylagan sonni {taxmin_user} urinishda topdingiz")
        else:
            print("O'yin uchun rahmat, durrang bo'ldi!")
        yana=int(input(f"Yana o'ynaymizmi? Ha(1)/yo'q(0)\n>>"))
print(play(10))


