"""Generates the Matplotlib figures in assets/figures/ (Midnight Lavender palette).
Run from the repository root:  python scripts/make_figures.py
Figures marked 'schematic' are illustrative redrawings of the hand sketches, not computed from real data."""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG='#171821'; BG2='#222332'; CARD='#2C2B40'; A='#A78BFA'; B='#E89BB5'; M='#EAC477'; S='#91C7A5'; T='#F1EFF7'; T2='#AAA9BB'
plt.rcParams.update({'figure.facecolor':BG,'axes.facecolor':BG2,'savefig.facecolor':BG,'axes.edgecolor':T2,
 'axes.labelcolor':T,'text.color':T,'xtick.color':T2,'ytick.color':T2,'axes.titlecolor':T,'font.size':11,
 'legend.facecolor':CARD,'legend.edgecolor':CARD,'axes.spines.top':False,'axes.spines.right':False})
OUT='assets/figures/'
def save(fig,name):
    fig.savefig(OUT+name+'.png',dpi=150,bbox_inches='tight'); plt.close(fig)
def arrow(ax,p,q,c=T2,style='->'):
    ax.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle=style,color=c,lw=1.6))
def note(fig,t): fig.text(.5,-.04,t,ha='center',color=T2,fontsize=9)

# 1 entropy
p=np.linspace(1e-6,1-1e-6,500); H=-p*np.log2(p)-(1-p)*np.log2(1-p)
fig,ax=plt.subplots(figsize=(6,3.8)); ax.plot(p,H,color=A,lw=3,label='$H(p_1)$')
ax.scatter([.5],[1],color=M,s=70,zorder=5); ax.annotate('maximum at 50-50\n$p_1=0.5,\\ H=1$',(.5,1),(.64,.55),color=M,arrowprops=dict(arrowstyle='->',color=M))
ax.set_xlabel('$p_1$ = fraction of examples that are cats'); ax.set_ylabel('$H(p_1)$'); ax.set_ylim(0,1.12); ax.legend(loc='lower center')
save(fig,'entropy-curve')

# 2 log loss
f=np.linspace(.005,.995,400); fig,ax=plt.subplots(figsize=(6,3.8))
ax.plot(f,-np.log(f),color=A,lw=3,label='$y=1$:  $-\\log(f)$'); ax.plot(f,-np.log(1-f),color=B,lw=3,label='$y=0$:  $-\\log(1-f)$')
ax.set_ylim(0,5); ax.set_xlabel('$f_{\\vec w,b}(\\vec x)$'); ax.set_ylabel('loss $L$'); ax.legend()
save(fig,'log-loss')

# 3 decision boundaries
rng=np.random.default_rng(3); fig,(a1,a2)=plt.subplots(1,2,figsize=(10,4.2))
P=rng.uniform(0,3.8,(90,2)); P=P[abs(P.sum(1)-3)>.45]; s=P.sum(1)
a1.scatter(*P[s<3].T,facecolors='none',edgecolors=S,s=45); a1.scatter(*P[s>3].T,marker='x',color=B,s=45)
a1.plot([0,3],[3,0],color=M,lw=2.5); a1.text(2.3,1.2,'$x_1+x_2=3$',color=M); a1.set_xlim(0,3.8); a1.set_ylim(0,3.8)
a1.set_xlabel('$x_1$'); a1.set_ylabel('$x_2$'); a1.set_title('Linear boundary: $z=x_1+x_2-3=0$')
Q=rng.uniform(-2,2,(160,2)); r=np.hypot(*Q.T); Q=Q[abs(r-1)>.25]; r=np.hypot(*Q.T)
a2.scatter(*Q[r<1].T,facecolors='none',edgecolors=S,s=45); a2.scatter(*Q[r>1].T,marker='x',color=B,s=45)
a2.add_patch(plt.Circle((0,0),1,fill=False,ec=M,lw=2.5)); a2.set_aspect('equal'); a2.set_xlabel('$x_1$'); a2.set_ylabel('$x_2$')
a2.set_title('Non-linear boundary: $z=x_1^2+x_2^2-1=0$')
save(fig,'decision-boundaries')

# 4 convex vs non-convex (schematic)
w=np.linspace(-2,2,500); fig,(a1,a2)=plt.subplots(1,2,figsize=(10,3.6))
a1.plot(w,w**2,color=S,lw=3); a1.set_title('Linear regression + squared error: convex'); a2.plot(w,.6*w**2+.35*np.sin(8*w)+.15*np.sin(21*w),color=B,lw=3)
a2.set_title('Logistic regression + squared error: non-convex')
for a in (a1,a2): a.set_xlabel('$w,\\ b$'); a.set_ylabel('$J(w,b)$'); a.set_xticks([]); a.set_yticks([])
note(fig,'Schematic redrawing of the sketch on source p. 3 (not computed from data)')
save(fig,'mse-convex-vs-nonconvex')

