#!/usr/bin/env python3

import unittest, random

def mkteststring(length):
    return "".join([chr(random.randint(32,126)) for i in range(length)])

class CoreStack(unittest.TestCase):
    """core stack functions: direct interations with []Stack.stack"""

    def setUp(self):
        stack.stack = []

    def test_inspect(self):
        """stack viewer"""
        result = stack.inspect()
        self.assertEqual(result, [])
        try:
            assert result == [], "fatal: failed to read the stack: not continuing"
        except AssertionError as error:
            raise RuntimeError(error) from AssertionError

    def test_inspect_fail(self):
        """this function can't fail testably."""
        pass

    def test_push(self):
        """put something on the stack"""
        stack.push(9)
        result = stack.inspect()
        self.assertEqual(result, [9])

    def test_push_fail(self):
        """this function can't fail testably."""
        pass

    def test_pushn(self):
        """put n things on the stack"""
        stack.pushn([i for i in range(100)])
        result = stack.inspect()
        self.assertEqual(result, [i for i in range(100)])

    def test_pushn_fail(self):
        """this function can't fail testably."""
        pass

    def test_pop(self):
        """pop from stack"""
        stack.push(9)
        stack.pop()
        result = stack.inspect()
        self.assertEqual(result, [])

    def test_pop_fail(self):
        """expect fail during pop"""
        with self.assertRaises(SystemExit):
            stack.pop()

    def test_popn(self):
        """pop n things from stack"""
        stack.pushn([i for i in range(1000)])
        result = stack.inspect()
        self.assertEqual(result, [i for i in range(1000)])

    def test_popn_fail(self):
        """expect failure during multipop"""
        with self.assertRaises(SystemExit):
            stack.popn()

    def test_copy(self):
        """copy the top of the stack"""
        stack.push(9)
        result = stack.copy()
        self.assertEqual(result, 9)

    def test_copy_fail(self):
        """expect failure during copy"""
        self.assertRaises(SystemExit, stack.copy())

    def test_copyn(self):
        """copy n items from the top of the stack and return a tuple"""
        stack.pushn([i for i in range(10)])
        result = stack.copyn(2)
        self.assertEqual(result, tuple(stack.inspect()[:-2]))

    def test_copyn_fail(self):
        """expect failure during multicopy"""
        with self.assertRaises(SystemExit):
            stack.copyn()

    def test_insert(self):
        """insert an item at an index"""
        stack.pushn([i for i in range(10)])
        stack.insert(5, 7)
        self.assertEqual(stack.inspect()[7], 5)

    def test_insert_fail(self):
        """expect failure during insertion"""
        self.assertRaises(mouse16.BadInternalCallException, stack.insert(9, 9))

    def test_insertn(self):
        """insert items at index n and up"""
        stack.pushn([i for i in range(10)])
        stack.insertn([2, 3, 4, 5], 2)
        self.assertEqual(stack.inspect()[2:6], [2, 3, 4, 5])

    def test_insertn_fail(self):
        """expect failure during multiple insertion"""
        self.assertRaises(mouse16.BadInternalCallException, stack.insertn([8, 4, 12], 16))
        with self.assertRaises(TypeError):
            stack.insertn(8, 16)

    def test_remove(self):
        """remove an item from an index"""
        stack.pushn([i for i in range(10)])
        stack.remove(5)
        lst = [i for i in range(10)]
        lst.remove(5)
        self.assertEqual(stack.inspect(), lst)

    def test_remove_fail(self):
        """expect failure during by-index removal"""
        with self.assertRaises(mouse16.BadInternalCallException):
            stack.remove(1)

    def test_index(self):
        """return a 1-indexed item from the end of the list"""
        stack.pushn(list(reversed([i for i in range(10)])))
        result = stack.index(7)
        self.assertEqual(result, stack.inspect()[-7])

    def test_index_fail(self):
        """expect failure during index operation"""
        with self.assertRaises(IndexError):
            stack.index(16)

    def test_clean(self):
        """clear the stack and return the old stack"""
        stack.pushn([i for i in range(10)])
        result = stack.clean()
        self.assertNotEqual(result, stack.inspect())

class Math(unittest.TestCase):
    """mathematical functions: proxied stack interactions, direct interaction with basic Python math operators"""

    def setUp(self):
        stack.clean()

    # addition

    def test_add_nums(self):
        """add numbers"""
        stack.pushn([4, 12])
        stack.add()
        self.assertEqual(stack.pop(), 16)

    def test_add_strs(self):
        """add strings"""
        stack.pushn(["cat", "dog"])
        stack.add()
        self.assertEqual(stack.pop(), "catdog")

    def test_add_numstr(self):
        """add a number to a string"""
        stack.pushn(["mouse", 16])
        stack.add()
        self.assertEqual(stack.pop(), "mouse16")
        stack.pushn([7, "9"])
        stack.add()
        self.assertEqual(stack.pop(), 16)

    def test_add_failure(self):
        """expect addition failure"""
        stack.pushn([{"this is a":"dictionary"}, ("this", "is", "a", "tuple")])
        self.assertRaises(mouse16.TypeWarning, stack.add())
        stack.pushn(["mouse", 16])
        self.assertNotEqual(stack.pop(), "mouse 16")

    # subtraction

    def test_sub_nums(self):
        """subtract numbers"""
        stack.pushn([2, 3])
        stack.sub()
        self.assertEqual(stack.pop(), -1)

    def test_sub_strs(self):
        """subtract strings"""
        stack.pushn([5, "1ll2ll3ll4ll5ll", "ll"])
        stack.sub()
        self.assertEqual(stack.pop(), "12345")

    def test_sub_numstr(self):
        """subtract a number from a string"""
        stack.pushn([4, "mouse16"])
        stack.sub()
        self.assertEqual(stack.pop(), "mou")
        stack.pushn(["20", 4])
        stack.sub()
        self.assertEqual(stack.pop(), 16)

    def test_sub_failure(self):
        pass

    # multiplication

    def test_mlt_nums(self):
        pass

    def test_mlt_strs(self):
        pass

    def test_mlt_numstr(self):
        pass

    def test_mlt_failure(self):
        pass

    # divmod

    def test_dmd_nums(self):
        pass

'''
class StackOps(unittest.TestCase):
    """stack operators: proxied []Stack.stack interaction through CoreStack"""
    pass

class Types(unittest.TestCase):
    """interactions between certain types and operators, and type-specific functions"""
    pass

class MathConst(unittest.TestCase):
    """tests of number-special functions (Python's Math library) and builtin constants"""
    pass

class Parsing(unittest.TestCase):
    """tests specific to syntax and the parser, but not the runner"""
    pass

class Runtime(unittest.TestCase):
    """variables, memory, function defs/calls, language features: reliant on all o the previous classes"""
    pass

class FailMe(unittest.TestCase):
    """things that should explicitly fail: zero division, for instance"""
    pass
'''

if __name__ == '__main__':
    try:
        import mouse16
    except ImportError:
        try:
            import mouse16hlink as mouse16
        except ImportError:
            print("stat: cannot stat 'mouse16.py': no such file or directory\nmodule for testing not found (must be named mouse16 in the current directory)")
            exit(1)

    stack = mouse16.Stack()

    mouse = mouse16.Mouse()

    mouse16._fromfile = True # make underflow raise SystemExit(4) for testing

    unittest.main()
