'''x = int(input())
y = int(input())

if (x < 6 and x  > 0) or (y < 6 and y > 0):
    print('NO')
elif (x >= 18 and x < 120 ) or (y >= 18 and y < 120):
    print('YES')
elif (x >= 14 and x < 120 ) and (y >= 14 and y < 120 ):
    print('YES')
'''


x = int(input())
y = int(input())
if x < 6 or y < 6:
    print('NO')
elif x >= 14 or y >= 14:
    print('YES')
elif x > 18 or y > 18:
    print('YES')
   
