from math import sqrt

R = 2
S = 5
T = -1
X = 3
Y = 1
Z = 0

A = (R >= 5) or (T > Z) and (X - Y + R > 3 * Z)
B = T + 3 >= 4 and not(3 * R / 2 < S * 3)
C = X == 2 or Y == 1 and ((Z == 0) or (R > 3)) and S < 10
D = (R != S) or not(sqrt(R) < sqrt(X)) and (4327 * X * S * Z == 0)

if A == True:
    print("A=True")
else:
    print("A=False")
    
if B == True:
    print("B=True")
else:
    print("B=False")
    
if C == True:
    print("C=True")
else:
    print("C=False")

if D == True:
    print("D=True")
else:
    print("D=False")