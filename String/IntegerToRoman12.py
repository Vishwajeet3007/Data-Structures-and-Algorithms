def integerToRoman(num):
    val = [
        1000,900,500,400,
        100,90,50,40,
        10,9,5,4,1
    ]
    syms = [
        'M','CM','D','CD',
        'C','XC','L','XL',
        'X','IX','V','IV','I'
        ]
    roman = ""
    for i in range(len(val)):
        while num >= val[i]:
            roman += syms[i]
            num -= val[i]
    return roman
num = 12345
print(integerToRoman(num))
num = 58
print(integerToRoman(num))
num = 3749
print(integerToRoman(num))
num = 2002
print(integerToRoman(num))
num = 1994
print(integerToRoman(num))