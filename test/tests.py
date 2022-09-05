import pytest
import re

def coerce(s: str):
    def fun(s1: str):
        if s1 == "true":
            return True
        if s1 == "false":
            return False
        return s1
    string = s
    try:
        string = int(s)
    except ValueError:
        try:
            string = float(s)
        except ValueError:
            string = fun(re.search('^\s*(.+?)\s*$', s)).group(1)
        return string
    except Exception as e:
        print("Error 101: coerce_file_crashed")

def the_function(help: str):
    the = {}
    try:
        valuesToAppend = re.findall('\n [-][^\s]+[\s]+[-][-]([^\s]+)[^\n]+= ([^\s]+)', help)
        for match in valuesToAppend:
            the[match[0]] = coerce(match[1])
        return the
    except Exception as e:
        print("Error 102: the_functino crashed",e)

# confirm this once
def test_eg_the():
    return True

def test_eg_sym():
    pairs = dict.fromkeys(["a","a","a","a","b","b","c"])
    sym = Sym()
    for key, value in pairs:
        sym.add(value)
    mode, entropy = sym.mid(), sym.div()
    entropy = {1000 * entropy} // 1 / 1000
    oo({mid = mode, div = entropy})
    assert mode == "a" and 1.37 <= entropy and <= 1.38




