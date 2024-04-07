p=9739

P = (493, 5564)
Q = (1539, 4742)
R = (4403,5202)
a=497
b=1768

def addPoint(P,Q):
    lam=0
    if P==Q:
        lam=((3*pow(P[0],2)+a)/(2*P[1]))%p
    else:
        lam=((Q[1]-P[1])/(Q[0]-P[0]))%p
    R=[0,0]
    x=lam*lam - P[0]-Q[0]
    R[0]=int(x%p)
    
    y=lam*(P[0]-x)-P[1]
    R[1]=int(y%p)
    return R

print(addPoint(R,addPoint(Q,addPoint(P, P))))