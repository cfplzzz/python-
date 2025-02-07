#daydayupQ1.py
dayup=pow(1.001,365)
daydown=pow(0.999,365)
print("向上：{:.2f}".format(dayup))
print("向下：{:.2f}".format(daydown))
#daydayupQ2.py
dayfactor=0.005
dayup=pow(1+dayfactor,365)
daydown=pow(1-dayfactor,365)
print("向上：{:.2f}".format(dayup))
print("向下：{:.2f}".format(daydown))
#daydayupQ3.py
dayfactor=0.01
dayup=pow(1+dayfactor,365)
daydown=pow(1-dayfactor,365) 
print("向上：{:.2f}".format(dayup))
print("向下：{:.2f}".format(daydown))
#daydayupQ4.py #一年内工作日上升0.01，休息日下降0.01
dayup=1.0
dayfactor=0.01
for i in range(365):
    if i%7 in [6,0]:
        dayup=dayup*(1-dayfactor)
    else:
        dayup=dayup*(1+dayfactor)
print("工作日的力量：{:.2f}".format(dayup))
#daydayupQ5.py #一年内工作日达到多少努力才能和每天工作的达到一样效果
def dayUP(df):
    dayup=1
    for i in range(365):
        if i%7 in [6,0]:
            dayup=dayup*(1-0.01)
        else:
            dayup=dayup*(1+df)
    return dayup
dayfactor=0.01
while dayUP(dayfactor)<37.78:
    dayfactor+=0.001
print("工作日的努力参数是：{:.3f}".format(dayfactor))