import requests

class Api_login_fun(object):

    #接口post操作传参方式
    def api_post(self,host_url,url,data,clom,*args,**kwargs):
        url="{}{}".format(host_url,url)
        #正常传参方式
        if clom == 1:
            
            # reques = requests.post(url=url,data=data,*args,**kwargs)
            reques=requests.request('post',url=url,data=data,*args,**kwargs)
        #上传图片或文件方式
        elif clom ==2:
            reques = requests.request('post',url=url, files=data, *args, **kwargs)

        return reques

    # 接口get操作传参方式
    def api_get(self,host_url,url,params,*args,**kwargs):

        url = '{}{}'.format(host_url,url)
        reques=requests.request('get',url=url,params=params,*args,**kwargs)

        return reques
