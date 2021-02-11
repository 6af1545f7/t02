# -*- coding: utf-8 -*-
"""
This is ...
"""

import sys
import logging

from t02 import __version__

__author__ = "6af1545f7"
__copyright__ = "6af1545f7"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def literals() :
    """Demonstrate literals.

    Returns:
      dict: r of all literal types
    """
    r = {'str' : "string",
         'multiline-str' : """multiline\nstring""",
         'raw-str': r'a raw\string',
         'booleans' : [True, False],
         'character' : chr(0xe4),
         'str-unicode' : 'u00ff\xE4\U000000E4',
         'characters' : '\n \f \r \b \t',
         'integer' : ['unlimited precision',
                      {'integer' : 42, 'hex' : 0xff, 'base2' : 0b111, 'oct' : 0o40}],
         'floating-point' : ['usually as C double', {'dou' : 3.14, 'exp' : 6.2e23}],
         'complex' : [3+4j, 3.0+4.0j, 3]}
    return r


def collection_literals() :
    """Demontrate expressions.

    Returns:
      dict: r of all literal types
    """

    r = {'list' : [0, 1, 'str', [1.1, 2.2], list('spam'), [], {}],
         'tuple' : (1, 2, 3),
         'dict' : {'name' : 'Chas',  'age' : 31},
         'dict1' : dict([('name', "Chas"), ('age', 31)]),
         'dict2' : dict(name='Chas', age=31),
         'dict3' : dict(zip('abc', [1, 2, 3])),
         'set' : [set('eggs'), {'s', 'p', 'a', 'm'}, frozenset(range(0, 5))],
         'set1' : set(["one", "two"])}
    return r


def expressions() :
    """Demontrate expressions.

    Returns:
      dict: r of all
    """
    x = None
    y = 0
    r = {'undefined' : [x, y],
         'list' : [0, 1, 2, 3],
         'get(key)' : [dict(list=[1, 2, 3], val=2).get('list')],
         'isinstance' : isinstance([0, 1, 2, 3], type([]))}
    """:namespace-keyword {:keyword "cheese" ::ns-keyword "there"}
    :quote ["(quote x) or 'x'" (quote x)]
    :symbol ["(symbol? (quote x))" (symbol? (quote x))]
    """
    return r


def deconstruct():
    """Demonstrate deconstruction:
    - vector and map, with '_' (gaps) and ':rest';
    - setting symbol with ':as';
    - 'del' deletes symbol or one or more elements in a collection;
    - ':unknown' is not working.

    Returns:
      dict: r of all
    """
    p = [0, 1, 'str', [1.1, 2.2], list('spam'), [], {}]
    r1 = {'input' : p,
          'first' : p[0],
          'last' : p[-1],
          'indexed' : [p[1], p[-2]],
          'sliced' : [p[2:], p[1:4:2], p[:-3]],
          'rest' : [p[4:]]}
    r2 = {'input' : r1,
          'indexed' : [r1['rest']]}
    del p[2]
    r3 = {'del 2nd element' : p}
    del p[1:4:2]
    r3.update({'del range' : p})
    r3.update({'del symbol' : 'no longer defined'})
    return {'sequence' : r1, 'key' : r2, 'del' : r3}


def def_required(a, *b, c) : return [a, b, c]


def def_optional(a, *, c=None) : return [a, c]


def def_annot(a: 99, b: 'spam' = None) -> float: return a


def def_lambda(n): return lambda a : a*n


def function() :
    """ Demonstrate 'def'
    - required and optional arguments;
    - annotation;
    - lamdba.

    Returns:
     dict: r of all
    """
    double = def_lambda(2)
    triple = def_lambda(3)
    r = {'required' : def_required(1, 2, c=3),
         'optional' : [def_optional(1), def_optional(1, c='spam')],
         'annotations' : [def_annot(88), def_annot.__annotations__],
         'lambda' : [double(10), triple(10)]}
    return r


def condition() :
    """ Demonstration of if ... elif ... else:
    - on Boolean conditions;
    - on empty vector, '[]';
    - bool(x)' for various x.

    Returns:
     dict:
    """
    if True :
        c11 = 'if True'
    if False :
        c12 = 'if True'
    else :
        c12 = 'else'
    if False :
        c13 = 'if True'
    elif 1 == 1 :
        c13 = 'elif 1 == 1'
    c21 = '[] if is not True'
    if [] :
        c21 = '[] if'
    else :
        c22 = '[] else'
    r = {'c1' : [c11, c12, c13], 'c2' : [c21, c22],
         'bool(False)' : [bool(False), bool([]), bool(None)],
         'bool(True)' : [bool(True), bool(c11)]
         }
    return r


