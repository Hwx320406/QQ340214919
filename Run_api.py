import time , os  , unittest
from HTMLTestReportCN import HTMLTestRunner
from tool.Email import (sendEmail,
    get_new_report,
    email_account,
    email_host,
    email_port,
    email_pwd,
    email_to_account,
    email_to_account_list,
    email_time)


def run_edu():
    # api_dirpath = os.path.abspath(os.path.join(os.path.dirname(__file__), "./scripts"))
    # print(os.chdir())
    api_dirpath='./ApiTestSet'
    edu_testfile = unittest.defaultTestLoader.discover(api_dirpath,pattern='*_tc.py')
    time1 = time.strftime('%y%m%d %H%M%S')
    reportflie = ('./file_generalList/TestReports/'+'Api_'+time1+'.html')
    # tmpdir = os.path.abspath(os.path.join(os.path.dirname(__file__), reportflie))
    with open(reportflie,'w',encoding='utf-8') as api:
        runnet = HTMLTestRunner(stream=api,
                                title= 'EDU测试报告',
                                description='EDU系统UI界面自动化测试，更新到五月版本',
                                tester='老道',
                                verbosity= 2)
        runnet.run(edu_testfile)
    report = get_new_report()
    sendEmail(s_user=email_account,s_pwd=email_pwd,port=email_port,host=email_host,report_flie=report,
              to_user=email_to_account_list,subject='EDU自动化测试报告',body='各位领导，今天{}的报告已生成，请查阅'.format(email_time))
    print('邮件已发送')

if __name__=="__main__":
    run_edu()
    # run_test()