# 5 underfit / generalised / overfit
rng=np.random.default_rng(1); x=np.linspace(0,1,10); y=np.sin(2.4*x)+rng.normal(0,.12,10); xs=np.linspace(0,1,300)
fig,axs=plt.subplots(1,3,figsize=(13,3.6),sharey=True)
for ax,d,t,c in zip(axs,(1,2,9),('Underfit (high bias)','Generalised (ideal)','Overfit (high variance)'),(B,S,M)):
    ax.scatter(x,y,marker='x',color=T,s=45); ax.plot(xs,np.polyval(np.polyfit(x,y,d),xs),color=c,lw=3); ax.set_title(t); ax.set_ylim(-.3,1.5); ax.set_xticks([]); ax.set_yticks([])
note(fig,'Illustrative: the same 10 noisy points fitted with polynomial degree 1, 2 and 9')
save(fig,'underfit-generalised-overfit')

# 6 regularisation effect (ridge on degree-8 polynomial)
rng=np.random.default_rng(5); x=np.linspace(0,1,12); y=np.sin(2.4*x)+rng.normal(0,.12,12)
def fit(lam,deg=10):
    X=np.vander(x,deg+1,increasing=True)[:,1:]; mu=X.mean(0); sd=X.std(0); Z=(X-mu)/sd
    wv=np.linalg.lstsq(Z,y-y.mean(),rcond=None)[0] if lam==0 else np.linalg.solve(Z.T@Z+lam*len(x)*np.eye(deg),Z.T@(y-y.mean()))
    return lambda q:((np.vander(q,deg+1,increasing=True)[:,1:]-mu)/sd)@wv+y.mean()
fig,(a1,a2)=plt.subplots(1,2,figsize=(10,3.8),sharey=True)
for ax,lam,t,c in ((a1,0,'No regularisation ($\\lambda=0$): overfit',M),(a2,.05,'With regularisation ($\\lambda>0$): smoother',S)):
    ax.scatter(x,y,marker='x',color=T,s=45); ax.plot(xs,fit(lam)(xs),color=c,lw=3); ax.set_title(t); ax.set_ylim(-.5,1.6); ax.set_xticks([]); ax.set_yticks([])
note(fig,'Illustrative: degree-10 polynomial on 12 noisy points; $\\lambda$ penalises large $w_j$')
save(fig,'regularization-effect')

# 7 gradient descent step size
fig,(a1,a2)=plt.subplots(1,2,figsize=(10,3.8),sharey=True); ww=np.linspace(-.5,6.5,200)
for ax,al,t,c in ((a1,.05,'Small $\\alpha$: small steps',S),(a2,.9,'Large $\\alpha$: big steps (overshoot)',B)):
    ax.plot(ww,(ww-3)**2+1,color=T2,lw=2); wv=[0.]
    for _ in range(9 if al<.5 else 8): wv.append(wv[-1]-al*2*(wv[-1]-3))
    wv=np.array(wv); ax.plot(wv,(wv-3)**2+1,'o-',color=c,lw=1.5); ax.set_title(t); ax.set_xlabel('$w$'); ax.set_xticks([]); ax.set_yticks([])
a1.set_ylabel('$J(w)$'); note(fig,'Illustrative one-parameter cost $J(w)=(w-3)^2+1$')
save(fig,'gradient-descent-step-size')

# 8 convergence
it=np.arange(0,601); J=3*np.exp(-it/110)+.05; fig,ax=plt.subplots(figsize=(6.5,3.8))
ax.plot(it,J,color=A,lw=3); ax.axvline(400,color=M,ls='--'); ax.text(410,1.6,'$J(w,b)$ likely\nconverged by\n400 iterations',color=M)
ax.set_xticks(range(0,601,100)); ax.set_xlabel('iterations'); ax.set_ylabel('$J(w,b)$'); ax.set_yticks([])
note(fig,'Schematic learning curve'); save(fig,'gradient-descent-convergence')

# 9 alpha problems
fig,(a1,a2)=plt.subplots(1,2,figsize=(10,3.6)); i1=np.arange(0,60); i2=np.arange(0,45)
a1.plot(i1,1.5+3*np.exp(-i1/80)+.7*np.sin(1.3*i1),color=B,lw=2.5); a2.plot(i2,.4*np.exp(i2/18),color=B,lw=2.5)
for a,t in ((a1,'$J(w,b)$ goes up and down'),(a2,'$J(w,b)$ keeps increasing')): a.set_title(t); a.set_xlabel('iterations'); a.set_ylabel('$J(w,b)$'); a.set_xticks([]); a.set_yticks([])
note(fig,'Schematic: either there is a bug, or $\\alpha$ is too large'); save(fig,'learning-rate-problems')

