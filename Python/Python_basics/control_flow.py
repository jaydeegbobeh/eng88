customer_age = 15

if customer_age <= 12:
    print('U, PG and 12 films are available')
elif customer_age <= 15:
    print('U, PG, 12 and 15 films are available')
else:
    print('all films are available')


time_of_day = 20

if time_of_day > 5 and time_of_day < 12:
    print('Good morning')
elif time_of_day > 12 and time_of_day < 18:
    print('Good afternoon')
else:
    print('Good evening')