# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.

#definindo função
def is_leap(year):
    leap = False
    
    #só será bisexto se o ano for divisivel por 4 e não for divisivel por 100 OU se o ano for divisivel por 400
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0: 
        #se atender o if, mudar leap pra true
        leap = True 
    return leap

#input do ano
ano = int(input("digite um ano: "))

#testando função
print(is_leap(ano))