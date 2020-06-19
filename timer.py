import gct
import minus

st=None

lst = []
def gfs (out=None):
    global lst
    minute = gct.gct("gm")
    second = gct.gct("gs")
    mill_sec = gct.gct("gmis")
    mts = minute*60
    mls_ts = mill_sec/1000
    fs = second+mts+mls_ts
    out = fs
    return out

def start():
    global st
    st = gfs()

def end(display=True):
    global st
    et = gfs()
    ans = et-st
    if display == True:
        print("Time used:%s%s"%(round(float(ans))," second"))
        print("Exactly:",ans,"second")
    return ans