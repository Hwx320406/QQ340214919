# -*- coding: UTF-8 -*-
from json import decoder
import json
# from tool.login_fun import Api_login_fun
from data.fixed_parameter import url1,host_url
from ApiLogin.api_login import Api_login

class TeacherList(Api_login):

    # 添加教师
    # def add_Teacher(self,data,clom,*args,**kwargs):
    def add_Teacher(self,data,clom,*args,**kwargs):


        execute=self.api_post(host_url=host_url,url=url1,data=data,clom=clom,cookies=self.cookies)
        TData=execute.text

        return TData

if __name__=='__main__':
    run =TeacherList()
    run.api_login()
    run.add_Teacher()