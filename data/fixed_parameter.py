import os
#登录环境地址
host_url ='http://localhost'
# 登录参数
# 登录测试excel路径
# excel_testpath ='../file_generalList/Excel_TestSet/edu_login_v01.xlsx'
excel_testpath= os.path.abspath(os.path.join(os.path.dirname(__file__), '../file_generalList/Excel_TestSet/edu_login_v01.xlsx'))
# 登录测试excel子页
excel_subpage ='Login'
# 登录接口地址
url = '/admin.php?m=mgr/admin.chklogin&ajax=1'

# 教师列表
# 登录测试excel子页
excel_subpage1 ='addTeacher'
# 添加教师接口地址
url1='/admin.php?m=mgr/member2.saveMemberInfo&id='