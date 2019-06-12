import unittest,sys
from ApiLogin.Api_Login_page import Edu_login
from tool.openpyxl_fun import Excel_data
from data.fixed_parameter import excel_subpage,excel_testpath

class Api_login_set(unittest.TestCase):
    '''登录测试'''
    inexecution = 1
    def setUp(self):
        self.login=Edu_login()
        self.ed = Excel_data()

    @unittest.skipIf(inexecution !=1,'')
    def test_edu_login_1(self):
        '''登录成功'''
        testname =sys._getframe().f_code.co_name
        data = self.ed.edu_data(excel_testpath, excel_subpage,testname,1)
        print('test1',data)
        a =self.login.api_login(data,1)
        # self.assertAlmostEqual(a,'200')

    @unittest.skipIf(inexecution != 1, '')
    def test_edu_login_2(self):

        '''测试账号不能为空'''

        testname =sys._getframe().f_code.co_name
        testname = sys._getframe().f_code.co_name
        data = self.ed.edu_data(excel_testpath, excel_subpage, testname, 1)
        print('test2', data)
        a = self.login.api_login(data, 1)
        # self.assertAlmostEqual(a,'账号或密码不能为空')

    @unittest.skipIf(inexecution != 1, '')
    def test_edu_login_3(self):
        '''测试密码不能为空'''

        testname =sys._getframe().f_code.co_name
        testname = sys._getframe().f_code.co_name
        data = self.ed.edu_data(excel_testpath, excel_subpage, testname, 1)
        print('test3:', data)
        a = self.login.api_login(data, 1)
        # self.assertAlmostEqual(a,'账号或密码不能为空')

    @unittest.skipIf(inexecution != 1, '')
    def test_edu_login_4(self):
        '''测试账号不存在'''
        testname =sys._getframe().f_code.co_name
        testname = sys._getframe().f_code.co_name
        data = self.ed.edu_data(excel_testpath, excel_subpage, testname, 1)
        print('test4:', data)
        a = self.login.api_login(data, 1)
        # self.assertAlmostEqual(a,'密码错误')

    @unittest.skipIf(inexecution != 1, '')
    def test_edu_login_5(self):
        '''测试密码错误'''
        testname =sys._getframe().f_code.co_name
        testname = sys._getframe().f_code.co_name
        data = self.ed.edu_data(excel_testpath, excel_subpage, testname, 1)
        print('test5:', data)
        a = self.login.api_login(data, 1)
        # self.assertAlmostEqual(a,'密码错误')

if __name__=='__main__':
    unittest.main()