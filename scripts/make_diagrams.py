"""Generates the SVG diagrams in assets/diagrams/ (Midnight Lavender palette).  Run from repo root: python scripts/make_diagrams.py"""
from xml.sax.saxutils import escape
BG='#171821'; BG2='#222332'; CARD='#2C2B40'; A='#A78BFA'; B='#E89BB5'; M='#EAC477'; S='#91C7A5'; T='#F1EFF7'; T2='#AAA9BB'
FONT="Nunito,'Segoe UI',Helvetica,Arial,sans-serif"

class Svg:
    def __init__(s,w,h,title,desc=''): s.w,s.h,s.title,s.desc,s.e,s.mk=w,h,title,desc,[],set()
    def _mk(s,c): s.mk.add(c); return f'url(#ah{c[1:]})'
    def rect(s,x,y,w,h,fill=CARD,stroke=A,rx=12,sw=2,dash=None):
        d=f' stroke-dasharray="{dash}"' if dash else ''
        s.e.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
    def box(s,cx,cy,w,h,label,fill=CARD,stroke=A,size=14,color=T,rx=12,sw=2,dash=None):
        s.rect(cx-w/2,cy-h/2,w,h,fill,stroke,rx,sw,dash); s.text(cx,cy,label,size,color)
    def ell(s,cx,cy,rx,ry,fill=CARD,stroke=A,sw=2): s.e.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    def circle(s,cx,cy,r,fill=CARD,stroke=A,sw=2): s.e.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    def text(s,x,y,t,size=14,fill=T,anchor='middle',weight=400):
        lines=str(t).split('\n'); y0=y-(len(lines)-1)*size*0.6+size*0.35
        tsp=''.join(f'<tspan x="{x}" dy="{0 if i==0 else size*1.2}">{escape(l)}</tspan>' for i,l in enumerate(lines))
        s.e.append(f'<text x="{x}" y="{y0}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{tsp}</text>')
    def line(s,x1,y1,x2,y2,c=T2,sw=2,arrow=False,dash=None):
        m=f' marker-end="{s._mk(c)}"' if arrow else ''; d=f' stroke-dasharray="{dash}"' if dash else ''
        s.e.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{sw}"{d}{m}/>')
    def path(s,d,c=T2,sw=2,fill='none',arrow=False,dash=None):
        m=f' marker-end="{s._mk(c)}"' if arrow else ''; dd=f' stroke-dasharray="{dash}"' if dash else ''
        s.e.append(f'<path d="{d}" fill="{fill}" stroke="{c}" stroke-width="{sw}"{dd}{m}/>')
    def poly(s,pts,fill=CARD,stroke=A,sw=2): s.e.append(f'<polygon points="{" ".join(f"{x},{y}" for x,y in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    def tri(s,cx,cy,r=10,c=M): s.poly([(cx,cy-r),(cx+r,cy+r*.8),(cx-r,cy+r*.8)],fill=c,stroke=c,sw=1)
    def sq(s,cx,cy,r=9,c=B): s.rect(cx-r,cy-r,2*r,2*r,fill=c,stroke=c,rx=2,sw=1)
    def save(s,name):
        defs=''.join(f'<marker id="ah{c[1:]}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>' for c in s.mk)
        svg=(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s.w} {s.h}" width="{s.w}" height="{s.h}" font-family="{FONT}" role="img" aria-labelledby="t d">'
             f'<title id="t">{escape(s.title)}</title><desc id="d">{escape(s.desc or s.title)}</desc><defs>{defs}</defs>'
             f'<rect width="{s.w}" height="{s.h}" rx="16" fill="{BG}"/>'+''.join(s.e)+'</svg>')
        open(f'assets/diagrams/{name}.svg','w',encoding='utf-8').write(svg)

def vdots(s,x,y,c=T2):
    for k in (-8,0,8): s.circle(x,y+k,2,fill=c,stroke=c,sw=0)

def network(s,sizes,x0,x1,cy,gap,r=16,fills=None,nums=False):
    L=len(sizes); xs=[x0+i*(x1-x0)/(L-1) for i in range(L)]; pos=[]
    for x,n in zip(xs,sizes): pos.append([(x,cy+(j-(n-1)/2)*gap) for j in range(n)])
    for a,b in zip(pos,pos[1:]):
        for p in a:
            for q in b: s.line(p[0]+r,p[1],q[0]-r,q[1],c='#4a4963',sw=1.2)
    for i,col in enumerate(pos):
        for j,(x,y) in enumerate(col):
            s.circle(x,y,r,fill=CARD,stroke=[A,S,B,M][i%4]);
            if nums and 0<i<L-1: s.text(x,y,str(j+1),13,T)
    return pos

