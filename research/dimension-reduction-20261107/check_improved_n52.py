#!/usr/bin/env python3
"""Exact parameter improvement for the existing 52-integer-variable body."""
from fractions import Fraction as F
from math import comb,factorial
from pathlib import Path
import json


def power_interval(a, exponent, digits=50):
    scale=10**digits
    lo=a.numerator*scale//a.denominator
    hi=-((-a.numerator*scale)//a.denominator)
    lower=upper=scale
    original_exponent=exponent
    while exponent:
        if exponent&1:
            lower=lower*lo//scale
            upper=-((-upper*hi)//scale)
        exponent//=2
        if exponent:
            lo=lo*lo//scale
            hi=-((-hi*hi)//scale)
    assert original_exponent>=0 and a>0
    return F(lower,scale),F(upper,scale)


def main():
    n,N,h,ell=52,13,2747786,1350000000000000000
    theta,beta=F(3,32),F(27,64)
    s,t,eta=F(500000001,10**9),F(999999997,10**9),F(399999999,400000000)
    eps,q=F(1,10**12),F(1000001,2000000)
    ds,dt,dq=2*s-1,1-t,2*q-1
    assert 0<eps<F(1,4) and F(1,2)<s<1 and F(1,2)<q<1
    assert 0<t<eta<2*(1-s) and N*dt<1 and N*dq<1
    assert N*(ds+4*eps*(3*t+1-ds))<1
    m_int=tuple(theta*(2*s)**3*x for x in power_interval(2*q,h))
    elo=ehi=F(0)
    powers=[]
    for r in range(1,N+1):
        tr,ur=1-r*dt,1-r*dq
        assert tr>0 and ur>0
        lo,hi=power_interval(ur,h)
        factor=4*comb(N,r)*theta*tr**3
        elo+=factor*lo;ehi+=factor*hi
        powers.append({'r':r,'base':str(ur),'interval':[str(lo),str(hi)]})
    mlo,mhi=F(1463251505373,10**12),F(1463251505374,10**12)
    Elo,Ehi=F(465699293757,10**12),F(465699293758,10**12)
    assert mlo<m_int[0]<=m_int[1]<mhi
    assert Elo<elo<=ehi<Ehi
    e_upper=F(1359141,500000)
    series_upper=sum((F(1,factorial(i)) for i in range(9)),F(0))+F(10,9*factorial(9))
    assert series_upper<e_upper
    margins={
        'middle_cut':mlo/e_upper-beta-Ehi/4,
        'mass_surplus':1+Elo-mhi,
        'padding':1+Elo-mhi-2**n*mhi/(2*ell-1),
        'outer_mass_below_maximum':mlo-theta,
        'negative_free_scale':1-N*dq,
        'paid_origin_facet':1-N*(ds+4*eps*(3*t+1-ds)),
    }
    assert all(x>0 for x in margins.values())
    original_d=274784+2**61
    report={
        'status':'PASS_EXACT_RATIONAL_PARAMETER_IMPROVEMENT',
        'n':n,'d':str(3+h+ell),'h':h,'ell':str(ell),
        'parameters':{k:str(v) for k,v in {'s':s,'t':t,'eta':eta,'epsilon':eps,'q':q,'theta':theta,'beta':beta}.items()},
        'm_enclosure':[str(mlo),str(mhi)],'E_enclosure':[str(Elo),str(Ehi)],
        'margins':{k:str(v) for k,v in margins.items()},
        'margins_decimal_for_orientation_only':{k:float(v) for k,v in margins.items()},
        'power_intervals':powers,
        'dimension_reduction_fraction':str(F(original_d-(3+h+ell),original_d)),
        'scope':'Same fully proved geometric lemma as df488edae05a1702, with new exact parameters. Counterexample to 1/(e*2^52); not Lean-formalized and still far above dimension 100.'
    }
    path=Path(__file__).with_name('improved-n52-certificate.json')
    path.write_text(json.dumps(report,indent=2)+'\n')
    print(report['status'])
    print('n =',n,'d =',3+h+ell)
    print(json.dumps(report['margins_decimal_for_orientation_only'],indent=2))
    print('Saved',path.name)


if __name__=='__main__':main()
