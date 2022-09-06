import pytest
import re
import math
import random
class Num:
    '''
        Num summarize as stream of numbers
        Attributes:
            n: number of items seen
            at: column position
            name: column name
            _has: kept data
            lo: lowest seen
            hi: highest seen
            isSorted: tracks the status of sort
            c: column position
            s: column name
        '''

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
            print("Error 102: the_function crashed",e)
            
            
    def per(self, t, p):
        
            '''
                            Return the pth item from the sorted list 't'
                            Arguments:
                                p: Denotes index
                                t: Denotes sorted list
            '''
            p = math.floor(((p or 0.5) * len(t)) + 0.5)
            return t[math.max(1, math.min(len(t), p))]
        
    def o(self,t):
            '''
                            Generates a string from nested list
                            Arguments:
                                t: Denotes list of values
            '''

            if type(t) != list:
                return str(t)

            def show(self,k, v):
                if str(k).find('^_') == -1:
                    v = self.o(v)
                    return len(t) == 0 and format(':{} {}', k, v) or str(v)

            u = []
            index = 0
            dict_keys = list(t.keys())
            for key in dict_keys:
                u[index] = show(key, t[key])
            if len(t) == 0:
                u.sort()
            return '{' + ' '.join(str(item) for item in u) + '}'

    def oo(self,t):
            '''
                            Prints the string from o()
                            Arguments:
                                t: Denotes list of values
            '''
            print(self.o(t))
            return t