"""     Dictionary ( sozluk )
dictionry vasitesi ile biz datalari etrafli gostermek olur


"""

info = {'name':'Fazail','surname':'Talibov','age':28}
print(type(info))  # tipini gostermek ucun 
print(info)   # tam datani gostermek ucun
print(info['name'])   # yalniz name deyerini gostrmk ucun

# yeni data elave etmk ucun
info['city'] = 'Baku'
print(info) 

# dictda olmyan datani girmek istynde none dyrini verlmsi.sehv olmamasi ucn
#.get metdndan ist edilir var olan datani gostrir olmyni ise none edir

print(info.get('email'))   # email datasi olmdgi ucn none deyeri donecek

#  datanii update etmek 

info.update({'name':'Fezail','age':27})
print(info)

#   datani silmek ucun 

"""
# bu cur silmey datani tam silir ve sonradan o datani berpani etmek olmur
del info
del info['age']

# .pop ile silmek olur bu silmek usulu silmey istdymz datani 1 dyskn verib
sonradan ist ede bilerik
info.pop('age')
"""
info.pop('age')   # bir basa silmek
infopop = info.pop('age') # dyskene verib silmek
print(info)
print(infopop)  # silnmis datani gostermek ucun 


