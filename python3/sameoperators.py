# Pythonda bir deyisken yazanda ona verilen deyere uygun bir id yaranir
# bu deyerin(deyiskene verilmis deyer)butun yerlderde eyni id sahib olur

name1 = 'Fazail'
print(id(name1))

name2 = 'Fazail'
print(id(name2))

# bu deysknlern adi ferqli olsda deyr 'Fazail' oldgu ucn eyni id-dediler

# bunu yoxlamaq ucun if ele
if id(name1) == id(name2):
    print('They have same id')
else:
    print('they have not same id')
# netice birinci print olacag 
    
    
    
    
    

"""   is ve is not operatorlari
yxarda biz deyerleri qarsilasdirdiq yeni id(name1) yazmasaq beraberlik olmazdi
 paremetrlerin beraberliyin yoxlamaq ucun is operatorundan ist edilir

beraber olmamisi ise is not 
"""

if name1 is name2:
    print('eyndi')

if name1 is not name2:
    print('eyni deyil')
    

"""  None operatoru
None operaotu yoxluq demekdir.funksiyalarda 
ve bir cox yerde bow bir deyer vermek istedikde
ist olunur
asgdaki misallara baxaq

"""
print('\n')

sample = None

if sample is None:
    print('sample deyeri bos bir deyerdi')
    
    
#  funksiyada islenmesi
# biz text deyerine eger bos olmasa hey sozunu goster dedik
# programi ise saldiqda text deyer olaraq None dedik ve hey sozunu gostermedi
    
def UserName(name:str, city=str, age=int,text='Hey'):
    print(f'hi {name} ')
    print(f'welcome to {city} ')
    print(f' do you have {age} years old??')
    if text is not None:
      print(text)
    
UserName('Fazail','Baku','28',None)


"""


 """
    
    




