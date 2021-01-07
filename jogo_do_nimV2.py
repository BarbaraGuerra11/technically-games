#Jogo do Nim#

#Versão 2: Piramide, Riscando quanto quiser da linha#

def playnimv2():
    print(rulesnimv2)
    i=input("Quantas linhas você quer? ")
    i=int(i)
    n = 0
    for item in range(0,i):
        n += (2*item +1)
    pyr1 = "| "*(n-1) + "|"
    pyr1 = pyr1.split()
    prtpyr1(n,pyr1)
    play(n, pyr1)

def prtpyr1(n,pyr):
    e = 0
    m = 1
    while e < n:
        i = 1
        while i <= m:
            if i == 1:
                if m == 3:
                    print(" "*(42-((m-1)//2)) + pyr[e], end="")
                else:
                    print(" "*(41-((m-1)//2)) + pyr[e], end="")
            elif 1 < i < m:
                print(pyr[e], end="")
            else:
                print(pyr[e])
            e += 1
            i += 1
        m += 2

def play(n, pyr):
    while "|" in pyr:
        i = chooseplay(n)
        m = 0
        for item in range(0,i[0]):
            m += (2*item + 1)
        pyr[m + i[1] : m + i[2] + 1] = ["-"]*len(pyr[m + i[1] : m + i[2] + 1])
        prtpyr1(n, pyr)
    print("O jogo acabou! Quem ganhou?")

def chooseplay(n):
    i = input("Qual jogada você quer fazer? ")
    i = i.split()
    try:
        i = (int(i[0]) - 1, int(i[1]) - 1, int(i[2]) - 1)
        if (i[0] >= n) or (i[0] < 0):
            print("Essa jogada é invalida.")
            chooseplay(n)
        elif (i[1] > (i[0]*2 + 1)) or (i[1] < 0):
            print("Essa jogada é invalida.")
            chooseplay(n)
        elif (i[2] > (i[0]*2 + 1)) or (i[2] < i[1]):
            print("Essa jogada é invalida.")
            chooseplay(n)
        else:
            return i
    except:
        print("Essa jogada é invalida.")
        chooseplay(n)

rulesnimv2 = ["Bem vindo ao Jogo do NIM! \n \n O objetivo do jogo é forçar seu oponente a riscar o último traço! Jogue com um amigo, alternando",
"jogadas até que o último traço seja riscado. Você pode riscar qualquer número de traços na sua jogada, desde que todos estejam na mesma linha.",
"\n A jogada deve ser a forma: \n x y z \n em que x é a linha da qual você quer riscar traços, y a primeira peça da linha que você quer riscar",
" e z a última. Por favor escreva as jogadas exatamente dessa forma, ou poderá haver problemas na leitura da sua jogada. \n \n Divirta-se!"]

rulesnimv2 = " ".join(rulesnimv2)

playnimv2()
