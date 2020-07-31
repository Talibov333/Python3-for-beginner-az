         # ikili datalarin listlerde toplanmasi
     # asgda sinifin teleblrin adini ve ortalama statikasi listde gostrcy

# 1) bos students adinda list duzeldirk


students = []
notes = 0
tablenumber = 0

while True:
    fullname = input('enter your fullname or for exit(Q/q) ')
    if fullname == 'q' or fullname == 'Q':
        exit = input('are you sure? Y/N ')
        if exit == 'y' or exit == 'Y':
            print('have good time')
            break
        elif exit == 'n' or 'N':
            continue

    tablenumber += 1
    note = int(input('enter your idnumber: '))
    students += [[fullname,note]]

if tablenumber != 0:
    for i in range(len(students)):
        notes += students[i][1]
    value = notes/tablenumber
    print(*students)
    print('class degree',value)
