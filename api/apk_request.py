'''
封装接口请求发送
'''
import requests


class Request_Api:

    def __init__(self):

        # 登陆路径
        self.login_url = 'http://ihrm-test.itheima.net' + '/api/sys/login'
        # 添加、修改、查看、删除部门
        self.add_bumen_url = 'http://ihrm-test.itheima.net' + '/api/company/department'

    # 封装登陆接口
    def login_api(self,jsondata,headers):
        return requests.post(self.login_url,json=jsondata,headers=headers)

    # 封装添加部门接口
    def bumen_add_api(self,jsondata,headers):
        return requests.post(self.add_bumen_url,json=jsondata,headers=headers)

    # 封装修改部门接口
    def bumen_updata_api(self,jsondata,headers,id):
        # 修改部门路径
        updata = self.add_bumen_url + '/' + id
        return requests.put(updata,json=jsondata,headers=headers)

    # 封装查看部门接口
    def bumen_select_api(self,headers,id):
        # 查看部门路径
        select = self.add_bumen_url + '/' + id
        return requests.get(select,headers=headers)

    # 封装删除部门接口
    def bumen_delete_api(self,headers,id):
        # 删除部门路径
        delete = self.add_bumen_url + '/' + id
        return requests.get(delete,headers=headers)