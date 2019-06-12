import unittest,sys
from po.addTeacher import TeacherList
from tool.openpyxl_fun import Excel_data
from data.fixed_parameter import excel_subpage1,excel_testpath
from tool.eduMySQL import edu_pyMySql


class Api_add_teacher(unittest.TestCase):
    '''教师列表'''
    inexecution = 1
    def setUp(self):
        self.at=TeacherList()
        self.ed=Excel_data()
        self.at.api_login()



    #添加教师
    @unittest.skipIf(inexecution != 11, '')
    def test_add_teacher_1(self):
        '''添加教师成功'''
        edu_pyMySql('delete from xsmart_users where username="123456789"')
        testname=sys._getframe().f_code.co_name
        data=self.ed.edu_data(excel_testpath,excel_subpage1,testname,2)
        a=self.at.add_Teacher(data,1)
        a1 =a.split(',')
        b=list()
        
        print(b[0])
        print(b[1])
        self.assertAlmostEqual(a['info'],'保存成功')

    @unittest.skipIf(inexecution != 11, '')
    def test_add_teacher_2(self):
        '''账号已存在，添加教师失败'''
        testname=sys._getframe().f_code.co_name
        data=self.ed.edu_data(excel_testpath,excel_subpage1,testname,2)
        print('username2值是：',data['username'])
        a=self.at.add_Teacher(data,1)
        # self.assertAlmostEqual(a,'保存失败')

    @unittest.skipIf(inexecution != 11, '')
    def test_add_teacher_3(self):
        '''账号不能为空，添加教师失败'''
        testname=sys._getframe().f_code.co_name
        data=self.ed.edu_data(excel_testpath,excel_subpage1,testname,2)
        print('username3值是否为空：',data['username'])
        a=self.at.add_Teacher(data,1)
        # self.assertAlmostEqual(a,'保存失败')

    @unittest.skipIf(inexecution != 11, '')
    def test_add_teacher_4(self):
        '''email不能为空，，添加教师失败'''
        testname=sys._getframe().f_code.co_name
        data=self.ed.edu_data(excel_testpath,excel_subpage1,testname,2)
        print('email4值是否为空：',data['email'])
        a=self.at.add_Teacher(data,1)
        # self.assertAlmostEqual(a,'保存失败')

    @unittest.skipIf(inexecution != 11, '')
    def test_add_teacher_5(self):
        '''email格式不对，，添加教师失败'''
        testname=sys._getframe().f_code.co_name
        data=self.ed.edu_data(excel_testpath,excel_subpage1,testname,2)
        print('email5值是：', data['email'])
        a=self.at.add_Teacher(data,1)
        # self.assertAlmostEqual(a,'保存失败')

    @unittest.skipIf(inexecution != 11, '')
    def test_add_teacher_6(self):
        '''phone不能为空，，添加教师失败'''
        testname=sys._getframe().f_code.co_name
        data=self.ed.edu_data(excel_testpath,excel_subpage1,testname,2)
        print('phone6值是否为空：', data['phone'])
        a=self.at.add_Teacher(data,1)
        print(a)
        self.assertAlmostEqual(a['info'],'保存失败')

    @unittest.skipIf(inexecution != 11, '')
    def test_add_teacher_7(self):
        '''phoen格式不正确，，添加教师失败'''
        testname=sys._getframe().f_code.co_name
        data=self.ed.edu_data(excel_testpath,excel_subpage1,testname,2)
        print('phone7值是：', data['phone'])
        a=self.at.add_Teacher(data,1)
        # self.assertAlmostEqual(a,'保存失败')

    @unittest.skipIf(inexecution != 11, '')
    def test_add_teacher_8(self):
        '''账号格式不正确，，添加教师失败'''
        testname=sys._getframe().f_code.co_name
        data=self.ed.edu_data(excel_testpath,excel_subpage1,testname,2)
        print('username8值是：',data['username'])
        a=self.at.add_Teacher(data,1)
        # self.assertAlmostEqual(a,'保存失败')

if __name__=='__main__':
    unittest.main()
