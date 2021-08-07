duration = int(input('Введите промежуток времени: '))
hours = duration // 3600
minutes = (duration // 60) % 60
seconds = duration % 60

if duration < 60:
    print(seconds, 'сек')

elif duration >= 60 and duration < 3600:
    print('{} мин {} сек'.format(minutes, seconds))

elif duration >= 3600 and duration < 86400:
    print('{} час {} мин {} сек'.format(hours, minutes, seconds))
    
else:
    print('Вы ввели слишком большой промежуток.')
