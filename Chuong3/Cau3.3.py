a=int(input("Tien thu="))
b=0
if 1<a<100:
    b=550
if 101<a<150:
    b=750
if 151<a<200:
    b=950
if a>201:
    b=1350
c=a*b+0.1*b
print("Phai tra=",c)