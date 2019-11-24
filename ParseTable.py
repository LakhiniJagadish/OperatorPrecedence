print(" ")
print("HERE IS OPERATOR PRECEDENCE TABLE")
print(" ")
import numpy as np

p1 = 'id'
p2 = '*'
p3 = '+'
p4 = '$'

x = np.array([["  " for i in range(6)] for j in range(6)])
a = ['id', '*', '+', '$']

for i in range(0, 4):
    for j in range(0, 4):

        if (a[i] == p1):
            pi = 1
        elif (a[i] == p2):
            pi = 2
        elif (a[i] == p3):
            pi = 3
        elif (a[i] == p4):
            pi = 4
        if (a[j] == p1):
            pj = 1
        elif (a[j]  == p2):
            pj = 2
        elif (a[j] == p3):
            pj = 3
        elif (a[j] == p4):
            pj = 4
        if (pi < pj):
            x[i][j] = '>'
        elif(pi == pj) and ((a[i] == p2) or (a[i] == p3))  :
            x[i][j] = '>'
        elif(pi == pj):
            x[i][j] = '-'
        else:
            x[i][j] = '<'


print("\t", end='')
for i in range(0, 4):
    print(a[i] + "\t", end='')
print('')
for i in range(0, 4):
    print("\n")
    print(a[i] + "\t", end='')
    for j in range(0, 4):
        print(x[i][j] + "\t", end='')
    print('')
