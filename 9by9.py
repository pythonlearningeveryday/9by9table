import pandas as pd

s=""

for i in (1,2,3,4,5,6,7,8,9):
    for j in (1,2,3,4,5,6,7,8,9):
        s+= str(i) + "x" +str(j) +"=" +str(i*j)+"\t"
    s+="\n"


cf = pd.DataFrame.to_csv(r's', '9by9')
print(cf)
