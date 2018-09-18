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

"""
所以解决一个问题的步骤: 
1. concet inventory, 确定问题有多少个概念
2. refine ideas, 提炼想法
3. simple implementation, 实现一个简单的办法
4. back envelop, 初略的计算实现的耗时, 准确度等等
5. refine code, 继续提炼完善代码
"""