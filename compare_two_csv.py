import csv
import sys
a=[]
with open('Suspicious_downloads_Bitsadmin1.csv') as f:
    rows = csv.reader(f)
    for row in rows:
        a.append((row[-1]))
#print("a")       
#print(a)

b=[]
with open('Suspicious_downloads_Bitsadmin.csv') as g:

    rows1 = csv.reader(g)
    for row1 in rows1:
         b.append((row1[-1]))
#print("b")
#print(b)

common=[]
common=list((set(a).intersection(set(b))))
#print("cc")
print(common)

## appending data to csv bro


orig_stdout = sys.stdout
f = open('out.csv', 'w')
sys.stdout = f

for i in common:
    print(i)
    

sys.stdout = orig_stdout
f.close()