# 10 activations
z=np.linspace(-5,5,300); fig,axs=plt.subplots(1,3,figsize=(12,3.4))
for ax,y_,t,c in zip(axs,(z,1/(1+np.exp(-z)),np.maximum(0,z)),('Linear: $g(z)=z$','Sigmoid: $g(z)=\\frac{1}{1+e^{-z}}$','ReLU: $g(z)=\\max(0,z)$'),(S,A,B)):
    ax.plot(z,y_,color=c,lw=3); ax.axhline(0,color=T2,lw=.8); ax.axvline(0,color=T2,lw=.8); ax.set_title(t); ax.set_xlabel('$z$'); ax.set_ylabel('$g(z)$')
save(fig,'activation-functions')

# 11 softmax loss
a=np.linspace(.02,1,300); fig,ax=plt.subplots(figsize=(6,3.6)); ax.plot(a,-np.log(a),color=A,lw=3); ax.set_xticks([0,.5,1]); ax.set_ylim(0,4)
ax.set_xlabel('$a_j$'); ax.set_ylabel('$L$'); ax.set_title('loss $=-\\log a_j$ when $y=j$'); save(fig,'softmax-loss')

# 12 bias/variance vs degree
d=np.linspace(1,10,300); Jt=2.5*np.exp(-.45*(d-1))+.1; Jc=Jt+.0006*np.exp(.9*d); k=d[np.argmin(Jc)]
fig,ax=plt.subplots(figsize=(7,4)); ax.plot(d,Jt,color=S,lw=3,label='$J_{train}$'); ax.plot(d,Jc,color=B,lw=3,label='$J_{cv}$'); ax.set_ylim(0,3.2)
for xv,t,c in ((1.9,'underfit',T2),(k,'ideal fit',M),(9.1,'overfit',T2)): ax.axvline(xv,color=c,ls=':'); ax.text(xv,3.0,t,ha='center',color=c)
ax.set_xlabel('degree of polynomial'); ax.set_ylabel('$J$'); ax.legend(loc='center right'); ax.set_yticks([])
note(fig,'Schematic of the sketch on source p. 42'); save(fig,'bias-variance-vs-degree')

# 13 learning curve
m=np.linspace(1,100,200); fig,ax=plt.subplots(figsize=(6.5,3.8)); ax.plot(m,.5+1.6*np.exp(-m/35),color=B,lw=3,label='$J_{cv}$'); ax.plot(m,.45-.4*np.exp(-m/18),color=S,lw=3,label='$J_{train}$')
ax.axhline(.2,color=M,ls='--',label='human performance'); ax.set_xlabel('$m_{train}$ (training set size)'); ax.set_ylabel('error'); ax.set_yticks([]); ax.legend()
note(fig,'Schematic of the sketch on source p. 48'); save(fig,'learning-curve')

# 14 elbow
K=np.arange(1,7); J=[9,4.2,1.6,1.45,1.35,1.3]; fig,ax=plt.subplots(figsize=(6,3.8)); ax.plot(K,J,'o-',color=A,lw=3)
ax.annotate('elbow',(3,1.6),(4,5),color=M,arrowprops=dict(arrowstyle='->',color=M)); ax.set_xlabel('K (no. of clusters)'); ax.set_ylabel('cost function $J$'); ax.set_yticks([])
note(fig,'Schematic of the sketch on source p. 19'); save(fig,'elbow-method')

# 15 k-means steps (real run on synthetic blobs)
rng=np.random.default_rng(7); C=np.array([[0,0],[3.4,.6],[1.5,3.2]]); X=np.vstack([c+rng.normal(0,.6,(25,2)) for c in C]); cols=[A,B,S]
mu=X[[0,30,60]]+np.array([[.6,.8],[-.5,.9],[.9,-.6]])
def assign(mu): return np.argmin(((X[:,None]-mu[None])**2).sum(2),1)
def move(c,mu): return np.array([X[c==k].mean(0) if (c==k).any() else mu[k] for k in range(3)])
c0=assign(mu); mu1=move(c0,mu); mu_f=mu1.copy()
for _ in range(10): cf=assign(mu_f); mu_f=move(cf,mu_f)
fig,axs=plt.subplots(1,4,figsize=(15,3.6),sharex=True,sharey=True)
def pane(ax,c,mu_,t,old=None):
    ax.scatter(*X.T,c=[T2]*len(X) if c is None else [cols[i] for i in c],s=22,alpha=.85); ax.set_title(t,fontsize=10)
    if old is not None:
        for o,n,col in zip(old,mu_,cols): ax.scatter(*o,marker='*',s=160,facecolors='none',edgecolors=col); arrow(ax,o,n,col)
    for n,col in zip(mu_,cols): ax.scatter(*n,marker='*',s=260,color=col,edgecolors=T,linewidths=1.2,zorder=5)
    ax.set_xticks([]); ax.set_yticks([])
