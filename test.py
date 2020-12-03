import re
import sys

count=0
list1=[]
flag=True
#todo
n=sys.argv[1]
if re.search('[A-Za-z]+',n) is None: 
    flag=False
    count+=1
    ans='不包含英文'
    list1.append(ans)
if re.search('[0-9]+',n) is None: 
    flag=False
    count+=1
    ans='不包含數字'
    list1.append(ans)    
if re.search('\W+',n) is None: 
    if re.search('_',n) is None:        
        flag=False
        count+=1
        ans='不包含符號'
        list1.append(ans)
if n.islower():
    flag=False
    count+=1
    ans='不包含大寫字母'
    list1.append(ans)
if 8>len(n):
    flag=False
    count+=1
    ans='字串長度小於8'
    list1.append(ans)
if 16<len(n):
    flag=False
    count+=1
    ans='字串長度大於16'
    list1.append(ans)    
if flag==True:
    print("Success")
else:
    print("Fail")
for i in range(count):
    print("Error: {}".format(list1[i]))
