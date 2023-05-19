import numpy as np
import matplotlib.pyplot as plt


print('Введите число K: ')
k = int(input())
print('Введите число N: ')
n = int(input())
A = []
crutch = []
c = 0
s1 = 0
s2 = 1
print('Введите строку чисел для заполнения матрицы: ')
# На вход подается строка из чисел, разделенных пробелами. Количество чисел в строке должно быть n*n
nums = list(map(int,input().split()))
for i in nums:
    crutch.append(i)
    if len(crutch) == n:
        A.append(crutch)
        crutch = []
crutch = []
E,B,D,C = [],[],[],[]
print('Сгенерированная матрица A\n',np.array(A))
if n % 2 == 0:
    for i in range (n):
        for j in range (n):
            if (j <= n/2-1)and(i <= n/2-1):
                crutch.append(A[i][j])
                if len(crutch) == n/2:
                    E.append(crutch)
                    crutch = []
            if (j > n/2-1)and(i <= n/2-1):
                crutch.append(A[i][j])
                if len(crutch) == n/2:
                    B.append(crutch)
                    crutch = []
            if (j <= n/2-1)and(i > n/2-1):
                crutch.append(A[i][j])
                if len(crutch) == n/2:
                    D.append(crutch)
                    crutch = []
            if (j > n/2-1)and(i > n/2-1):
                crutch.append(A[i][j])
                if len(crutch) == n/2:
                    C.append(crutch)
                    crutch = []
else:
    for i in range (n):
        for j in range (n):
            if (j<=n//2-1) and (j != n//2) and (i <=n//2-1) and (i != n//2):
                crutch.append(A[i][j])
                if len(crutch) == n//2:
                    E.append(crutch)
                    crutch = []
            if (j>n//2-1) and (j != n//2) and (i <=n//2-1) and (i != n//2):
                crutch.append(A[i][j])
                if len(crutch) == n//2:
                    B.append(crutch)
                    crutch = []
            if (j<=n//2-1) and (j != n//2) and (i > n//2-1) and (i != n//2):
                crutch.append(A[i][j])
                if len(crutch) == n//2:
                    D.append(crutch)
                    crutch = []
            if (j>n//2-1) and (j != n//2) and (i > n//2-1) and (i != n//2):
                crutch.append(A[i][j])
                if len(crutch) == n//2:
                    C.append(crutch)
                    crutch = []
print('Матрица E\n', np.array(E))
print('Матрица B\n', np.array(B))
print('Матрица D\n', np.array(D))
print('Матрица C\n', np.array(C))
F = np.copy(np.array(A))
for i in range(len(C)):
    for j in range(len(C)):
        if j % 2 == 1:
            s1 += C[i][j]
        if i % 2 == 0:
            s2 *= C[i][j]
if n%2 == 0:
    if s1 > s2:
        for i in range(len(B)):
            for j in range(len(B),len(F)):
                c = F[i][j]
                F[i][j] = int(F[-(i+1)][j])
                F[-(i+1)][j] = c
    else:
        for i in range(len(E)):
            for j in range(len(E)):
                c = F[i][j]
                F[i][j] = F[i][j+len(E)]
                F[i][j+len(E)] = c
else:
    if s1 > s2:
        for i in range(len(B)):
            for j in range(len(B)+1,len(F)):
                c = F[i][j]
                F[i][j] = int(F[-(i+1)][j])
                F[-(i+1)][j] = c
    else:
        for i in range(len(E)):
            for j in range(len(E)):
                c = F[i][j]
                F[i][j] = F[i][j+len(E)+1]
                F[i][j+len(E)+1] = c
print('Сгенерированная матрица F после преобразований\n',F)
print('Определитель A: ', np.linalg.det(np.array(A)))
print('Сумма диагональных элементов F: ',np.trace(F))
if np.linalg.det(np.array(A)) > np.trace(F):
    print(np.dot((np.linalg.inv(np.array(A))),np.transpose(np.array(A))) - k * np.linalg.inv(F))
else:
    print((np.transpose(np.array(A))+np.linalg.inv(np.triu(np.array(A))-np.linalg.inv(F)))*k)

figure1 = plt.figure()
ax1 = figure1.add_subplot(2,2,1)
ax2 = figure1.add_subplot(2,2,2)
ax3 = figure1.add_subplot(2,2,3)
ax1.plot(F[0],F[1],color='red',marker='o')
ax1.set_xlabel('F[0]')
ax1.set_ylabel('F[1]')
ax2.plot(E[0],C[0],color='blue',linestyle='',marker='.')
ax2.plot(E[0],B[0],color='orange',linestyle='',marker='.')
ax2.plot(E[0],D[0],color='red',linestyle='',marker='.')
ax2.set_xlabel('С[0],B[0],D[0]')
ax2.set_ylabel('E[0]')
ax3.plot(A[0],F[0],marker='.')
ax3.plot(A[n-1],F[n-1],color='red',marker='.')
ax3.set_xlabel('A')
ax3.set_ylabel('F')
plt.show()






