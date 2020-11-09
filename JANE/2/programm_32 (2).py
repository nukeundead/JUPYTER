def suma(x):
    suma_digit=0
    while x>0:
        digit=x%10
        suma_digit+=digit
        x=x//10
    return suma_digit
def insertion_sort(A):
    for i in range(1,len(A)):
        for j in range(i,0,-1):
            if suma(A[j-1])>suma(A[j]):
                A[j-1],A[j]=A[j],A[j-1]
                    
N=int(input())
if N>0:
    S=[0]*N
    for i in range(N):
        S[i]=abs(int(input()))
y=insertion_sort(S)
for i in S:
    print(i)
