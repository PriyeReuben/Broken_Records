from datetime import date


date_list = []

start = date(1945, 1, 1)
x = start.toordinal()
today = date.today()

int_to_date = date.fromordinal(x)


for i in range(710032, today.toordinal()):
    print(date.fromordinal(i))
    date_list.append(str(i))
print(len(date_list))