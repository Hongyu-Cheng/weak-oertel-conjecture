"""Exact finite certificates for the sharp all-dimensional three-tail theorem."""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json


def add(a,b):
    return [(a[i] if i<len(a) else Q(0))+(b[i] if i<len(b) else Q(0))
            for i in range(max(len(a),len(b)))]


def scale(a,c): return [c*x for x in a]


def mul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def power(a,n):
    out=[Q(1)]
    for _ in range(n):out=mul(out,a)
    return out


def evaluate(a,r):
    out=Q(0)
    for c in reversed(a):out=out*r+c
    return out


CERTIFICATES={
    3:{'basis':'Bernstein','factor':'1/70','coefficients':
       [140,210,330,465,531,450,405,2835,28350]},
    4:{'basis':'Bernstein','factor':'1/9009','coefficients':
       [288288,384384,521664,722304,1015773,1439568,2038392,2860592,
        3950408,5339808,7079232,9518784,14783472,33551232,116468352,521224704]},
    5:{'basis':'Bernstein','factor':'1/178474296','coefficients':
       [89594096592,111992620740,141208087020,179719383480,231067778760,
        300303989622,394621080750,524249216400,703717669200,953628776100,
        1303138575375,1793399858250,2482300507500,3450962926125,4812850428750,
        6727712696250,9427739230000,13281714355000,18987532687500,28208619562500,
        45765058462500,87382082287500,208058350500000,612111062062500,2127748247625000]},
    6:{'basis':'monomial','factor':'1','coefficients':
       [8712,60984,243936,731808,1829520,4024944,7656985,12704407,18695404,
        24737916,29670690,32335086,31587318,27626130,22586067,20396341,
        25905292,43270444,73801371,117665373,171895962,229957278,282864435,
        321859797,339523604,335492948,310913099,269765181,218594358,
        164638530,113891946,73425534,43146348,22397732,9627401,2868335]}
}


def main():
    scalar_checks=0
    for d in range(2,7):
        gamma=Q(d,d+1)**d
        lam=Q(7,9) if d==2 else Q(1)
        U=[Q(d)]*(d+1);W=[Q(d+1)]*d
        front=[1-gamma]+[Q(0)]*(d-1)+[gamma+lam]
        P=add(add(mul(front,power(W,d)),scale(power(U,d),-1)),
              scale(power(add(scale(U,2),scale(W,-1)),d),-lam))
        assert sum(P)==0
        quotient=[];running=Q(0)
        for coefficient in P[:-1]:
            running+=coefficient;quotient.append(running)
        assert mul(quotient,[Q(1),Q(-1)])==P
        if d==2:
            assert quotient==[Q(2,9),Q(2,3),Q(-7,3),Q(49,9)]
            # The numerator derivative is147(r-1/7)^2+3.
            assert [6,-42,147]==[Q(147,49)+3,Q(-294,7),Q(147)]
        else:
            cert=CERTIFICATES[d]
            wanted=[Q(cert['factor'])*x for x in cert['coefficients']]
            n=len(quotient)-1
            bernstein=[sum(quotient[k]*Q(comb(i,k),comb(n,k))for k in range(i+1))
                       for i in range(n+1)]
            actual=bernstein if cert['basis']=='Bernstein' else quotient
            assert actual==wanted
            assert all(x>0 for x in actual)
            assert min(bernstein)=={3:Q(2),4:Q(32),5:Q(502),6:Q(8712)}[d]
        for numerator in range(101):
            r=Q(numerator,101)
            m=Q(d,d+1)*(1-r**(d+1))/(1-r**d)
            p=(m**d-r**d)/(1-r**d)
            t=((2*m-1)**d-r**d)/(1-r**d)
            assert evaluate(P,r)==(1-gamma-p-lam*t)*(1-r**d)*evaluate(W,r)**d
            assert p+lam*t<=1-gamma
            scalar_checks+=1
    gamma7=Q(7,8)**7
    assert Q(1,2)-gamma7-Q(2,3)*gamma7**2==Q(29669536175,6597069766656)>0
    for d in range(7,101):
        gamma=Q(d,d+1)**d
        assert gamma<=gamma7
        assert Q(1,2)+Q(2,3)*gamma**2<1-gamma
        assert 4*gamma**2<=gamma/(1-gamma)
    a=Q(2,3);v=Q(3,4);shift=v-a;lam=Q(7,9);gamma=Q(4,9)
    assert shift==Q(1,12)
    assert gamma+(a-shift)**2+lam*(a+shift)**2==gamma+lam
    subset=1-v*v
    assert subset==Q(7,16)
    assert gamma+lam*subset==Q(113,144)
    Path(__file__).with_name('sharp_weighted_three_tails_bernstein_certificates.json').write_text(
        json.dumps(CERTIFICATES,indent=2)+'\n')
    print(f"PASS: all displayed exact coefficient vectors; {scalar_checks} rational frustum identities; "
          "large-dimensional rational bound and actual simplex/subset equality.")


if __name__=='__main__':main()
