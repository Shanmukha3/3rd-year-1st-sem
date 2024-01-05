def board_print(board,n):
    for i in range(n):
        for j in range(n):
            print(board[i][j],end='')
            if(j!=n-1):
                print(' | ',end='')
        print()
        
def haswon(board,player,dict,p,q,n):
    c=0
    for i in range(n):
        if(board[p-1][i]==dict[player]):
            c=c+1
            if(c==n):
                print()
                print(dict[player]," has won")
                print()
                return 1
    c=0
    for i in range(n):
        if(board[i][q-1]==dict[player]):
            c=c+1
            if(c==n):
                print()
                print(dict[player]," has won")
                print()
                return 1
    c=0
    for i in range(n):
        if(board[i][i]==dict[player]):
            c=c+1
            if(c==n):
                print()
                print(dict[player]," has won")
                print()
                return 1
    c=0
    for i in range(n):
        if(board[i][n-1-i]==dict[player]):
            c=c+1
            if(c==n):
                print()
                print(dict[player]," has won")
                print()
                return 1
    return 0
    
    
def draw(board,n):
    for i in range(n):
        for j in range(n):
            if(board[i][j]==' '):
                return 0
    return 1
    
    
def tic_tae_toe(board,n):
    board_print(board,n)
    dict={0:'O',1:'X'}
    player=0
    while(True):
        print("now its ",dict[player]," turn")
        p=int(input("Enter the row:"))
        q=int(input("Enter the column:"))
        if(board[p-1][q-1]==' '):
            board[p-1][q-1]=dict[player]
            board_print(board,n)
            x=haswon(board,player,dict,p,q,n)
            if(x==1):
                break
            z=draw(board,n)
            if(z==1):
                print()
                print("matche is draw")
                break
        else:
            print("this box is already filled")
            board_print(board,n)
            continue

        player=(player+1)%2

n=int(input("enter the grid value"))
board=[]
for i in range(n):
    l=[]
    board.append(l)
    for j in range(n):
        l.append(' ')
        
tic_tae_toe(board,n)

