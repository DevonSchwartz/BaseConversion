import string


def dec_to_binary(dec):
    if '.' not in str(dec):
        dec = str(dec)
        dec += '.0'
        float(dec)

    num_af_dec, num_bef_dec  = str(dec).split('.')
    num_af_dec = int(num_af_dec)
    num_bef_dec = int(num_bef_dec)



    binary = ''
    binary_1 = ''
    count = 0
    count_1 = 0
    lst_of_num_af = []
    lst_of_num_bef = []
    while count >= 0:

        i = 2 ** count
        lst_of_num_af.append(i)
        if 2 ** (count + 1) > num_af_dec:
            break
        count += 1

    while count_1 >= 0:

        i = 2 ** count_1
        lst_of_num_bef.append(i)
        if 2 ** (count_1 + 1) > num_bef_dec:
            break
        count_1 += 1
    lst_of_num_af = lst_of_num_af[::-1]
    lst_of_num_bef = lst_of_num_bef[::-1]


    total_1 = num_af_dec
    total_2 = num_bef_dec
    print (lst_of_num_bef)

    for i in range(0,len(lst_of_num_af)):
        if total_1 >= lst_of_num_af[i]:
            total_1 -= lst_of_num_af[i]
            binary += '1'
        elif total_1 < lst_of_num_af[i]:
            binary += '0'

    for i in range(0,len(lst_of_num_bef)):
        if total_2 >= lst_of_num_bef[i]:
            total_2 -= lst_of_num_bef[i]
            binary_1 += '1'
        elif total_2 < lst_of_num_bef[i]:
            binary_1 += '0'

    return binary + '.' + binary_1



# dec = eval(input('Dec:'))
# print (dec_to_binary(dec))

def dec_to_base(dec,base):
    number_af = ''
    number_bef = ''
    count = 0
    count_1 = 0
    alpha = string.ascii_uppercase

    if ('.') not in str(dec):
        dec = str(dec)
        dec += '.0'
        dec = float(dec)

    num_af_dec,num_bef_dec = str(dec).split('.')
    num_af_dec = int(num_af_dec)
    num_bef_dec = int(num_bef_dec)



    letters = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}

    for i in range(0,len(alpha)):
        letters[i + 10] = (alpha[i])
    dividend_af = num_af_dec
    dividend_bef = num_bef_dec


    while count >= 0:
        quotient_af = int(dividend_af/base)
        remainder_af = dividend_af % base
        dividend_af = quotient_af
        character = letters[remainder_af]
        number_af += character
        if count >=1 and quotient_af < base:
            quotient_af = int(dividend_af/base)
            remainder_af = dividend_af % base
            dividend_af = quotient_af
            character = letters[remainder_af]
            number_af += character
            break
        count += 1

    while count >= 0:
        quotient_bef = int(dividend_bef/base)
        remainder_bef = dividend_bef % base
        dividend_bef = quotient_bef
        character = letters[remainder_bef]
        number_bef += character
        if count_1 >=1 and quotient_bef < base:
            quotient_bef = int(dividend_bef/base)
            remainder_bef = dividend_bef % base
            dividend_bef = quotient_bef
            character = letters[remainder_bef]
            number_bef += character
            break
        count_1 += 1
    number_af = number_af[::-1]
    for i in number_af:
        index = number_af.index(i)
        if number_af[index] != '0':
            break
        number_af = number_af[(index + 1):len(number_af)]


    return number_af + '.' + number_bef


decimal = eval(input('What decimal would you like to convert: '))
base = eval(input('What base would you like to convert it to?: '))
amount = dec_to_base(decimal,base)
print (dec_to_base(decimal,base))
