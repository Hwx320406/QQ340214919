# -*- coding: UTF-8 -*-

from data.fixed_parameter import url,host_url
from tool.login_fun import Api_login_fun

# 登录EDU
cookies={}
class Api_login(Api_login_fun):
    def api_login(self):

        reques = self.api_post(clom=1,host_url=host_url ,url=url ,data={'username':'admin','password':'admin'})
        # global cookies
        cook = reques.headers['Set-Cookie']
        a = cook.split(';')
        b = a[1].split('=')
        pid = b[2]
        self.cookies = {
            'PHPSESSID':'{}'.format(pid)
        }
        return self.cookies

if __name__=='__main__':
    run =Api_login()
    run.api_login()
    print('这是cookies',cookies)