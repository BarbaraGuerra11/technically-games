#Jogo do Nim#

#Versão 1: Linha#

placar=[]

def computador_escolhe_jogada(n,m):
    if m>=n:
        c=n
    elif n%(m+1)==0:
        c=m
    else:
        c=n%(m+1)
    return c

def usuario_escolhe_jogada(n,m):
    p=input("Quantas peças você vai tirar? ")
    try:
        p=int(p)
        if (p<1) or (p>m) or (p>n):
            print()
            print("Oops! Jogada inválida! Tente de novo. ")
            print()
            usuario_escolhe_jogada(n,m)
    except:
        print()
        print("Oops! Jogada inválida! Tente de novo. ")
        print()
        usuario_escolhe_jogada(n,m)
    return p

def partida():
    n=invalidn()
    m=invalidm()
    if (n%(m+1)!=0) or (m>=n):
        print()
        print("Computador começa!")
        print()
        c=computador_escolhe_jogada(n,m)
        n=n-c
        if c==1:
            print("O computador tirou uma peça.")
        else:
            print("O computador tirou",c,"peças.")
        if n==1:
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            print("Agora restam",n,"peças no tabuleiro.")
            print()
    else:
        print()
        print("Voce começa!")
        print()
    if n==0:
        print("Fim do jogo! O computador ganhou!")
        placar.append("c")
        print()
    else:
        while True:
            p=usuario_escolhe_jogada(n,m)
            n=n-p
            if p==1:
                print("Você tirou uma peça.")
            else:
                print("Voce tirou",p,"peças.")
            if n>0:
                if n==1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                else:
                    print("Agora restam",n,"peças no tabuleiro.")
                print()
                c=computador_escolhe_jogada(n,m)
                n=n-c
                if c==1:
                    print("O computador tirou uma peça.")
                else:
                    print("O computador tirou",c,"peças.")
                if n==1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                elif n==0:
                    print("Fim do jogo! O computador ganhou!")
                    placar.append("c")
                    print()
                    break
                else:
                    print("Agora restam",n,"peças no tabuleiro.")
                    print()
            else:
                print("Fim do jogo! Você ganhou!")
                placar.append("p")
                print()
                break

def invalidn():
    n=input("Quantas peças? ")
    try:
        n=int(n)
    except:
        print("Essa não é uma escolha válida!")
        invalidn()
    return n

def invalidm():
    m=input("Limite de peças por jogada? ")
    try:
        m=int(m)
    except:
        print("Essa não é uma escolha válida!")
        invalidm()
    return m

def invalidk():
    k=input()
    try:
        k=int(k)
        if k != 1 and k != 2:
            print("Essa não é uma escolha válida!")
            invalidk()
    except:
        print("Essa não é uma escolha válida!")
        invalidk()
    return k

def playnimv1():
    print("Bem-vindo ao jogo do NIM!")
    print("O objetivo é tirar a última peça do tabuleiro. Boa Sorte!")
    print("Escolha:")
    print()
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato ")
    k=invalidk()
    if k==1:
        print("Voce escolheu uma partida isolada!")
        print()
        partida()
    else:
        print()
        print("Voce escolheu um campeonato!")
        print()
        i=1
        while i<=3:
            print("**** Rodada",i,"****")
            print()
            partida()
            i=i+1
        print("**** Final do campeonato! ****")
        print()
        playa=0
        comp=0
        for e in placar:
            if e=="p":
                playa=playa+1
            if e=="c":
                comp=comp+1
        print("Placar: Você",playa,"X",comp,"Computador")

playnimv1()
