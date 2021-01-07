#Cara a Cara Matemático#

import random

def playcara():
    print(rulescara)
    num = random.randrange(1,51)
    print("Um número foi escolhido!")
    move(num)

rulescara = ["O seguinte jogo é análogo ao conhecido Cara a Cara. Aqui, ao invés de tentar adivinhar qual a pessoa escolhida pelo outro jogador",
"você deverá tentar adivinhar qual número, de 1 a 50, o computador escolheu. Para isso você pode fazer qualquer uma das jogadas legais, essas",
"sendo: \n par, ímpar, primo, fibonacci, altamente composto, palíndromo, quadrado perfeito, cubo perfeito, potência pura de n, divide n, n mod",
"m. \n fazendo uma dessas jogadas, serão eliminados os números que não tem a característica caso o número escolhido a tenha ou serão eliminados",
"os números que tem essa característica caso o número escolhido não a tenha. \n Além dessas jogadas, você também pode fazer um chute, digitando",
"apenas o número que você acha que o computador escolheu. Caso você esteja correto, você ganha o jogo! Caso contrário, você perde.",
"\n É importante ressaltar que sua jogada não será reconhecida caso você não a escreva exatamente como o indicado. Espaços são importantes",
", capitalização e acentos não importam. Caso precise se lembrar quais são as jogadas possíveis, digite jogadas. \n Divirta-se!"]

rulescara = " ".join(rulescara)

legalmoves = ["par", "impar", "primo", "fibonacci", "altamente composto", "palindromo", "quadrado perfeito", "cubo perfeito",
"potencia pura de n", "divide n", "n mod m"]

moves=[]

fib = [1,2,3,5,8,13,21,34]
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
pftsqr = [1,4,9,16,25,36,49]
pftcube = [1,8,27]
palindrome = [11,22,33,44]
comp = [1,2,4,6,12,24,36,48]

def move(num):
    i=input("Qual é a sua jogada? ").lower()
    i=norm(i)
    try:
        i = int(i)
        if i == num:
            print("Parabéns! Você acertou!")
            return
        else:
            print("Que pena! Você errou, o número correto era ",num,".",sep = "")
            return
    except:
        l=i.split()
        if len(l) == 1:
            if l[0] == "jogadas":
                print(", ".join(legalmoves[:len(legalmoves)-1])+", "+legalmoves[-1])
                move(num)
            else:
                n = 0
                while (l[0] != legalmoves[n]) and (n < len(legalmoves) - 1):
                    n += 1
                if n < len(legalmoves) - 1:
                    act(n,num)
                else:
                    print("Essa não é uma jogada possível.")
                    move(num)
        elif len(l) == 2:
            if l[0] == "divide":
                try:
                    n = int(l[1])
                    for item in range(1,51):
                        if ((n%num == 0) and (n%item != 0)) or ((n%num != 0) and (n%item == 0)):
                            moves.append(item)
                except:
                    print("Essa não é uma jogada possível.")
                    move(num)
            elif l[1] == "perfeito":
                if l[0] == "quadrado":
                    act(6,num)
                elif l[0] == "cubo":
                    act(7,num)
                else:
                    print("Essa não é uma jogada possível.")
                    move(num)
            else:
                print("Essa não é uma jogada possível.")
                move(num)
        elif len(l) == 3:
            if l[1] == "mod":
                try:
                    n=int(l[0])
                    m=int(l[2])
                    for item in range(1,51):
                        if ((num%m == n) and (item%m != n)) or ((num%m != n) and (item%m == n)):
                            moves.append(item)
                except:
                    print("Essa não é uma jogada possível.")
                    move(num)
            else:
                print("Essa não é uma jogada possível.")
                move(num)
        elif len(l) == 4:
            if l[0] == "potencia":
                try:
                    n = int(l[3])
                    for item in range(1,51):
                        if pftpwr(n,num) != pftpwr(n,item):
                            moves.append(item)
                except:
                    print("Essa não é uma jogada possível.")
                    move(num)
            else:
                print("Essa não é uma jogada possível.")
                move(num)
        else:
            print("Essa não é uma jogada possível.")
            move(num)
        screen(moves)
        move(num)

def act(n,num):
    if n==0 or n==1:
        for item in range(1,51):
            if item%2 != num%2:
                moves.append(item)
    elif n==2:
        for item in range(1,51):
            if ((num in primes) and (item not in primes)) or ((num not in primes) and (item in primes)):
                moves.append(item)
    elif n==3:
        for item in range(1,51):
            if ((num in fib) and (item not in fib)) or ((num not in fib) and (item in fib)):
                moves.append(item)
    elif n==4:
        for item in range(1,51):
            if ((num in comp) and (item not in comp)) or ((num not in comp) and (item in comp)):
                moves.append(item)
    elif n==5:
        for item in range(1,51):
            if ((num in palindrome) and (item not in palindrome)) or ((num not in palindrome) and (item in palindrome)):
                moves.append(item)
    elif n==6:
        for item in range(1,51):
            if ((num in pftsqr) and (item not in pftsqr)) or ((num not in pftsqr) and (item in pftsqr)):
                moves.append(item)
    elif n==7:
        for item in range(1,51):
            if ((num in pftcube) and (item not in pftcube)) or ((num not in pftcube) and (item in pftcube)):
                moves.append(item)

def pftpwr(n, x):
    e=0
    m=1
    pure = 0
    while e<= 50:
        e = n**m
        if e == x:
            pure = 1
        m += 1
    return pure

def screen(moves):
    for n in range(1,51):
        if n%10==0:
            if n in moves:
                print("x")
            else:
                print(n)
        else:
            if n in moves:
                print("x", end = " ")
            else:
                print(n, end=" ")

def norm(item):
    a = ["à","á","â","ä","æ","ã","å","ā"]
    e = ["è","é","ê","ë","ē","ė","ę"]
    i = ["î","ï","í","ī","į","ì"]
    o = ["ô","ö","ò","ó","œ","ø","ō","õ"]
    u = ["û","ü","ù","ú","ū"]
    n=0
    while n < len(item):
        if item[n] in a :
            item = item[0,n] + "a" + item[n+1,]
        elif item[n] in e:
            item = item[0,n] + "e" + item[n+1,]
        elif item[n] in i:
            item = item[0,n] + "i" + item[n+1,]
        elif item[n] in o:
            item = item[0,n] + "o" + item[n+1,]
        elif item[n] in u:
            item = item[0,n] + "u" + item[n+1,]
        n +=1
    return item

playcara()