def loop_while() :
    """ Demonstration of while ... else on counter.

    Returns:
     dict:
    """
    c11 = []
    while len(c11) < 3 :
        c11.append(len(c11)+1)
    else :
        c12 = 'else not used'
    c21 = 'while loop not used'
    while False :
        c21 = 'while loop not used'
    else :
        c22 = 'else triggered'
    r = {'while' : [c11, c12], 'else' : [c21, c22]}
    return r


def loop_for() :
    """ Demonstration of:
    - 'for ... else';
    - 'pass'.

    Returns:
     dict:
    """
    c11 = []
    c12 = 'else not triggered'
    for x in range(3) :
        c11.append(x+1)
    else :
        pass
    r = {'for' : [c11, c12]}
    return r


def gen_sq(n) :
    for i in range(n) :
        yield i**2


"""
def gen_sq2(n) :
    for i in range(n) :
        if i > 4 :
            raise StopIteration()
        else :
            yield i**2
"""


def generator() :
    """ Demonstration of a generator, which returns an iterator:
    - 'yield', which is compiled as a generator and lazy-evaluates;
    - 'close()' to be done.

    Returns:
    dict:
    """
    c11 = gen_sq(3)
    c21 = []
    for x in gen_sq(3) :
        c21.append(x)
    r = {'yield list' : list(c11),
         'for on iterator' : c21}
    return r


def iterator() :
    """ Demonstration of iterators:
    - 'iter' and 'next' on str and keys in dict;
    - using 'items' to get key-value pairs from dict.

    Returns:
    dict:
    """
    i1 = iter('abcd')
    d1 = {'a' : 1, 'b' : 2}
    i2 = iter(d1)
    i3 = []
    for k, v in d1.items():
        i3.append([k, v])
    r = {'str' : [next(i1), next(i1), 'etc'],
         'key' : [next(i2), next(i2), 'etc'],
         'key value' : i3}
    return r


def seqs_lib() :
    """ Demonstration of list comprehension expressions:
    - 'for' and 'range' compared with 'map' on a function or lambda;
    - conditional comprehension expression and 'filter';
    - comprehension expression for a set;
    - 'cons' equivalent.

    Returns:
    dict:
    """
    f1 = []
    for i in filter((lambda x: x % 2 == 0), range(5)) :
        f1.append(i)
    l1 = []
    for k, v in {x: x * x for x in range(4)}.items():
        l1.append([k, v])
    l2 = [1, 2, 3]
    l2.insert(0, 99)
    r = {'map' : {'for' : list([ord(x) for x in 'spam']),
                  'map-fn' : list(map(ord, 'spam')),
                  'range' : list([x**2 for x in range(5)]),
                  'map-lambda' : list(map((lambda x: x**2), range(5)))},
         'filter' : {'range-cond' : list([x for x in range(5) if x % 2 == 0]),
                     'filter' : f1},
         'set' : list({x * x for x in range(4)}),
         'dict' : l1,
         'cons' : l2
         }
    return r


def evaluation() :
    """ Demonstration of:
    - 'eval' on a string.

    Returns:
    dict:
    """
    s = 'list([ord(x) for x in \'spam\'])'
    r = {'eval' : eval(s)}
    return r


def stack() :

    s = ['a', 'b']
    s0 = s
    s.append('c')
    s1 = s
    s2 = s.pop()
    r = {'stack-list' : {'start' : s0, 'push (FIXME)' : s1, 'pop' : s2, 'end' : s}}
    return r


def lang() :
    """Test module.

    Returns:
      dict: r of all returns in file
    """
    r = {'literals' : literals(),
         'collection_literals' : collection_literals(),
         'expressions' : expressions(),
         'deconstruct' : deconstruct(),
         'function' : function(),
         'condition' : condition(),
         'loop_while' : loop_while(),
         'loop_for' : loop_for(),
         'generator' : generator(),
         'iterator' : iterator(),
         'seqs_lib' : seqs_lib(),
         'evaluation' : evaluation(),
         'stack': stack()}
    return r
