     # girilen datalarin listler sekilinde saxlanilmasi
   # as-ki misalda reqemleri vurb hasili ve vurulan ed-ri listde saxlycq
   
 # 1) numbs adinda bos list yaradrq
 # 2) ededlri hasili uc x adinda deyisken yaradib 1e beraber edirik
# egerbu dyskni yrdmasaq proqram hasili 0-a vuracag ve cvb 0 olacag
# bundan elave x-e 1den basqa dyr vere bilerik mes 2,3,4 
# mes x=2 olanda hasili 2ye vurub cvbi gostrck
 # 3) istfadciden neqeder reqem gireceyini count deyiskeni ile inputdan alirq
 # for dongusu ile countdan aln datani i deyisken ile aliriq
 # for dongusunun icrsden numb deyiskeni ile girilecek reqemleri inpt ile alirq
# {} bu isare vasitesi ile girilck reqemlrn sirasini gostrb
# .format metodu ile ancq count inputndan alinan reqmlri girmye icaze verir
# (i+1) ile girilecek reqmlerin siyahisi birden baslayacq
 # 4) numbs+=[numb] istfdcinin girdiyi reqmler numbs listine elve edirik
 # x*=numb girilen reqemleri 1-1ne vururuq
 # printlerle uugun hasili ve girlmis reqmleri list sekilinde gosterik

numbs = []
x = 2
count = int(input('nece reqem gireceksiz? => '))
for i in range(count):
    numb = int(input("{}.Reqemi girin ".format(i+1)))
    numbs += [numb]
    x *= numb
print('Reqemlerin hasili',x)
print('girilen reqemler',*numbs)



