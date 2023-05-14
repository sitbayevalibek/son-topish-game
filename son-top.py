# Son topish o'yini 
import random as r

def son_top(x=10):
    t_son = r.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim topaolasizmi?")
    taxminlar = 0
    while True:
        taxminlar +=1
        taxmin = int(input(">>>"))
        if taxmin<t_son:
            print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling!")
        elif taxmin>t_son:
            print("Xato. Men o'ylagan son bundan kichikroq. Yana harakat qiling!")
        else:
            break
    print(f"Tabriklayman. Siz {taxminlar} taxmin bilan topdingiz")
    return taxminlar

def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan raqamni bosing. Men topaman\n>>>")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar +=1
        if quyi != yuqori:
            taxmin = r.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz. To'g'ri bo'lsa (t)."
                      f"Men o'ylagan son bundan kattaroq (+)."
                      f"Men o'ylagan son bundan kichikroq (-).\n>>>")
        if javob == "-":
            yuqori = taxmin - 1
        elif javob =="+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim")
    return taxminlar

def play(x=10):
    yana = True
    while yana:
        t_user = son_top() 
        t_pc = sontop_pc()
        if t_user>t_pc:
            print("Men yutdim")
        elif t_user<t_pc:
            print("Siz yutdingiz")
        else:
            print("Durrang")
        yana = int(input("Yana o'ynaymizmi ha(1) yo'q(0)"))
        
        
        
        