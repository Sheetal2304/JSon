import json
from os import nice
myfile=open("myfile.json","r+")
a=json.load(myfile)
print(a)
myfile.close()

