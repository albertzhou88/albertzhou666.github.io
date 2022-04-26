price = input('Input price ')
price = float(price)

# if price > 1.0:
#     tax = 0.07
# else:
#     tax = 0

# output = f'Tax is {tax}'
# print(output)

country = input('Input your country ')
if country.lower() == 'canada':
    if price > 1.0:
        province = input('Input your province ')
        if province.lower() in ('alberta', 'nunavut', 'yukon'):
            tax_rate = 0.05
        elif province.lower() == 'ontario':
            tax_rate = 0.13
        else:
            tax_rate = 0.15
    else:
        tax_rate = 0
    tax = price * tax_rate
    output = f'Price is {price}. Tax rate is {tax_rate}. Tax is {tax}.'
    print(output)
else:
        print('Unknown tax')
