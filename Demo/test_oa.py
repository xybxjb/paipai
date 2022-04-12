import datetime
import shelve
from time import sleep

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.support.select import Select


class TestOA:

    db = shelve.open('cookies')

    # 初始化工作
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://testoa.longtubas.com/login.aspx')
        self.driver.implicitly_wait(10)
    def teardown(self):
        sleep(2)
        self.driver.quit()

    # 获取OA登录名
    def get_oaid(self):
        self.driver.find_element_by_xpath('//*[@id="welcome"]/td[1]/a').click()
        self.driver.switch_to.frame('hot')
        return self.driver.find_element_by_xpath('//*[@id="admindate"]/li[2]/span[1]').text

    # 使用cookie登录
    def use_cookie(self):
        for cookie in self.db['cookies']:
            self.driver.add_cookie(cookie)
        self.driver.get('http://testoa.longtubas.com')


    # 进入员工管理
    def go_to_employee_management(self):
        self.driver.find_element_by_xpath('//*[@onclick="showTwo(200000);"]').click()
        self.driver.find_element_by_id('upw405000').click()

    # 登录测试
    def test_login(self):
        uid = 'jiananliu'
        self.driver.find_element_by_id('txtUserID').send_keys('%s' % uid)
        self.driver.find_element_by_id('txtPassword').send_keys('a11111')
        self.driver.find_element_by_id('btnLogin').click()
        self.db['cookies'] = self.driver.get_cookies()
        assert uid in self.get_oaid()

    # 错误登录提示测试
    # @pytest.mark.parametrize(('un','pw'),[('',''),('123','123'),('jiananliu','123')])
    # def test_login_fail(self,un,pw):
    #     self.driver.find_element_by_id('txtUserID').send_keys('%s' % un)
    #     self.driver.find_element_by_id('txtPassword').send_keys('%s' % pw)
    #     self.driver.find_element_by_id('btnLogin').click()
    #     li = ['*用户名或密码不能为空','*用户名称不存在','*用户密码不正确']
    #     assert self.driver.find_element_by_id('txtlabzy').text in li

    # 登记人员测试
    @pytest.mark.parametrize('un',('测试脚本1','测试脚本2'))
    def test_register(self,un):
        self.use_cookie()
        self.go_to_employee_management()
