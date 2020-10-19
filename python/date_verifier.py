# Date Verification Module


def leap_year(a):
    b = int(a[:4])
    if(b%100 == 0):
        if(b%400 == 0):
            return True
        else:
            return False
    elif(b%4 == 0):
        return True
    else:
        return False

def month_verify(a):
    b = a[5:7]
    if(int(b) in range(1,13)):
        if(b in "01 03 05 07 08 10 12".split()):
            return 'odd'
        elif(b in "04 06 09 11".split()):
            return 'even'
        else:
            return "feb"
    else:
        return "Month can only be in range 1 to 12 including 12\n"
    
def date_verify(a):
    b = int(a[8:])
    if(b not in range(1,32)):
        return "The maximum range of date is from 1 to 31 including 31\n"
    elif(month_verify(a) == 'odd'):
        if(b <32):
            return True
        
    elif(month_verify(a) == 'even'):
        if(b < 31):
            return True
        else:
            return "The Month You selected Can Only contain 30 days\n"
        
    else:
        if(leap_year(a)):
            if(b < 30):
                return True
            else:
                return "In a leap year Feb only contains 29 days"
        else:
            if(b < 29):
                return True
            else:
                return "In a Non-Leap year Feb only contains 28 days\n"

def verify(a): #Date in YYYY/MM/DD format
    if(month_verify(a) in ['odd', 'even', 'feb']):
        if(date_verify(a) == True):
            return True
        else:
            return date_verify(a)
    else:
        return month_verify(a)

def date_input(): ## Needed to be Recoded also at Line 150 Employee_end
    a = input('Enter the Year\n')
    if(a.isdigit()):
        b = input('Enter the Month\n')
        if(b.isdigit()):
            if(len(b) == 1):
                b = '0' + b
            c = input('Enter The Date\n')
            if(c.isdigit()):
                if(len(c) == 1):
                    c = '0' + c
                if(verify(a + '/' + b + '/' + c) == True):
                    return (True, a + '/' + b + '/' + c)
                else:
                    return (False, verify(a + '/' + b +'/' + c))

print(date_input()) # Further  Computation with the Date (as index 1 element)
