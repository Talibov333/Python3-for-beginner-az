firstname = 'Fazail'
lastname = 'Talibov'
text = firstname +  " " + lastname + " is a coder "
print(text)


firstname = 'Fazail'
lastname = 'Talibov'
text =f'{firstname} {lastname} is a coder '
print(text)

firstname = 'Fazailsaaaaaaaaaasscdsd'
lastname = 'Talibovdddddddddddda'
text =f'{firstname:.1}.{lastname:.1} is a coder '
print(text)


binary = 1283737992
print(f'bu reqemin ikilik say siteminde yeri {binary:#b}')


num = 1237832940207379777733973749283
print(f'{num:,}')



name = input("enter your name  ")
msg1 = f'Xos Gelmisiz {name:.12}'
msg2 = f' {name:.12} xos oldu bize'
msg3 = ' saytdan zovq alin '
print(f' {msg1:^30} ')
print(f' {msg2:<30} ')
print(f' {msg3:>30} ')