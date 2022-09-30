CONV_TABLE = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))

def arab_to_roman( number ):
   if number <= 0: return ''

   ret = ''
   for arab, roman in CONV_TABLE:
       while number >= arab:
           ret += roman
           number -= arab

   return ret

print(arab_to_roman(4999))