print("Disegna un albero di natale!\n")

h=int(input("Inserire in l'altezza dell'albero: "))
nspace=h
line=1
linprec=0

while line<=h:
    print(str(nspace*" ")+str((line+linprec)*"*"))
    linprec=line
    nspace=nspace-1
    line=line+1
    
    
