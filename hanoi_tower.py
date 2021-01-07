yes=["yes","yup","yep","sim","alright","all right","allright","ya","yas","ye",
     "sure","by all means","why not","why not?","indeed","agreed","roger",
     "affirmative","right","very well","of course","aye","ok","k","good","okay",
     "okey dokey","yeah","fine","s"]

def printtower(towers,tower,n):
    t=towers[tower][:]
    while len(t)<n:
        t.append(0)
    print(38*" "+tower)
    k=n-1
    while k>=0:
        disk=(41-t[k])*" "+t[k]*"-"+"|"+t[k]*"-"
        print(disk)
        k-=1

def printtowers(towers,n):
    for tower in towers.keys():
        printtower(towers,tower,n)
        print()

def solve(n,t1,t2,t3):
    if n==1:
        print(t1,"to",t3)
    else:
        solve(n-1,t1,t3,t2)
        print(t1,"to",t3)
        solve(n-1,t2,t1,t3)
    
def move(s,towers,n):
    try:
        if s.lower()=="restart":
            hanoi(n)
        elif s.lower()=="new game":
            print()
            callhanoi()
        elif s.lower()=="solve":
            print()
            solve(n,"1","2","3")
        else:
            s=s.lower()
            ft,tt=s.split(" to ")
            ft,tt=int(ft),int(tt)
            movedisk(ft,tt,towers)
    except:
        print("Sorry, you have picked an invalid move.")
        s=input("What will your move be? ")
        move(s,towers,n)

def movedisk(ft,tt,towers):
    l=list(towers.keys())
    ft,tt=l[ft-1],l[tt-1]
    if len(towers[ft])>0 and len(towers[tt])>0:
        if towers[ft][-1]>towers[tt][-1]:
            print("Sorry, you have picked an invalid move.")
            s=input("What will your move be? ")
            move(s,towers,n)
        else:
            towers[tt].append(towers[ft][-1])
            del towers[ft][-1]
    elif len(towers[ft])>0:
        towers[tt].append(towers[ft][-1])
        del towers[ft][-1]
    else:
        print("Sorry, you have picked an invalid move.")
        s=input("What will your move be? ")
        move(s,towers,n)
    

print("Welcome to Tower of Hanoi!\n\nThe objective of the game is to move all",
      "the disks from the first tower to the last and the rules are as",
      "follows:\n\t1.You can only move one disk per move;\n\t2.You can only",
      "move the top disk from a tower;\n\t3.You can only move a disk to the",
      "top of another tower;\n\t4.You can only put a smaller disk on top of",
      "another.\n\nYour moves must be written as follows:\nFT to TT\nIn which",
      "FT is the number of the tower from which you want to remove a disk and",
      "TT is the number of the tower on which you wish to place that",
      "disk.\n\nAlternatively,type ""restart"" to start a new game with the",
      "same number of disks, ""new game"" to start a new game with a new",
      "number of disks, or ""solve"" for the list of moves of the optimal",
      "solution for that number of disks.\n")

def callhanoi():
    try:
        n=int(input("How many disks would you like to play with? "))
        if n>0:
            hanoi(n)
        else:
            print("Sorry, you have picked an invalid move.")
            callhanoi() 
    except:
        print("Sorry, you have picked an invalid move.")
        callhanoi()

def hanoi(n):
    l=list(range(1,n+1))
    l.reverse()
    towers={"Tower 1":l,"Tower 2":[],"Tower 3":[]}
    win=False
    t=0
    while not win:
        print()
        printtowers(towers,n)
        s=input("What will your move be? ")
        move(s,towers,n)
        t+=1
        print()
        if len(towers["Tower 3"])==n:
            win=True
            printtowers(towers,n)
            if t==2**n-1:
                print("Congrats! You did it in",t,"tries! That's the optimal",
                      "solution!")
            else:
                print("You suck! You did it in",t,"tries! The optimal solution",
                      "takes",2**n-1,"moves, far less than it took you!")
    print()
    i=input("Would you like to play again? ")
    if i.lower() in yes:
        print()
        callhanoi()
    else:
        return

callhanoi()
