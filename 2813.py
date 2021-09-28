x = int(input())
casa_comp = 0
casa_sob = 0
trab_comp = 0
trab_sob = 0
for i in range(x):
    sd, sn = input().split()
    if (sd == "chuva" and casa_sob == 0):
        casa_comp += 1
        trab_sob += 1
    elif (sd== "chuva" and casa_sob > 0):
        trab_sob += 1
        casa_sob -= 1
            
    if (sn == "chuva" and trab_sob == 0):
        trab_comp += 1
        casa_sob += 1
    elif (sn == "chuva" and trab_sob > 0): 
        casa_sob += 1
        trab_sob -= 1

print(casa_comp, trab_comp)
        
