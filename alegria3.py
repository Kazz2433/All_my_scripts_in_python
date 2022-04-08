def car(*name,**model):
    dic = {}
    dic["Name"] = name
    dic["Model"] = model
    for k,v in dic.items():
        dic[k] = v
    return dic

a = car('subaru','outback',color='blue', tow_package=True)
print(a)
