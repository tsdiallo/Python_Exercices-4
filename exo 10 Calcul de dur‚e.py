def hms_to_s (h,m,s):
    sec=h*3600+m*60+s
    return sec
print ("1h30l=", hms_to_s (1,30,0),"s")
print ("3h20m15s=", hms_to_s (3,20,15),"s")

def s_to_hms (s):
    H=s/3600
    r=s%3600
    m=r/60
    s=r%60
    return [H,m,s]
print (s_to_hms (5400))
print (s_to_hms (12015))


def afficher_temps (hms):
    hms=[H,m,s]
    hms =[2,42,16]
    H=hms[0]
    m=hms[1]
    s=hms[2]
    return H,"heures",m,"minutes","et",s,"secondes"

print (afficher_temps (hms))
