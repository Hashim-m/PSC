import re
f={}

with open("pfd/aaa.txt",'r',encoding="utf8") as hashim:

    line=hashim.readline()
    while line:
        if re.findall("^Question[0-9].",line):
            k=str(line)
            f[k]=[]
            line=hashim.readline()
            while re.findall("^[A-D]",line):
                f[k].append(str(line))
                line=hashim.readline()
        else:
            line=hashim.readline()
        
        
            

