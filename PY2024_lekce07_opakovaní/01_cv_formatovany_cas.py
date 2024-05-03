import datetime

time_now = datetime.datetime.now()
print(time_now)
print(str(time_now)[:19])

formatovany_cas = time_now.strftime('%d.%m.%Y %H:%M:%S')
print(formatovany_cas)