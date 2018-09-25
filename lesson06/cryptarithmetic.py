# coding=utf-8
from __future__ import division
import string, re, itertools

def solve(formula):
    for f in fill_in(formula):
        if (valid(f)): 
            return f

def fill_in(formula):
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    for digits in itertools.permutations("0123456789", len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)


def valid(f):
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError: 
        return False

summary = """
所以解决一个问题的步骤: 
1. concet inventory, 确定问题有多少个概念
2. refine ideas, 提炼想法
3. simple implementation, 实现一个简单的办法
4. back envelop, 初略的计算实现的耗时, 准确度等等
5. refine code, 继续提炼完善代码
"""

def compile_word(word):
    if word.isupper():
        terms = [('%s*%s' % (10**i, d)) 
                for (i, d) in enumerate(word[::-1]) ]
        return '(' + '+'.join(terms) +')'
    else:
        return word

def faster_solve(formula):
    f, letters = compile_formula(formula, True)
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
        try:
            if f(*digits) is True:
                table = string.maketrans(letters, ''.join(map(str, digits)))
                print table
                return formula.translate(table)
        except ArithmeticError:
            print 'error happens'
            pass


def compile_formula(formula, verbose= False):
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    params = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    f = 'lambda %s: %s' % (params, body)
    if verbose: print f
    return eval(f), letters


print faster_solve("TWO+TWO == FOUR")

