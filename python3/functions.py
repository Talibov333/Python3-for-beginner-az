# eyni olan kodlari ve onu basqa yerlerde tekrar isletmemey ucun 
# funksiyalardan ist edilir. def (defined-tanitmaq sozunden) ile yazlr
# def name(): name yerine ne istese yaza bilirsiz () paremetler yazilir
# daha sonra bu programa aid isleri altinda yaziriq
# daha sonra yaratdigin name() ile onu istediyin yerde cagira bilerse
def GreatUser():
    print('hello there')
    print('this is a simple function for graeting user')
    
GreatUser()

print('****')

# () icersinde name,age(ad,yas yazmaq olar) paremetre tanidrq
# bu paremetleri {} icerisinde harda isletmey istyrkse orda qeyd edrk
# hmn prgrami bsqa-bsqa yrlrde name ve age-n yerine uygn ad ve yas qyd edrk

def UserName(name,age):
    print(f'hi {name}')
    print(f'you are {age} years old')
    
UserName('Emin','25')   # posianial arqument deyilir
UserName('Fazail','27')

print('****')


# eger paremetrler cox olarsa ve isteyirkse yalniz birini isledmk ucun

def FullName(name,surname):
    print(f'your name: {name}' )
    print(f'your surname:{surname}' )

    
FullName(name ='Fazail',surname ='Talibov',) 
 # buna keyword argumentleri deyilir
 # eger hem positional hem keyword isletmey isteyirkse 
 # 1c- positional olmalidi

     
    
def adressLine(name,country,city,postcode):
    print(f'hello mr:  {name}')
    print(f'welcome to  {country}')
    print(f'you are in {city} ')
    print(f'{city}-s post code is {postcode}')

adressLine('Fazail',country='Azerbaijan',city='Baku',postcode='1031')

print('\n')

# test 
# bir emailin dogru olub olmamisini funksiya ile yoxluyaq


email = 'Talibov.93f@gmail..com'

def emailvalid(email):
    if email.count('@') != 1:
        return False
    numbofdots = email.count('.', email.find('@'))
    if numbofdots != 1:
        return False
    return True
    
    
if emailvalid(email):
    print('your email is valid')
else:
    print('your email is invalid')


