year=int(input('enter the year'))
ryear=int(input('enter the ryear'))
month=(input('enter the month'))
rmonth=(input('enter the rmonth'))
date=int(input('enter the date'))
rdate=int(input('enter the rdate'))
if year==ryear:
    if month==month:
        if date==rdate:
            print('no fee')  
elif month>rmonth:
    if date==rdate:
        if year==year:
            print(30*(rmonth-month)*500)
elif date>rdate:
    if month==rmonth:
        if year==ryear:
            print(15*(rdate-date))
else:
    print('10000')                        
                
