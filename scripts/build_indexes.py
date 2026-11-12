"""Builds the module README files, the root README table of contents and mkdocs.yml from the topic files.  Run from repo root."""
import os,re,glob
MODS=[
('01-supervised-learning','01 — Supervised Learning','Regression and classification: linear and logistic regression, gradient descent, feature scaling, overfitting and regularization.'),
('02-advanced-learning-algorithms','02 — Advanced Learning Algorithms','Neural networks: layers, activation functions, softmax, vectorization, TensorFlow training steps, backpropagation, Adam.'),
('03-model-evaluation-and-ml-practice','03 — Model Evaluation and ML Practice','Train/CV/test sets, model selection, bias and variance, learning curves, error analysis, metrics, transfer learning, deployment.'),
('04-decision-trees-and-ensembles','04 — Decision Trees and Ensembles','Decision trees, entropy, information gain, one-hot encoding, regression trees, random forests, XGBoost.'),
('05-unsupervised-learning','05 — Unsupervised Learning','K-means clustering, choosing K, the Gaussian distribution and anomaly detection.'),
('06-recommenders-and-reinforcement-learning','06 — Recommenders and Reinforcement Learning','Collaborative and content-based filtering, retrieval and ranking, return, policy and the Q function.'),
]
def info(path):
    t=open(path,encoding='utf-8').read()
    title=re.search(r'^# (.+)$',t,re.M).group(1).strip()
    src=re.search(r'\*\*Source pages?:\*\*\s*([^·\n]+)',t); src=src.group(1).strip() if src else ''
    return title,src
toc=[];nav=['  - Home: index.md']
for d,name,desc in MODS:
    files=sorted(f for f in os.listdir(d) if f.endswith('.md') and f!='README.md')
    rows=[];navs=[]
    for f in files:
        title,src=info(f'{d}/{f}'); rows.append((f,title,src)); navs.append(f'      - "{title}": {d}/{f}')
    body=f'# {name}\n\n> {desc}\n\n| # | Topic | Source pages (PDF) |\n|---|---|---|\n'+''.join(f'| {i+1} | [{t}]({f}) | {s} |\n' for i,(f,t,s) in enumerate(rows))
    pass
    open(f'{d}/README.md','w',encoding='utf-8').write(body)
    toc.append(f'### [{name}]({d}/README.md)\n\n{desc}\n\n'+''.join(f'{i+1}. [{t}]({d}/{f})\n' for i,(f,t,s) in enumerate(rows))+'\n')
    nav.append(f'  - "{name}":\n      - Overview: {d}/README.md\n'+'\n'.join(navs))
tmpl=open('scripts/readme_template.tpl',encoding='utf-8').read()
open('README.md','w',encoding='utf-8').write(tmpl.replace('{{TOC}}',''.join(toc)))
nav.append('  - Transcription notes: TRANSCRIPTION_NOTES.md')
yml=open('scripts/mkdocs_template.yml',encoding='utf-8').read().replace('{{NAV}}','\n'.join(nav))
open('mkdocs.yml','w',encoding='utf-8').write(yml)
print('built')