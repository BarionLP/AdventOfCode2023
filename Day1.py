import re as RegEx

digit_map = {
    'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}
def spelled_to_digit(digit: str) -> str:
    return digit_map.get(digit, digit)
    

pattern = r'(?:zero|one|two|three|four|five|six|seven|eight|nine|\d)'
pattern_rvs = r'(?:orez|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d)'
def solve(row: str) -> int:

    first = RegEx.findall(pattern, row)
    last = RegEx.findall(pattern_rvs, row[::-1])
    solution = spelled_to_digit(first[0])+spelled_to_digit(last[0][::-1])
    return int(solution)



if __name__ == '__main__':
    print(pattern)
    print(pattern_rvs)
    #print(solve("hczrldvxffninemzbhsv2two5eightwozfh"))
    
    result = 0
    with open("Day1String.txt", "r") as file:
        for line in file:
            result += solve(line.strip())
            

    print(result)
    