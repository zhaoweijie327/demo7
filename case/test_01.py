import unittest

from parameterized import parameterized

import app
from api.apk_request import Request_Api


from utils import pathfile


class Test_Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 调用apk_request模块里的Request_Api类
        cls.api = Request_Api()

    # 登陆接口方法
    @parameterized.expand(pathfile(app.BATH_PATH + '/data/data_json.json','login'))
    def test_01_login(self,mobile,password,message):
        data = {"mobile":mobile,"password":password}
        hearers = {"Content-Type":"application/json"}
        json_lingpai = self.api.login_api(data,hearers)

        # 获取令牌
        token = "Bearer " + json_lingpai.json().get("data")
        app.HEADERS = {"Content-Type":"application/json",'Authorization':token}
        # 断言
        self.assertIn(message,json_lingpai.json().get("message"))

    # 添加部门接口方法
    @parameterized.expand(pathfile(app.BATH_PATH + '/data/data_json.json','add_bumen'))
    def test_02_add(self,name,code,manager,introduce,message):
        data =  {"name":name,
                "code":code,
                "manager":manager,
                "introduce":introduce}
        json_data = self.api.bumen_add_api(data,app.HEADERS)

        # 获取id
        app.ID = json_data.json().get("data").get('id')
        # 断言
        self.assertIn(message,json_data.json().get("message"))

    # 修改部门接口方法
    @parameterized.expand(pathfile(app.BATH_PATH + '/data/data_json.json','updata_bumen'))
    def test_03_updata(self,name,code,manager,introduce,message):
        data =  {"name":name,
                "code":code,
                "manager":manager,
                "introduce":introduce}
        json_data = self.api.bumen_updata_api(data,app.HEADERS,app.ID)

        # 断言
        self.assertIn(message,json_data.json().get("message"))

    # 修改部门接口方法
    def test_04_select(self):
        self.api.bumen_select_api(app.HEADERS,app.ID)

    # 修改部门接口方法
    def test_05_delete(self):
        self.api.bumen_delete_api(app.HEADERS,app.ID)