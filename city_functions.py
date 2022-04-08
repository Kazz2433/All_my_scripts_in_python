def city_counrty(city, country, population=''):
    if population:
        fullname = city+', '+ country +' - '+population
    else:
        fullname = city+', '+ country
    return fullname.title()