all_time = '1h 45m,360s,25m,30m 120s,2h 60s'
time_minutes = 0
for i in all_time.replace(',', ' ').split():
    if 'h' in i:
       time_minutes += int(i.replace('h', '')) * 60 
    elif 'm' in i:
        time_minutes += int(i.replace('m', ''))
    elif 's' in i:
        time_minutes += int(i.replace('s', ''))//60

print(time_minutes)