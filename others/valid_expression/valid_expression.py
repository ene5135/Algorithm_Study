import re

"""
Language Spec

e = 
    | e + e
    | e - e
    | e * e
    | e / e
    | - e   ��, double unary ����
    | + e   ��, double unary ����
    | (e)
    | NUM

NUM =
    | NUMNUM    ��, 0001 ����
    | NUM.NUM   ��, 1.100000 ����
    | 0~9
"""
reNum = re.compile('([1-9][0-9]*([.][0-9]*[1-9])?)$|(0([.][0-9]*[1-9])?)$') # ���� ��Ģ
#reOp = re.compile('(?P<left>.+)[+*\-/](?P<right>.+)') # ��Ģ���� ��Ģ, �����������
reOp = re.compile('[+*/-]')
reUnary = re.compile('(-|\+)(?P<inner>.+)') # ���׿����� ��Ģ
reBracket = re.compile('\((?P<inner>.+)\)') # ��ȣ ��Ģ
reDoubleUnary = re.compile('[+-][+-]') # double unary ��Ģ

def isValid(target):
    if reDoubleUnary.search(target): # double unary check
        return False

    if reNum.match(target):  # | NUM
        return True

    opIter = reOp.finditer(target)  # | e + e | e - e | e * e | e / e
    for cursor in opIter:
        left = target[0:cursor.start()]  # cursor.start() = �߰ߵ� op�� ��ġ
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
