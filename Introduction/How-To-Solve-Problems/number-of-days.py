def is_leap_year(year):
    return (year % 400 == 0) and (year % 100 != 0) and (year % 4 == 0)

def days_between_dates(year1, month1, date1, year2, month2, date2):
    days = 0
    years = year2 - year1
    days_list_leap = [31,29,31,30,31,30,31,31,30,31,30,31]
    days_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    if(years < 0):
        return None
    if(years == 0):
        year = year1 
        if (is_leap_year(year)):
            days += sum(days_list_leap[(month1-1):month2]) - (date1) - (days_list_leap[month2-1] - date2) 
        else:
            days += sum(days_list[(month1-1):month2]) - (date1) - (days_list[month2-1] - date2)
    else:
        for year in range(year1, year2):
            if (is_leap_year(year)):
                days += sum(days_list_leap[(month1-1):]) - (date1) 
            else:
                days += sum(days_list[(month1-1):]) - (date1)
        year = year2
        if (is_leap_year(year)):
            days += sum(days_list_leap[:month2]) - (days_list_leap[month2-1] - date2) 
        else:
            days += sum(days_list[:month2]) - (days_list[month2-1] - date2)
    return days 

print(days_between_dates(2013, 1, 1, 2013, 1, 31))