pane(axs[0],None,mu,'Randomly initialise $\\mu_1,\\mu_2,\\mu_3$'); pane(axs[1],c0,mu,'Assign points to nearest centroid'); pane(axs[2],c0,mu1,'Move centroids to cluster means',old=mu); pane(axs[3],cf,mu_f,'Repeat until assignments stop changing')
note(fig,'Real K-means run (K=3) on synthetic data, drawn to illustrate the two steps of the algorithm'); save(fig,'k-means-steps')

# 16 gaussian
x=np.linspace(-4.2,4.2,400); pdf=lambda v:np.exp(-v**2/2)/np.sqrt(2*np.pi); fig,ax=plt.subplots(figsize=(7,3.9)); ax.plot(x,pdf(x),color=A,lw=3)
ax.axvline(0,color=T2,ls=':'); ax.text(.08,.02,'$\\mu$',color=T2); ax.scatter([-2.6,-1.6,-1.1,-.7,-.4,-.2,0,.2,.35,.6,.9,1.3,1.9,3.2],np.zeros(14),marker='x',color=T,zorder=4,clip_on=False)
arrow(ax,(0,.2),(1,.2),M,'<->'); ax.text(.5,.215,'$\\sigma$',color=M,ha='center')
for v,c in ((-.9,S),(3.2,B)): ax.plot([v,v],[0,pdf(v)],color=c,lw=2); ax.scatter([v],[pdf(v)],color=c,zorder=5)
ax.text(-4.1,.33,'normal: $p(x)$ large',color=S); ax.text(1.9,.12,'anomaly:\n$p(x)$ tiny',color=B); ax.set_xlabel('$x$'); ax.set_ylabel('$p(x)$'); ax.set_ylim(0,.45)
save(fig,'gaussian-distribution')

# 17 anomaly density
rng=np.random.default_rng(4); mu_=np.array([2.,2.]); cov=np.array([[.5,.2],[.2,.4]]); D=rng.multivariate_normal(mu_,cov,90)
gx,gy=np.meshgrid(np.linspace(-.2,5,200),np.linspace(-.2,4.2,200)); G=np.stack([gx-mu_[0],gy-mu_[1]],-1); md=np.sqrt(np.einsum('...i,ij,...j',G,np.linalg.inv(cov),G))
fig,ax=plt.subplots(figsize=(6,4.4)); ax.contour(gx,gy,md,levels=[1,2,3],colors=[S,A,B],linewidths=2); ax.scatter(*D.T,marker='x',color=T,s=22)
ax.scatter([4.3],[.4],marker='x',color=B,s=110,linewidths=3); ax.annotate('anomaly',(4.3,.4),(3.6,1.3),color=B,arrowprops=dict(arrowstyle='->',color=B))
ax.set_xlabel('$x_1$ (heat)'); ax.set_ylabel('$x_2$ (vibration)'); ax.set_xticks([]); ax.set_yticks([])
note(fig,'Illustrative: contours of a fitted density; low-density points far from the centre are anomalies'); save(fig,'anomaly-density')

# 18 error analysis (counts from source p. 50)
cats=['Pharma','Deliberate\nmisspellings','Unusual email\nrouting','Steal passwords\n(phishing)','Text in\nimage']; cnt=[21,3,7,18,5]
fig,ax=plt.subplots(figsize=(7.5,3.8)); bars=ax.bar(cats,cnt,color=[A,T2,T2,B,T2])
for b_,v in zip(bars,cnt): ax.text(b_.get_x()+b_.get_width()/2,v+.4,str(v),ha='center',color=M)
ax.set_ylabel('misclassified examples'); ax.tick_params(axis='x',labelsize=9); save(fig,'error-analysis-spam')

# 19 speech recognition ladder
fig,ax=plt.subplots(figsize=(6.5,3.8)); lv=[(10.6,'Baseline (human): 10.6%',S),(10.8,'Training error $J_{train}$: 10.8%',A),(14.8,'Cross-validation error $J_{cv}$: 14.8%',B)]
for v,t,c in lv: ax.axhline(v,color=c,lw=3); ax.text(.02,v-.5 if v==10.6 else v+.12,t,color=c,transform=ax.get_yaxis_transform())
arrow(ax,(.8,10.6),(.8,10.8),M,'<->'); ax.text(.84,11.2,'bias gap 0.2%',color=M); arrow(ax,(.8,10.8),(.8,14.8),M,'<->'); ax.text(.84,12.6,'variance gap 4.0%',color=M)
ax.set_xlim(0,1.3); ax.set_ylim(10,15.5); ax.set_xticks([]); ax.set_ylabel('error (%)'); save(fig,'bias-variance-speech-recognition')
print('ok')