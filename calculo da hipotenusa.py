import math
co = float(input('digite o comprimento do cateto oposto:'))
ca = float(input('digite é o comprimento do cateto adjacente:'))
hi = math.hypot(co,ca)
print('o valor da hipotenusa é:{:.2f}'.format(hi))
