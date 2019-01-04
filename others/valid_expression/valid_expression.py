import re

"""
Language Spec

e = 
    | e + e
    | e - e
    | e * e
    | e / e
    | - e   단, double unary 금지
    | + e   단, double unary 금지
    | (e)
    | NUM

NUM =
    | NUMNUM    단, 0001 금지
    | NUM.NUM   단, 1.100000 금지
    | 0~9
"""
reNum = re.compile('([1-9][0-9]*([.][0-9]*[1-9])?)$|(0([.][0-9]*[1-9])?)$') # 숫자 규칙
#reOp = re.compile('(?P<left>.+)[+*\-/](?P<right>.+)') # 사칙연산 규칙, 사용하지않음
reOp = re.compile('[+*/-]')
reUnary = re.compile('(-|\+)(?P<inner>.+)') # 단항연산자 규칙
reBracket = re.compile('\((?P<inner>.+)\)') # 괄호 규칙
reDoubleUnary = re.compile('[+-][+-]') # double unary 규칙

def isValid(target):
    if reDoubleUnary.search(target): # double unary check
        return False

    if reNum.match(target):  # | NUM
        return True

    opIter = reOp.finditer(target)  # | e + e | e - e | e * e | e / e
    for cursor in opIter:
        left = target[0:cursor.start()]  # cursor.start() = 발견된 op의 위치
        right = target[cursor.start()+1:]
        if isValid(left) and isValid(right):
            return True

    unaryMatch = reUnary.match(target)  # | - e | + e
    if unaryMatch:
        if isValid(unaryMatch.group("inner")):
            return True

    bracketMatch = reBracket.match(target)  # | (e)
    if bracketMatch:
        if isValid(bracketMatch.group("inner")):
            return True

    return False



numTest = ["00","01","00.123","123.","1...1","123","123.123","10.10","0.123"]
for cursor in numTest:
    print(cursor, isValid(cursor))


expTest = ["1-(-1)","++1","+1","-1","1++1","1--1","((1)","((1))","(1-1)+(1+1-(3-3))"]
for cursor in expTest:
    print(cursor, isValid(cursor))

