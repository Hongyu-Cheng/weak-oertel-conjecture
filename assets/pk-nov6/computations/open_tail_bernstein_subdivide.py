exec(open('./open_tail_dual_bernstein.py').read().split('for N0 in')[0])
aa=(L-1+(L+2)*t)/3;jj=1+(aa-1)*u
base=S.expand(P.subs(j,jj).subs(a,aa).subs(L,11+x))
leaves=[];fails=[]
def recurse(t0,t1,u0,u1,depth):
 e=S.expand(base.subs({t:t0+(t1-t0)*t,u:u0+(u1-u0)*u},simultaneous=True))
 minimum,neg,degs=bern(e)
 if not neg:
  leaves.append((t0,t1,u0,u1,minimum[0]));return
 if depth==8:fails.append((t0,t1,u0,u1,minimum));return
 if depth%2==0:
  mid=(t0+t1)/2;recurse(t0,mid,u0,u1,depth+1);recurse(mid,t1,u0,u1,depth+1)
 else:
  mid=(u0+u1)/2;recurse(t0,t1,u0,mid,depth+1);recurse(t0,t1,mid,u1,depth+1)
recurse(S.Rational(0),S.Rational(1),S.Rational(0),S.Rational(1),0)
print('leaves',len(leaves));print(leaves);print('fails',len(fails),fails)
