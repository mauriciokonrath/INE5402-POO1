x = int(input())
for i in range(x):
    led = 0
    n = input()
    for i in range (0, len(n)):
        if n[i] == '1':
            led += 2
        elif n[i] == '2':
            led += 5
        elif n[i] == '3':
            led += 5
        elif n[i] == '4':
            led += 4
        elif n[i] == '5':
            led += 5
        elif n[i] == '6':
            led += 6
        elif n[i] == '7':
            led += 3
        elif n[i] == '8':
            led += 7
        elif n[i] == '9':
            led += 6
        elif n[i] == '0':
            led += 6
    
    print("{} leds".format(led))
