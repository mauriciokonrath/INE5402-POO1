while True:
    try:
        a = int(input())

        for h in range(a):
            x = input()
            x = x.replace(" ","")

            s = ""

            for i in x:
                if i in 'GQaku':
                    s += '0'
                elif i in 'ISblv':
                    s += '1'
                elif i in 'EOYcmw':
                    s += '2'
                elif i in 'FPZdnx':
                    s += '3'
                elif i in 'JYeoy':
                    s += '4'
                elif i in 'DNXfpz':
                    s += '5'
                elif i in 'AKUgq':
                    s += '6'
                elif i in 'CMWhr':
                    s += '7'
                elif i in 'BLVis':
                    s += '8'
                elif i in 'HRjt':
                    s += '9'

            print(s[:12])
    except EOFError:
        break
