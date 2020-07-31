import models
from models import CelsiusToFaren

for celsius in range(-100,101):
    print(f'{celsius} santigrat {CelsiusToFaren(celsius):.4} farenhetdi')


""" modeller bir nece funksiyani ve ya classi ve s kimi kodlari bir
py file icerisine atb basqa bir py filenin icerisinde import etmekle ist ede bilerik
burda biz elave models.py yaradib funksiyalarimizi onun icersne atib halhazrki faylimzda
ist ede bilerik
elave olaraq uzun adlari qisaca as ile qisa adini yaza bilerik

 """
