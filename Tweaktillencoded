import csv
import sys
import codecs

#uprint function
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)







a=[]
with open('powershellEncoded.csv') as f:
    rows = csv.reader(f)
    for row in rows:
         
        onlyBase64=(row[-1]).split('-EncodedCommand'or'-encodedcommand', 1)[-1]
        a.append(onlyBase64)
uprint("a")       
uprint(a)


#do it before the and list it up

## appending data to csv bro

orig_stdout = sys.stdout
f = open('out.csv', 'w')
sys.stdout = f

for i in a:
    print(i)
    

sys.stdout = orig_stdout
f.close()


