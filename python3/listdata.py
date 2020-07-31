# list data tipi birden cox datani(informasiyani) saxlamaq ucun ist edilir

# data-rin listseklde gsterlmesnde on-ri str,int,float bir-de ist et olar 

list = [1,3,4,5,'salam','hi',2.5]
print(list)
print('***')
# netice [1,3,4,5,'salam','hi',2.5]
# eger []-bunsuz gost-k istkse print(*list)
# eger data-rin syainii bilmk istyrkse print(len(list))

list = [1,3,4,5,'salam','hi',2.5]
print(len(list))

# netice 7    == yeni 7 melumat var listin icinde

print('***')
# for dongusu ile listde olani gostmkolar
 
data = ["talibov", 'Fazail:', 27]
for info in data:
    print(info)
    
    
print('***')

# list3-de olan datalari ve tipleri gostrmk ucun 
# list3de olan datarin range ile i deyiskeni uzerinden
list3 = ['hi',2,4,'hey',2.7]
for i in range(len(list3)):
    print(list3[i],type(list3[i]))
    
print('***')

# string datani list-e cevirmek ve ayri ayri gostermek ucun
# adress adli 1 string deyskeni list5 listtipine cevirmek
adress = 'name:Fazail, surname:Talibov, age:27'
list5 = adress.split()
print(list5)
print('***')

# datalar uzerinde emeliyatlar
# yeni data elave etmek ucun
list5 += ['codemoon service',56,76.7]
print(*list5)
print('***')

# yalniz bir data eleva etmek ucun
list5.append('append')
print(list5)
print(*list5)  # without this []
print()
# silmek ucun sirasina gore
list5.pop(2)
print(list5)
print()
# datani silmek ucun adina gore
list5.remove(56)
list5 += ['codemoon service',56,76.7]
print(list5)
print('***')

# datani herflere bolmek ve elave etmek
list5.extend('codemoon')
print(list5)
print('********')
# netice 'c','o','d', ve axira kimi bele edir elave edir kohne qalir
# bu yolla yeni datada elave ede bilerik onuda heriflere bolub elv edck

# int ve ya float datada reqmlri kickden boyuye siralayacag
# herflerde ve ya cumleler

# datalari siralamaq
list6 = [10,6,7,4,2,1,-1,-3]
list6.sort()
print(list6)
print('********')
# tersine siralamaq ucun sort(reverse=True)
list6 = [10,6,7,4,2,1,-1,-3]
list6.sort(reverse=True)
print(list6)
print('********')
# strng data tipi ucun siralamq
list7 = ['talibov','emin']
list7.sort()
print(list7)
print('********')


# data kopyalamaq
# for dngden ist olnr
# bir bos list8 yardrq  snra list7 nin icrsden datlri kopyalrq
# sonra list8+=[copy] ile melumatlari alib donguye saliriq
# copy sozunun yerinde basqa sozlerden ist etmk olar
# daha sonra biz list8 basqa data eleva etsek list7 ye tesir etmir

list8 = []
for copy in list7:
    list8 += [copy]
print(list7,list8)

list8 += ['new data']
print(list7,list8)
print('********')


