while True:
    try:
        x = int(input())
        epr = 0
        ehd = 0
        intruso = 0
        for i in range(x):
            mat, curso = input().split()
            if curso == 'EHD':
                ehd += 1
            elif curso == 'EPR':
                epr += 1
            else:
                intruso += 1
        
        print('EPR: {}'.format(epr))
        print('EHD: {}'.format(ehd))
        print('INTRUSOS: {}'.format(intruso))
        
    except EOFError:
        b