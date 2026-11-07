"""Discovery only: stationary reflected pairs in square homothetic profiles."""
import math, random, json

def hull(points):
    out=[]
    for p in points:
        while len(out)>1 and (out[-1][1]-out[-2][1])*(p[0]-out[-1][0]) <= (p[1]-out[-1][1])*(out[-1][0]-out[-2][0]):
            out.pop()
        out.append(p)
    return out

def coeffs(h):
    return [(z,t,(v*t-w*z)/(t-z),(w-v)/(t-z)) for (z,v),(t,w) in zip(h,h[1:])]

def polyint(c,l,r):
    return sum(v*(r**(i+1)-l**(i+1))/(i+1) for i,v in enumerate(c))

def data(h,a,kind):
    V=Q=S=Z=0.
    for lo,hi,A,B in coeffs(h):
        cuts=[lo,hi]
        if lo<0<hi:cuts.append(0.)
        k=1 if kind==0 else 2
        for sign in [-1,1]:
            den=sign-k*a*B
            if den:
                z=k*a*A/den
                if lo<z<hi:cuts.append(z)
        cuts=sorted(cuts)
        for l,r in zip(cuts,cuts[1:]):
            z=(l+r)/2;R=A+B*z
            r2=[A*A,2*A*B,B*B]
            vol=4*polyint(r2,l,r);V+=vol
            if z>k*a*R:Q+=vol;continue
            if z<-k*a*R:continue
            if kind==0:
                section=[2*A/a,2*B/a]
                capture=[2*A*A,4*A*B+2*A/a,2*B*B+2*B/a]
            else:
                sgn=1 if z>=0 else -1
                section=[2*A/a,2*B/a-sgn/a**2]
                T=2*B-sgn/a
                tail=[2*A*A,2*A*T,T*T/2]
                capture=[4*r2[i]-tail[i] for i in range(3)] if sgn==1 else tail
            Q+=polyint(capture,l,r)
            S+=polyint(section,l,r)
            Z+=polyint([0]+section,l,r)
    return Q/V,S/V,Z

def stationary(h,kind):
    samples=[10**(-3+i/16) for i in range(113)]
    out=[]
    last=samples[0];f=data(h,last,kind)[2]
    for t in samples[1:]:
        g=data(h,t,kind)[2]
        if f*g<0:
            l,r=last,t;fl=f
            for _ in range(50):
                mid=(l+r)/2;fm=data(h,mid,kind)[2]
                if fl*fm<=0:r=mid
                else:l=mid;fl=fm
            a=(l+r)/2;p,C,Z=data(h,a,kind)
            if not out or abs(a-out[-1][1])>1e-5:out.append((kind,a,p,C))
        last=t;f=g
    return out

def run():
    rng=random.Random(823173)
    best=1.
    for trial in range(12000):
        A=rng.randint(1,8);B=rng.randint(1,8)
        h=hull([(float(z),float(rng.randint(1,20))) for z in range(-A,B+1)])
        seg=coeffs(h);V=4*sum(polyint([c*c,2*c*b,b*b],l,r) for l,r,c,b in seg)
        Q0=4*sum(polyint([c*c,2*c*b,b*b],max(l,0),r) for l,r,c,b in seg if r>0)
        R0=next(c for l,r,c,b in seg if l<=0<=r)
        caps=[(-1,0.,Q0/V,4*R0*R0/V)]+stationary(h,0)+stationary(h,1)
        for a in caps:
            for b in caps:
                value=(b[3]*a[2]+a[3]*(1-b[2]))/(a[3]+b[3])
                if value<best:
                    best=value
                    print(trial,'best',value,'profile',h,'caps',a,b,flush=True)
                if value<4/9-1e-7:
                    with open('./square-profile-stationary-pair-candidate-rate-geometry.json','w') as f:
                        json.dump({'profile':h,'caps':[a,b],'value':value},f,indent=2)
                    print('NUMERICAL CANDIDATE ONLY',flush=True)
                    return

if __name__=='__main__':run()
