# -*- coding: utf -8 -*
n1,n2,n3,n4=input().split()

n1=float(n1)
n2=float(n2)
n3=float(n3)
n4=float(n4)

media=((n1*2)+(n2*3)+(n3*4)+(n4*1))/10

print("Media: {:.1f}".format(media))
if(media < 5):
    #print("Media: {:.1f}".format(media))
    print("Aluno reprovado.")
elif(media >= 7):
    #print("Media: {:.1f}".format(media))
    print("Aluno aprovado.")

elif(media >= 5 and media <= 6.9):
    #print("Media {:.1f}".format(media))
    print("Aluno em exame.")
    
    exame=float(input())
    mf=(media+exame)/2
    
    if(mf>=5):
        print("Nota do exame: {:.1f}".format(exame))
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(mf))
    else:
        print("Nota do exame: {:.1f}".format(exame))
        print("Aluno reprovado.")
        print("Media final: {:.1f}".format(mf))