# 1 decision tree
s=Svg(720,390,'Decision tree for cat classification','Root node Ear shape splits into Face shape and Whiskers decision nodes, ending in Cat / Not Cat leaves.')
s.ell(360,60,78,28,stroke=A); s.text(360,60,'Ear shape',16); s.text(360,18,'root node',12,T2)
s.ell(185,180,78,28,stroke=S); s.text(185,180,'Face shape',16); s.ell(535,180,78,28,stroke=S); s.text(535,180,'Whiskers',16); s.text(640,215,'decision node',12,T2)
for p,q,l,dx in ((( 330,86),(215,154),'Pointy',-38),((390,86),(505,154),'Floppy',38),((155,206),(95,278),'Round',-30),((215,206),(265,278),'Not round',32),((505,206),(445,278),'Present',-32),((565,206),(625,278),'Absent',32)):
    s.line(*p,*q,arrow=True); s.text((p[0]+q[0])/2+dx,(p[1]+q[1])/2,l,12,M)
for x,l,c in ((85,'Cat',S),(275,'Not Cat',B),(435,'Cat',S),(635,'Not Cat',B)): s.box(x,310,120,54,l,stroke=c,size=16)
s.text(360,372,'leaves',12,T2); s.save('decision-tree-cat')

# 2 information gain split
s=Svg(760,420,'Information gain example: splitting on ear shape','10 animals at the root (5 cats, 5 dogs) split by ear shape into pointy (4 cats, 1 dog) and floppy (1 cat, 4 dogs).')
def cluster(cx,cy,cats,dogs):
    items=['t']*cats+['q']*dogs
    for i,k in enumerate(items):
        x=cx-48+(i%5)*24; y=cy-14+(i//5)*30
        (s.tri if k=='t' else s.sq)(x,y)
s.box(380,78,330,100,'',stroke=A); cluster(380,64,5,5); s.text(380,20,'root node: 10 examples',13,T2); s.text(380,118,'p1(root) = 5/10 = 0.5',14,M)
s.line(300,132,190,205,arrow=True); s.line(460,132,570,205,arrow=True); s.text(215,160,'Pointy',13,M); s.text(545,160,'Floppy',13,M)
s.box(190,265,270,100,'',stroke=S); cluster(190,258,4,1); s.text(190,325,'p1(left) = 4/5     w(left) = 5/10',14,M)
s.box(570,265,270,100,'',stroke=B); cluster(570,258,1,4); s.text(570,325,'p1(right) = 1/5     w(right) = 5/10',14,M)
s.tri(60,375,9); s.text(76,375,'cat',13,T,'start'); s.sq(140,375,8); s.text(156,375,'dog',13,T,'start')
s.text(740,375,'p1 = cat fraction,   w = fraction of examples after split',13,T2,'end'); s.save('information-gain-split')

# 3 random forest
s=Svg(780,360,'Random forest ensemble','Training set of size m is resampled with replacement B times; a decision tree is trained on each new set and the trees vote.')
s.box(90,180,130,90,'Training set\nsize m',stroke=A,size=15)
for y,l in ((60,'Tree 1'),(140,'Tree 2'),(300,'Tree B')):
    s.line(155,180,238,y,arrow=True,c=T2)
    s.box(300,y,120,54,'new set\nsize m',stroke=S,size=13); s.line(360,y,420,y,arrow=True,c=T2); s.box(480,y,110,54,l,stroke=B,size=15); s.line(535,y,598,180,arrow=True,c=T2)
vdots(s,300,222); vdots(s,480,222)
s.text(196,20,'sampling with replacement',12,M); s.box(670,180,140,90,'vote on\nfinal decision',stroke=M,size=15)
s.text(390,345,'at each node: pick random subset of K < n features (ideally K = √n), choose the best split from those K',12,T2); s.save('random-forest')

# 4 t-shirt network
s=Svg(780,400,'Neural network for t-shirt demand prediction','Four inputs feed a hidden layer of three neurons (affordability, awareness, perceived quality) and an output neuron giving the probability of being a top seller.')
pos=network(s,[4,3,1],300,560,185,72,r=20,nums=True)
for (x,y),l in zip(pos[0],('price','shipping cost','marketing','material')): s.text(x-32,y,l,14,T,'end')
s.text(300,45,'input',13,T2); s.text(430,45,'hidden layer',13,T2)
s.line(pos[2][0][0]+22,185,640,185,arrow=True); s.text(700,170,'a',16,M); s.text(705,200,'probability of\nbeing a top seller',13,T,'middle')
s.text(390,340,'hidden neurons:  1 = affordability    2 = awareness    3 = perceived quality',13,T2); s.save('neural-network-tshirt')

# 5 layers 25-15-1
s=Svg(780,300,'Neural network with layers of 25, 15 and 1 units','Input vector a[0] feeds layers of 25 units, 15 units and 1 unit; a[1], a[2] and a[3] are the activations; the output is a probability.')
def col(cx,label,sub,c):
    s.rect(cx-34,50,68,200,fill=CARD,stroke=c)
    for k,y in enumerate((85,125,175,215)):
        if k==2: vdots(s,cx,152)
        else: s.circle(cx,y if k<2 else y-0,12,fill=BG2,stroke=c)
    s.text(cx,275,label,13,T); s.text(cx,24,sub,12,T2)
col(100,'input','',T2); col(300,'25 units','hidden',A); col(500,'15 units','hidden',S); s.rect(646,125,56,56,fill=CARD,stroke=B); s.circle(674,153,12,fill=BG2,stroke=B); s.text(674,275,'1 unit',13); s.text(674,100,'output',12,T2)
for a,b,l in ((136,264,'a[0]'),(336,464,'a[1]'),(536,642,'a[2]')): s.line(a,150,b,150,arrow=True); s.text((a+b)/2,132,l,14,M)
s.line(704,153,760,153,arrow=True); s.text(742,135,'a[3]',14,M); s.text(742,176,'probability',12,T); s.save('layer-sizes-25-15-1')

# 6 image recognition
s=Svg(780,260,'Image recognition: features learned layer by layer','Face image passes through layers that detect lines and patterns, then parts like eyes and nose, then possible faces.')
for x,l,c in ((90,'face image\n(input)',T2),(270,'1st hidden layer\nlines and patterns',A),(480,'2nd hidden layer\neyes, nose, …',S),(690,'3rd hidden layer\npossible faces',B)): s.box(x,125,150,100,l,stroke=c,size=14)
for a,b in ((165,195),(345,405),(555,615)): s.line(a,125,b,125,arrow=True)
s.text(390,220,'earlier layers detect simple patterns; later layers combine them',13,T2); s.save('image-recognition-layers')

# 7 convolutional layer
s=Svg(780,420,'Convolutional layer on an ECG signal','Each neuron of the convolutional layer looks only at a window of the input: x1-x20, x11-x30, x21-x40 and so on.')
s.rect(60,40,110,340,fill=CARD,stroke=T2)
for y,l in ((70,'x₁'),(110,'x₂'),(150,'x₃')): s.text(115,y,l,15)
vdots(s,115,205); s.text(115,360,'x₁₀₀',15)
s.path('M70,240 l8,-18 l8,34 l8,-30 l8,28 l8,-24 l8,20 l8,-14 l8,12',c=T2,sw=1.5)
wins=((50,'x₁ – x₂₀',A),(185,'x₁₁ – x₃₀',S),(300,'x₂₁ – x₄₀',B))
for y,l,c in wins:
    s.rect(174,y-20,26,70,fill='none',stroke=c,rx=4); s.line(200,y+15,360,y+15+(0 if y==185 else 0),c=c,arrow=True) if False else None
    s.line(200,y+15,380,150+(y-185)*0.55,c=c,arrow=True); s.text(268,y+(8 if y!=300 else 14),l,13,c)
s.rect(380,70,60,260,fill=CARD,stroke=M)
for y in (130,200,270): s.circle(410,y,16,fill=BG2,stroke=M)
s.text(410,50,'convolutional\nlayer',12,T2); vdots(s,410,320)
s.line(440,200,540,200,arrow=True,c=T2); s.rect(545,130,60,140,fill=CARD,stroke=S)
for y in (165,200,235): s.circle(575,y,12,fill=BG2,stroke=S)
s.text(575,115,'next layer',12,T2); s.line(605,200,670,200,arrow=True,c=T2); s.box(715,200,60,50,'σ',stroke=B,size=20); s.text(715,240,'sigmoid',12,T2); s.save('convolutional-layer-ecg')

# 8 bias/variance flow
s=Svg(780,360,'Bias/variance workflow for neural networks','If the network does poorly on the training set use a bigger network; if poorly on the cross validation set get more data; otherwise done.')
s.box(150,70,210,70,'Does it do well\non training set?',stroke=A); s.box(470,70,230,70,'Does it do well on\ncross validation set?',stroke=A)
s.line(255,70,355,70,arrow=True); s.text(305,55,'Yes',13,S)
s.ell(150,250,80,34,stroke=B); s.text(150,250,'Bigger\nnetwork',15); s.line(150,105,150,214,arrow=True); s.text(168,160,'No',13,B,'start')
s.ell(400,250,80,34,stroke=B); s.text(400,250,'More\ndata',15); s.line(440,105,420,216,arrow=True); s.text(446,160,'No',13,B,'start')
s.ell(690,250,70,34,stroke=S); s.text(690,250,'Done!',16); s.line(585,70,690,70,c=T2); s.line(690,70,690,214,arrow=True); s.text(670,150,'Yes',13,S,'end')
s.path('M70,250 L40,250 L40,70 L45,70',c=T2,arrow=True); s.line(70,250,70,250); s.path('M400,284 L400,325 L40,325 L40,250',c=T2)
s.text(390,345,'repeat the loop after each change',12,T2); s.save('bias-variance-flow')

# 9 ML project cycle
s=Svg(820,300,'Cycle of an ML project','Scope project, collect data, train model, deploy in production, with arrows returning to earlier stages.')
labels=(('Scope\nproject','Define project'),('Collect\nData',''),('Train\nModel','Training, error analysis\nand iterative improvement'),('Deploy in\nproduction','Deploy, monitor and\nmaintain system'))
for i,(l,sub) in enumerate(labels):
    x=40+i*195; s.poly([(x,110),(x+150,110),(x+185,160),(x+150,210),(x,210),(x+35,160)],fill=CARD,stroke=[A,S,B,M][i]); s.text(x+95,160,l,16)
    if sub: s.text(x+95,245,sub,12,T2)
for a,b in ((520,350),(520,155),(710,540),(710,350)): pass
s.path('M300,100 C300,50 130,50 130,100',c=T2,arrow=True,dash='5 4'); s.path('M495,100 C495,40 130,40 130,100',c=T2,arrow=True,dash='5 4'); s.path('M690,100 C690,30 300,30 300,100',c=T2,arrow=True,dash='5 4')
s.text(410,22,'iterate: later stages send you back to earlier ones',12,T2); s.save('ml-project-cycle')

# 10 ML development loop
s=Svg(700,360,'Iterative loop of ML development','Choose architecture (model, data, etc.), train model, run diagnostics (bias, variance and error analysis), then repeat.')
s.box(350,60,300,60,'Choose architecture\n(model, data, etc.)',stroke=A); s.box(570,290,200,60,'Train\nmodel',stroke=S); s.box(130,290,230,60,'Diagnostics\n(bias, variance and error analysis)',stroke=B,size=13)
s.path('M470,85 C560,130 590,200 580,255',c=T2,arrow=True); s.path('M470,300 L250,300',c=T2,arrow=True); s.path('M120,258 C110,190 180,110 215,80',c=T2,arrow=True); s.save('ml-development-loop')

# 11 deployment
s=Svg(760,260,'Deployment: inference server and mobile app','The mobile app sends an API call with x (an audio clip) to an inference server running the ML model; the server returns the inference y-hat (a text transcript).')
s.rect(40,40,280,180,stroke=A); s.text(180,62,'Inference server',15); s.box(180,150,150,70,'ML model',stroke=S,size=15)
s.rect(470,40,250,180,stroke=B); s.text(595,130,'Mobile app',16)
s.line(470,85,320,85,arrow=True,c=M); s.text(395,60,'API call (x)',13,M); s.text(395,102,'(audio clip)',12,T2)
s.line(320,175,470,175,arrow=True,c=S); s.text(395,150,'Inference (ŷ)',13,S); s.text(395,192,'(text transcript)',12,T2); s.save('deployment')

# 12 confusion matrix
s=Svg(540,400,'Confusion matrix for precision and recall','Rows are predicted 1 or 0, columns are actual 1 or 0: true positive, false positive, false negative, true negative.')
s.text(340,34,'Actual',15,M); s.text(255,64,'1',15); s.text(425,64,'0',15); s.text(60,200,'Predicted',15,M); s.text(150,150,'1',15); s.text(150,290,'0',15)
for x,y,l,c in ((170,80,'True\nPositive',S),(340,80,'False\nPositive',B),(170,220,'False\nNegative',B),(340,220,'True\nNegative',S)): s.rect(x,y,170,140,fill=CARD,stroke=c); s.text(x+85,y+70,l,17)
s.save('confusion-matrix')

# 13 two tower
s=Svg(780,360,'Two-network (user and movie) recommender','User features x_u pass through one network to give v_u; movie features x_m pass through another to give v_m; their dot product is the predicted rating.')
for y,xl,vl,c in ((90,'x_u','v_u',A),(260,'x_m','v_m',S)):
    s.text(60,y,xl,18,c); s.line(85,y,130,y,arrow=True)
    for k,(x,hh) in enumerate(((160,110),(290,80),(400,50))):
        s.rect(x-22,y-hh/2,44,hh,fill=CARD,stroke=c)
        for dy in (-hh/4,0,hh/4): s.circle(x,y+dy,6,fill=BG2,stroke=c)
    s.line(185,y,265,y,arrow=True); s.line(315,y,376,y,arrow=True); s.line(424,y,500,y,arrow=True); s.text(525,y,vl,18,c)
s.line(535,105,590,160,c=T2); s.line(535,245,590,190,c=T2); s.circle(610,175,20,fill=CARD,stroke=M); s.circle(610,175,4,fill=M,stroke=M)
s.line(630,175,700,175,arrow=True); s.text(735,175,'Prediction',13,M); s.text(390,335,'cost J = Σ (v_u · v_m − y)²  over rated pairs  +  NN regularization term',13,T2); s.save('two-network-recommender')

# 14 retrieval + ranking
s=Svg(820,300,'Recommender pipeline: retrieval then ranking','Retrieval generates many plausible candidates, they are combined with duplicates and watched items removed, then ranked by the learned model and displayed.')
steps=(('Retrieval','generate a large list of\nplausible item candidates',A),('Combine','remove duplicates and\nitems already watched',S),('Ranking','rank the list using the\nlearned model (neural net)',B),('Display','show ranked items',M))
for i,(t,sub,c) in enumerate(steps):
    x=105+i*200; s.box(x,115,170,90,t,stroke=c,size=17); s.text(x,200,sub,12,T2)
    if i: s.line(x-185+85+10,115,x-85,115,arrow=True)
s.text(105,255,'e.g. similar to each of the last 10\nwatched movies; top 20 in country',12,M); s.save('retrieval-ranking')

# 15 mars rover
s=Svg(760,230,'Mars rover with six states','Six states in a row; state 1 has reward 100 and state 6 has reward 40.')
for i in range(6):
    x=40+i*113; s.rect(x,70,113,90,fill=CARD,stroke=A); s.text(x+56,185,f'state {i+1}',14,T2)
s.text(96,115,'100',24,M); s.text(96,142,'reward',11,T2); s.text(660,115,'40',24,M); s.text(660,142,'reward',11,T2)
for i in (1,2,3,4): s.text(40+i*113+56,115,'0',20,T)
s.text(380,40,'discount factor γ = 0.9',14,S); s.save('mars-rover')

# 16 Q function
s=Svg(640,230,'State-action value Q(2, left)','Four states; terminal rewards 100 and 40; from state 2 going left reaches state 1 with reward 100, so Q(2, left) = 0 + 0.5 x 100 = 50.')
for i,(l,c) in enumerate((('100',M),('',T),('',T),('40',M))): s.rect(40+i*140,70,140,90,fill=CARD,stroke=A); s.text(110+i*140,115,l,24,c); s.text(110+i*140,185,f'state {i+1}',13,T2)
s.line(250,140,190,140,arrow=True,c=S); s.line(390,140,330,140,arrow=True,c=S); s.text(180,50,'Q(2, ←) = 0 + (0.5) · 100 = 50',16,S,'start'); s.save('q-function-example')

# 17 anomaly data split
s=Svg(820,380,'Data splits for anomaly detection (aircraft engines)','10000 good and 20 flawed engines split into training, cross-validation and test sets, or alternatively training and cross-validation only.')
def row(y,items,title):
    s.text(20,y-34,title,13,M,'start'); x=20
    for w,l,c in items: s.box(x+w/2,y+10,w-8,60,l,stroke=c,size=13); x+=w
row(80,((300,'Training set\n6000 good engines',A),(250,'CV set\n2000 good (y=0)\n10 anomalous (y=1)',S),(250,'Test set\n2000 good (y=0)\n10 anomalous (y=1)',B)),'10000 good engines (y=0), 20 flawed engines (y=1)')
row(240,((300,'Training set\n6000 good engines',A),(500,'CV set\n4000 good (y=0), 20 anomalous (y=1)',S)),'Alternative: no test set (if very few anomalies)')
s.text(420,330,'use the CV set to tune ε and the features xⱼ',13,T2); s.text(420,352,'alternative carries a higher risk of overfitting',12,T2); s.save('anomaly-data-split')

# 18 transfer learning
s=Svg(780,300,'Transfer learning','Download pretrained network parameters, then further train the network on your own data.')
s.box(130,100,200,70,'1. Download parameters\npretrained on a large dataset',stroke=A,size=13); s.line(232,100,300,100,arrow=True)
s.box(400,100,190,70,'network with same\ninput type as your app',stroke=S,size=13); s.line(496,100,560,100,arrow=True)
s.box(670,100,190,70,'2. Further train on\nyour own data',stroke=B,size=13)
s.box(300,215,230,56,'i) change output layer parameters\n(fine tuning)',stroke=M,size=12); s.box(580,215,230,56,'ii) train all parameters',stroke=M,size=12); s.line(670,136,600,186,c=M,arrow=True); s.line(640,136,330,186,c=M,arrow=True); s.save('transfer-learning')

# 19 backprop vs GD
s=Svg(780,250,'Backpropagation versus gradient descent','Backpropagation computes gradients with the chain rule; gradient descent uses them to update weights and biases.')
s.box(120,100,170,70,'Loss / cost J',stroke=T2,size=15); s.line(205,100,265,100,arrow=True)
s.box(390,100,230,90,'Backpropagation\nbackward error propagation\n(chain rule)',stroke=A,size=13); s.line(506,100,566,100,arrow=True); s.text(536,80,'gradients',12,M)
s.box(660,100,180,90,'Gradient descent\nupdates weights\nand biases',stroke=S,size=13); s.path('M660,150 C660,225 120,225 120,138',c=T2,arrow=True,dash='5 4'); s.text(390,232,'repeat: iteratively step down the loss surface',12,T2); s.save('backpropagation-vs-gradient-descent')

# 20 banner + roadmap
s=Svg(900,200,'Machine Learning Notes','Digitised handwritten Machine Learning notes')
s.rect(0,0,900,200,fill=BG,stroke=BG,rx=16); s.text(450,78,'Machine Learning Notes',44,A,'middle',700); s.text(450,126,'digitised, typeset and illustrated from handwritten notes',17,T); s.text(450,158,'supervised learning · neural networks · trees · clustering · recommenders · RL',14,T2)
for i,c in enumerate((A,B,M,S,T2)): s.rect(300+i*60,176,48,6,fill=c,stroke=c,rx=3,sw=0)
s.save('banner')
s=Svg(900,300,'Learning roadmap','Recommended order: supervised learning, neural networks, model evaluation and ML practice, decision trees and ensembles, unsupervised learning, recommenders and reinforcement learning.')
mods=(('01','Supervised\nlearning',A),('02','Advanced learning\nalgorithms',B),('03','Model evaluation\n& ML practice',M),('04','Decision trees\n& ensembles',S),('05','Unsupervised\nlearning',A),('06','Recommenders\n& RL',B))
for i,(n,l,c) in enumerate(mods):
    x=85+i*146; s.box(x,130,128,110,'',stroke=c); s.text(x,98,n,24,c,'middle',700); s.text(x,148,l,13,T)
    if i: s.line(x-73,130,x-64+0,130,arrow=True) if False else s.line(x-78,130,x-66,130,c=T2,arrow=True)
s.text(450,40,'Recommended study order',18,T); s.text(450,262,'each module links back to the notes it builds on',13,T2); s.save('learning-roadmap')
print('ok')