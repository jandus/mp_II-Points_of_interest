# get keys from file

def get_key(location, dict_name):
    dict_name = {}
    f = open(location, "r")
    for l in f:
        kv = l.split()
        dict_name[kv[0]] = kv[1]
    f.close()
    return dict_name

# Foursquare
fsq = get_key("/Users/jandas/api/foe", "fsq")

#Visual Crossing Weather
yep = get_key("/Users/jandas/api/yep", "yep")