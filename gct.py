from datetime import datetime

def gct(mode,out=None):
    ct = None

    cur_time = datetime.now()
    if mode == "nosep":
        ct_null = "%s%s%s%s%s%s%s"%(cur_time.year,cur_time.month,cur_time.day,cur_time.hour,cur_time.minute,cur_time.second,cur_time.microsecond)
        ct = int(ct_null)

    if mode == "ysep":
        ct_f= "%s/%s/%s %s:%s:%s:%s"%(cur_time.year,cur_time.month,cur_time.day,cur_time.hour,cur_time.minute,cur_time.second,cur_time.microsecond)
        ct = str(ct_f)

    if mode == "gs":
        ct_sec = "%s"%(cur_time.second)
        ct = int(ct_sec)

    if mode == "gm":
        ct_min = "%s"%(cur_time.minute)
        ct = int(ct_min)
    
    if mode == "gmis":
        ctms = "%s"%(cur_time.microsecond)
        ct = int(ctms)/1000
    out = ct
    return out