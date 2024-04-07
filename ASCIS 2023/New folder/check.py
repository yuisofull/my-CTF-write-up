nbits = 128
def a1(a,b,r0,r1,trun,m):
    T=(trun*r1-a*trun*r0-b+trun-1)%m
    for K in range(((trun-1)*(a+1)-T)//m):
        if((T+m*K)%a)<trun:
            x=(T+m*K)//a+trun*r0
            x=(a*x+b)%m
            x=(a*x+b)%m
            x=x>>(nbits-18)
            
            print(x)
            if x== 130745:
                print((T+m*K)//a+trun*r0)
a = 43787291635671214792919526096167649451
c = 156497500579206068939331641182566791023
m = 273364800599018888270443304662600024273
r0,r1={167323, 194700}
trun=pow(2,110)
a1(a,c,r0,r1,trun,m)