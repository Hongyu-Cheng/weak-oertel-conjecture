exec(open('./screen_simplex_chain_positive_normal.py').read().split('best=None')[0])
for trial in range(300):
    N=3
    rs=np.array([random.randint(1,20)/4 for _ in range(3)])
    if 2*rs[1]<rs[0]+rs[2]:continue
    j=1
    opt=differential_evolution(lambda v:obj(v,rs,j),[(.5,1.),(-4*max(rs),4*max(rs))],tol=1e-10,popsize=12,seed=trial,polish=True)
    if .501<opt.x[0]<.999:
        ends=[]
        for a in [.5,1.]:
            e=differential_evolution(lambda b:obj([a,b[0]],rs,j),[(-4*max(rs),4*max(rs))],tol=1e-10,popsize=15,seed=trial)
            ends.append(e.fun)
        if min(ends)-opt.fun>1e-5:
            print('COUNTER',rs.tolist(),opt.x.tolist(),opt.fun,ends,flush=True);break
else:print('none')
