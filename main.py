## Weekday From Date
# A small Python program to find the day of the week for a given date


date=int(input("Enter the date: "))
month=input("Enter the first 3 letter of month: ")
y1=int(input("Enter the first 2 digit of the year: "))     #y1=variable for first 2 digit of the year
y2= int(input("Enter the last 2 digit of the year: "))     #y2=variable for last 2 digit of the year

ly= y2//4  #ly=leap year

month_codes = {
    "jan": 0, "feb": 3, "mar": 3, "apr": 6,
    "may": 1, "jun": 4, "jul": 6, "aug": 2,
    "sep": 5, "oct": 0, "nov": 3, "dec": 5
}                                                   # use of dictionary instead of match case to store the codes

month_code = month_codes.get(month)

reminder=y1%4
#Calculation for century code(cc)
cc= 6-2*reminder                    


# Formula used to find the day code
day= (date+y2+ly+month_code+cc)%7     

match day:
    case 0:
        print("Sunday")
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
