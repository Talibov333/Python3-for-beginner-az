isHot = True

if isHot:
    print('today is hotday')
print('Drink water')


# if bir isin olub olamsi ucun ist edilir
# yuxarida ishot= True (boolen deyiskenidir) yeni hava istidir
# boolen deyiskenler True ve False olur,yeni dogru ve yalnis
# netice butun printler gosterilecek
 

isHot = False

if isHot:
    print('today is hotday')
print('Drink water')

burda ise False oldugu ucun yalniz asagidaki print gosterilecek



ishot = False
iscold = True

if ishot:
    print('today is hot day')
    print('drink water more')
elif iscold:
    print('today is cold day')
    print('wear warm clothes')
else:
    print('today is normal day')

# yuxarida if elif else kodelarindan istfde edilmisdir
# bu kodlar if den basqa hec biri tekliklde istfade edile bilmez
# yalnz if ile istifade edilir

# burda havanin isti ve ya soyuq olamsindan asili olaraq if elif ve else
# kodlrndan ist edlb..burda havanin iscold=True deysikenin dogru oldugu ucun
# neticede onun altindaki print gosterilecek
# eger her iki deyisken False olsaydi yalniz else-n altindaki print gostrlck


ishot = False
iscold = True
issnow = True
israiny = False

if ishot:
    print('today is hot day')
    print('drink water more')
elif israiny:
    print('it is raining')
elif iscold:
    print('today is cold day')
    print('wear warm clothes')
elif issnow:
    print('it is snowing')
else:
    print('today is normal day')

# bu neticede yalniz elif iscold-un printi gorseneck cunku ilk onu gorur
# issnow deyiskenide True oldugu halda gorsenmiyecek
# butun true deyiskenleri gostermek ucun


ishot = False
iscold = True
issnow = True
israiny = True


if ishot:
    print('today is hot day')
    print('drink water more')
    
elif iscold:
    print('today is cold day')
    print('wear warm clothes')
    if israiny:
           print('it is raining')
    if issnow:
       print('it is snowing')
else:
    print('today is normal day')


# burda if altinda basqa bir if aciriq ve ya elif-in altnda basqa if
# yalniz fikir vermek lazimdirki her biri neyi bildirmek isteyirikse
# onun altinda olsun yeni iki bosluq mesafesi olsun soldan saga