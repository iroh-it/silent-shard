## imports ##
import math as function
from math import sqrt as root
import json as structure
from time import sleep as wait
## pathing ##
file = "myFormat"
form = ".json"

dataDump = {}

## sudo class functions ##
def readJson(oFile=None):
    if oFile is None:
        oFile = file
    with open(f"{oFile}{form}","r") as f:
        data = f.read()
        json = structure.loads(data)
        f.close()
        return json
def writeJson(oFile,newData):
    with open(f"{oFile}{form}","w+") as f:
        data = structure.dumps(newData)
        f.write(data)
        f.close()
        return newData
###  huh  ###
def mean(lst,figs=16):
    numer = sum(lst)
    denem = len(lst)
    return round( (numer/denem), figs)
### functions ###    
def root_iT(myInt):
    if not isinstance(myInt,int):
        print("(e) <> not an int")
        print(f"(e)  |  {myInt}")
        return False
    else:
        steps = [myInt]; i = 1
        ans = root(myInt)
        counts = {}
        while ans > 1.00000000000000001: # 16
            ans = root(ans)
            #    print(ans)
            steps.append(ans)
            i += 1
        Ra = steps[51]; step = i-52
        Ra = (Ra)
        return [Ra, [i-52,steps]]
def cPrint(string):
    dispS = f"(Ra) | {string}"
    print(dispS)
def pDisp(iT):
    ## [Ra, [i,steps]] ##
    cPrint(f"val: {iT[0]} <> steps: {iT[1][0]}")

#############
#\   root  /#
### async ###
bPhia = "0.27"
def build(ad):
    global bPhia
    bPhia = f"{bPhia}{ad}"
    return bPhia
def phia():
    global bPhia
    ePhia = float(bPhia)
    ePhia = (float(ePhia)*100) - 27
    return ePhia
xxvii = 0
def calc(value=2):
    i = 2; oLst = []
    global xxvii
    while i < value+1:
        oLst.append( root_iT(i)[0] )
        i += 1
    oLst = oLst[1:]
    cPrint(f"oLst [{xxvii}] len({len(oLst)})")
    xxvii += 1
    build(  str( len(oLst) )  )
    
    #cPrint(f"so -> {phia()}")

def run(val):
    i = 0; expresh = 0
    global bPhia
    while i <= val:
        expresh = 5*(3**i)
        i += 1
        lstEx = True
        if expresh <= 1000:
            lstEx = False
        #print(f"{lstEx} was")
            
        calc(expresh)
    cPrint(f"#[{1+val}]# so -> {phia()}")
    cPrint(f"{bPhia}")
    cPrint("-----")
    cPrint( (float(bPhia)*100) - 27)

    

    









