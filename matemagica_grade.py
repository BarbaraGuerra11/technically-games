def digitos(n):
    d = 1
    while n//10!=0:
        n = n//10
        d+=1
    return d

def visualizar(grade):
    n = len(grade)
    m = digitos(n**2)
    for i in grade:
        print("-"*((m+1)*n + 1))
        for j in i:
            k = m - digitos(j)
            k1 = k//2
            if k%2==0:
                k2 = k1
            else:
                k2 = k1 + 1
            print("|", " "*k1, j, " "*k2, sep="", end="")
        print("|")
    print("-"*((m+1)*n + 1))

def criargrade(ordem):
    t = []
    for i in range(1, ordem + 1):
        l = []
        for j in range(1, ordem + 1):
            l.append((i - 1)*ordem + j)
        t.append(l)
    visualizar(t)
    return t

def trocarlinha(grade, linha1, linha2):
    n = len(grade)
    if 0 <= linha1 < n or 0 <= linha2 < n:
        l1 = grade[linha1 - 1]
        l2 = grade[linha2 - 1]
        grade[linha1 - 1] = l2
        grade[linha2 - 1] = l1
        visualizar(grade)
    else:
        print("Encolha inválida, tente de novo.")

def trocarcoluna(grade, coluna1, coluna2):
    n = len(grade)
    if 0 <= coluna1 < n or 0 <= coluna2 < n:
        for i in grade:
            c1 = i[coluna1 - 1]
            c2 = i[coluna2 - 1]
            i[coluna1 - 1] = c2
            i[coluna2 - 1] = c1
        visualizar(grade)
    else:
        print("Encolha inválida, tente de novo.")

def escolher(grade, linha, coluna):
    n = len(grade)
    k = grade[linha - 1][coluna - 1]
    if k == 0:
        print("Escolha inválida, tente de novo.")
    else:
        for i in range(n):
            grade[linha - 1][i] = 0
            grade[i][coluna - 1] = 0
        grade[linha - 1][coluna - 1] = k
        visualizar(grade)

def soma(grade):
    n = len(grade)
    s = 0
    for i in range(n):
        for j in range(n):
            s += grade[i][j]
    return s

def somagrade(ordem):
    n = ordem
    return n*(n**2 + 1)//2
