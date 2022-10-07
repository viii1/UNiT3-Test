# import unittest
# class LearnTest(unittest.TestCase):
#     def myfunc(self):
#         pass
#     def test_fun_1(self):
#         pass
#     def test_fun_2(self):
#         pass 
# class AnotherTEst(unittest.TestCase):
#     def test_fun_1(self):
#         pass 
# if __name__=="__main__":
#     unittest.main()


















""" import unittest
def sum(a,b):
    return a+b

class SumTest(unittest.TestCase):
    def test_sumFunc_1(self):
        #arrange
        a=10
        b=20
        #act
        result=sum(a,b)
        #assert
        self.assertEqual(result,a+b)
    def test_sumFunc_2(self):
        #arrange
        a=10
        b=20
        #act
        result=sum(b,a)
        #assert
        self.assertEqual(result,b+a)
if __name__ =="__main__":
    unittest.main() """




















import unittest
def sum(a,b):
    return a+b

class SumTest(unittest.TestCase):
    def setUp(self):
        print("SetUp  called")
        self.a=10
        self.b=20
    def teardown(self):
        self.a= 0
        self.b= 0
        print("teardown called")
    def test_sumFunc_1(self):
        print("test 1 called")
        #act
        result=sum(self.a,self.b)
        #assert
        self.assertEqual(result,self.a+self.b)
    def test_sumFunc_2(self):
        print("test 2 called")
        #act
        result=sum(self.b,self.a) 
        #assert
        self.assertEqual(result,self.a+self.b)
if __name__ =="__main__":
    unittest.main()     





