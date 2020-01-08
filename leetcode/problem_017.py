'''
Letter combinations of a Phone number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''


def solution(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    interpret_digit = {
        '1': '',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        '0': ' '}

    all_combinations = [''] if digits else []

    for digit in digits:
        current_combinations = list()

        for letter in interpret_digit[digit]:
            
            for combination in all_combinations:
                current_combinations.append(combination + letter)
        
        all_combinations = current_combinations
    
    return all_combinations


input = "23"
print(solution(input))