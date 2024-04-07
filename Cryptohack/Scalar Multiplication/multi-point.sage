p=9739
a=497
b=1768
def addPoint(P,Q):
    if P==0:
        return Q
    if Q==0: 
        return P

    if P==Q:
        lam=((3*pow(P[0],2)+a)*pow(2*P[1],-1,p))%p
    else:
        lam=((Q[1]-P[1])*pow(Q[0]-P[0],-1,p))%p
    R=[0,0]
    x=lam*lam - P[0]-Q[0]
    R[0]=x%p
    
    y=lam*(P[0]-x)-P[1]
    R[1]=y%p
    return R


def mul(P, n):
    Q=P
    R=0
    while n>0:
        if n%2==1:
            R=addPoint(R,Q)
        Q=addPoint(Q,Q)
        n=n//2
    return R

P = (2339, 2213)

print(mul(P, 7863))
