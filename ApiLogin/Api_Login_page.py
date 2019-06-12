# -*- coding: UTF-8 -*-

from tool.login_fun import Api_login_fun
from data.fixed_parameter import url,host_url


class Edu_login(Api_login_fun):
    # 登录操作层

    def api_login(self,data,colm):

        request = self.api_post(host_url=host_url,url=url,data=data,clom=colm)
        a =request.text

        return a



if __name__=='__main__':
    run=Edu_login()
    run.api_login('jj','kk')