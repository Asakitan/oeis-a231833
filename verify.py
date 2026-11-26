"""Direct polynomial determinant and numerator certificate for A231833."""
from itertools import permutations

states=[(i,0) for i in range(4)]+[(i,1) for i in range(3)]
M=[[0]*7 for _ in states]
for i,(v,d) in enumerate(states):
    for w in range(4):
        if not (d and w>v):
            M[i][states.index((w,int(v>w)))]+=1
S=[[sum(M[i][k]*M[k][j] for k in range(7)) for j in range(7)] for i in range(7)]

def determinant():
    polynomial=[0]*8
    for p in permutations(range(7)):
        sign=(-1)**sum(p[i]>p[j] for i in range(7) for j in range(i+1,7))
        term=[sign]
        for i,j in enumerate(p):
            a,b=int(i==j),-S[i][j]
            term=[a*u+b*v for u,v in zip(term+[0],[0]+term)]
        polynomial=[x+y for x,y in zip(polynomial,term)]
    return polynomial

if __name__=='__main__':
    den=determinant()
    assert den==[1,-4,-34,-86,-91,-46,-11,-1],den
    b=[1,1,1,1,3,2,1]
    a=[0]
    for n in range(1,8):
        a.append(sum(b[:4]))
        b=[sum(b[i]*S[i][j] for i in range(7)) for j in range(7)]
    num=[sum(den[j]*a[n-j] for j in range(n+1)) for n in range(8)]
    assert num==[0,4,34,86,91,46,11,1],num
    print("det(I-x M^2) and numerator passed; direct matrix counts:",a[1:])
