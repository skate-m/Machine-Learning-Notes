"""Inserts a labelled 'Detailed Explanation' section into every topic note (before 'Related topics'). Safe to re-run."""
import re,sys,os
sys.path.insert(0,'scripts')
import details_a,details_b,details_c
D={**details_a.D,**details_b.D,**details_c.D}
HEAD="> **Additional Explanation:**  \n> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.\n>\n"
def block(t): return '\n'.join('> '+l if l.strip() else '>' for l in t.strip().split('\n'))
n=0
for path,text in D.items():
    s=open(path,encoding='utf-8').read()
    if '## Detailed Explanation' in s: continue
    sec='## Detailed Explanation\n\n'+HEAD+block(text)+'\n\n'
    m=re.search(r'^## (?:\d+\. )?Related topics',s,re.M)
    s=s[:m.start()]+sec+s[m.start():] if m else s.rstrip()+'\n\n'+sec
    open(path,'w',encoding='utf-8').write(s); n+=1
print('expanded',n,'of',len(D))