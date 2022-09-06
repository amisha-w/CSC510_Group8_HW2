import pytest
import re

def test_eg_the():
    oo(the)
    assert True

def test_eg_sym():
    pairs = dict.fromkeys(["a","a","a","a","b","b","c"])
    sym = Sym()
    for key, value in pairs:
        sym.add(value)
    mode, entropy = sym.mid(), sym.div()
    entropy = {1000 * entropy} // 1 / 1000
    oo({mid = mode, div = entropy})
    assert mode == "a" and 1.37 <= entropy and <= 1.38




