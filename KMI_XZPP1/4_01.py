import re
test_input = input('Zadej římské číslo: ')

vzor="(^M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

roman_tuples = (('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000))

test = re.search(vzor, test_input)
result = 0
if test is not None:
    for num in test.groups():
        i = 0
        sub_res = 0
        for char in num:
            for roman in roman_tuples:
                if char == roman[0]:
                    value = roman[1]
            if i > 0 and value > sub_res:
                sub_res = value - sub_res
            else:
                sub_res += value
            i += 1
        result += sub_res
    
    print(f'Římské číslo {test_input} je {result}')
else:
    print(f'Řetězec {test_input} není římské číslo.')
