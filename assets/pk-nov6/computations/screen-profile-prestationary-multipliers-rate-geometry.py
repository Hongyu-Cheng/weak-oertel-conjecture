"""Discovery only. Common coarea plus section-moment scalar certificate."""
import math, random, json
import numpy as np

def hull(points):
    out=[]
    for p in points:
        while len(out)>1 and (out[-1][1]-out[-2][1])*(p[0]-out[-1][0]) <= (p[1]-out[-1][1])*(out[-1][0]-out[-2][0]):out.pop()
        out.append(p)
    return out

def coeffs(h):
    return [(z,t,(v*t-w*z)/(t-z),(w-v)/(t-z)) for (z,v),(t,w) in zip(h,h[1:])]

def integ(A,B,k,l,r):
    a=A+B*l;b=A+B*r
    return (r-l)*sum(a**(k-j)*b**j for j in range(k+1))/(k+1)

def zinteg(A,B,k,l,r):
    a=A+B*l;b=A+B*r
    return l*integ(A,B,k,l,r)+(r-l)**2*sum((j+1)*a**(k-j)*b**j for j in range(k+1))/((k+1)*(k+2))

def data(h,s,m):
    V=P=C=M=0.
    for lo,hi,A,B in coeffs(h):
        V+=integ(A,B,m,lo,hi)
        if s==0:
            if hi>0:P+=integ(A,B,m,max(0,lo),hi)
            if lo<=0<hi:C=A**m
            continue
        cuts=[lo,hi]
        for sign in [-1,1]:
            den=sign-s*B
            if den:
                z=s*A/den
                if lo<z<hi:cuts.append(z)
        cuts=sorted(cuts)
        for l,r in zip(cuts,cuts[1:]):
            z=(l+r)/2;R=A+B*z
            if z>s*R:P+=integ(A,B,m,l,r);continue
            if z<-s*R:continue
            P+=(integ(A,B,m,l,r)+zinteg(A,B,m-1,l,r)/s)/2
            C+=integ(A,B,m-1,l,r)/(2*s)
            M+=zinteg(A,B,m-1,l,r)/(2*s)
    return P/V,C/V,M/V

def run():
    rng=random.Random(7371323)
    slopes=[0.]+[10**(-3+i/12) for i in range(85)]
    for m in [1,2,3,4,6]:
      for trial in range(3000):
        A=rng.randint(1,8);B=rng.randint(1,8)
        h=hull([(float(z),float(rng.randint(1,20))) for z in range(-A,B+1)])
        ds=np.array([data(h,s,m) for s in slopes])
        p,C,M=ds.T;mu=M/C
        g=4/9
        low=(p-(1-g))/C;up=(p-g)/C
        dif=mu[:,None]-mu[None,:];rhs=low[:,None]-up[None,:]
        pos=dif>1e-8;neg=dif<-1e-8
        lower=np.max(np.where(pos,rhs/np.where(pos,dif,1),-np.inf))
        upper=np.min(np.where(neg,rhs/np.where(neg,dif,1),np.inf))
        if lower>upper+1e-5 or np.any((abs(dif)<=1e-8)&(rhs>1e-5)):
          il=np.unravel_index(np.argmax(np.where(pos,rhs/np.where(pos,dif,1),-np.inf)),dif.shape)
          iu=np.unravel_index(np.argmin(np.where(neg,rhs/np.where(neg,dif,1),np.inf)),dif.shape)
          result={'m':m,'trial':trial,'profile':h,'lower':lower,'upper':upper,'lowpair':[(slopes[k],list(ds[k])) for k in il],'uppair':[(slopes[k],list(ds[k])) for k in iu]}
          print('CANDIDATE ONLY',result,flush=True)
          with open('./profile-prestationary-multiplier-candidate-rate-geometry.json','w') as f:json.dump(result,f,indent=2)
          return
      print('completed m',m,flush=True)
if __name__=='__main__':run()
