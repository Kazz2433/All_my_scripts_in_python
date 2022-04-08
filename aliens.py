cities={
    'campo grande':{
        'country':'Brasil',
        'population':'1M',
    },
     
    'corumba':{
        'country':'Brasil',
        'population':'100K',
     },

    'aquidauana':{
        'country':'Brasil',
        'population':'50K',
    }
}
for k, v in sorted(cities.items()):
    print('\nCity ' + k.title())
    cept = v['country'] + ' ' + v['population']
    print(cept)
