'''
12. Integer to Roman
https://leetcode.com/problems/integer-to-roman/
'''

# first try
def solution(num):
    
    collected = []
    place = 1 # 자릿수

    for n in str(num)[::-1]:
        rom_string = convert_digit(int(n), place)
        collected.insert(0, rom_string)
        place += 1
    return ''.join(collected)

def convert_digit(n, place):
    if place == 1:
        if n < 4:
            return (n // 1) * 'I'
        elif n == 4:
            return 'IV'
        elif 5 <= n < 9:
            return 'V' + (n % 5) * 'I'
        elif n == 9:
            return 'IX'
        elif n == 0:
            return 
    elif place == 2:
        if n < 4:
            return (n // 1) * 'X'
        elif n == 4:
            return 'XL'
        elif 5 <= n < 9:
            return 'L' + (n % 5) * 'X'
        elif n == 9:
            return 'XC'
        elif n == 0:
            return 
    elif place == 3:
        if n < 4:
            return (n // 1) * 'C'
        elif n == 4:
            return 'CD'
        elif 5 <= n < 9:
            return 'D' + (n % 5) * 'C'
        elif n == 9:
            return 'CM'
        elif n == 0:
            return 
    elif place == 4:
        return (n // 1) * 'M'
        

        
# better solution
def solution1(num):
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    res = ""
    for i, v in enumerate(values):
        res += (num//v) * numerals[i]
        num %= v
    return res

'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''

# 조건: 1 <= input < 4000
input = 1994
print(solution1(input))