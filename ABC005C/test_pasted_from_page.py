#
from resolve import resolve
####################################
####################################
# 以下にプラグインの内容をペーストする
#  
import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        print('------------')
        print(out)
        print('------------')
        self.assertEqual(out, output)

        def test_case1(self):
            input = '''1
3
1 2 3
3
2 3 4'''
            output = '''yes
            '''
            self.assertIO(input, output)

        def test_case2(self):
            input = '''1
3
1 2 3
3
2 3 5'''
            output = '''no
            '''
            self.assertIO(input, output)

        def test_case3(self):
            input = '''1
3
1 2 3
10
1 2 3 4 5 6 7 8 9 10'''
            output = '''no
            '''
            self.assertIO(input, output)

        def test_case4(self):
            input = '''1
3
1 2 3
3
1 2 2'''
            output = '''no
            '''
            self.assertIO(input, output)

        def test_case5(self):
            input = '''1
5
1 3 6 10 15
3
4 8 16'''
            output = '''yes
            '''
            self.assertIO(input, output)



if __name__ == "__main__":
    unittest.main()
