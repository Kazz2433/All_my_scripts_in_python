def build_user(fname,lname,**misc):
    profile = {}
    profile["First name"] = fname
    profile["Last name"] = lname
    for k,v in misc.items():
        profile[k] = v
    return profile

u = build_user('Kelvin','Quida',location='BR',language='Potuguese - English - French')
print(u)
