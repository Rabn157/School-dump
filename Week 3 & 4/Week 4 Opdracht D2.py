import datetime

current_year = datetime.date.today().year
user_year = int(input('Vul het maximale jaar in: '))

while current_year <= user_year:
    if current_year % 4 == 0:
        print('Het is een schrikkeljaar', current_year)
        current_year += 1
    else:
        current_year += 1
    