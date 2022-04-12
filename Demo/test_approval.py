from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


# 获取下拉框信息

def get_data():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('http://testoa.longtubas.com/login.aspx')

    # 登录OA 需要修改
    driver.find_element_by_id('txtUserID').send_keys('yinmeng1')
    driver.find_element_by_id('txtPassword').send_keys('a11111')
    driver.find_element_by_id('btnLogin').click()

    # 打开采购申请
    driver.find_element_by_id('upw200500').click()
    driver.find_element_by_id('upw200506').click()
    li = driver.window_handles
    driver.switch_to.window(li[-1])
    # 获取下拉框信息
    dic = {}
    data = []
    fenlei1 = Select(driver.find_element_by_class_name('od_category_main'))
    for i in fenlei1.options:
        fenlei1.select_by_visible_text(i.text)
        fenlei2 = Select(driver.find_element_by_class_name('od_category'))
        for j in fenlei2.options:
            if j.text != '-请选择-':
                data.append(j.text)
        dic[i.text] = data
        if dic[i.text]:
            pass
        else:
            del dic[i.text]
    li1 = []
    for i in dic:
        for j in dic[i]:
            t = (i, j)
            li1.append(t)
    return li1


class TestApproval:

    def setup(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('http://testoa.longtubas.com/login.aspx')

        # 登录OA 需要修改
        self.driver.find_element_by_id('txtUserID').send_keys('yinmeng1')
        self.driver.find_element_by_id('txtPassword').send_keys('a11111')
        self.driver.find_element_by_id('btnLogin').click()

        # 打开采购申请
        self.driver.find_element_by_id('upw200500').click()
        self.driver.find_element_by_id('upw200506').click()
        li = self.driver.window_handles
        self.driver.switch_to.window(li[-1])

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize(('pinlei', 'leixing'), get_data())
    def test_class(self, pinlei, leixing):

        # 填写采购申请
        self.driver.find_element_by_xpath(
            '//*[@id="form1"]/div[3]/div[3]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[1]/input').send_keys(
            '%s' % leixing)
        Select(self.driver.find_element_by_class_name('od_category_main')).select_by_visible_text('%s' % pinlei)
        Select(self.driver.find_element_by_class_name('od_category')).select_by_visible_text('%s' % leixing)
        self.driver.find_element_by_xpath(
            '//*[@id="form1"]/div[3]/div[3]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[3]/input').send_keys(
            '%s' % leixing)
        self.driver.find_element_by_xpath(
            '//*[@id="form1"]/div[3]/div[3]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[4]/input').send_keys(
            '%s' % leixing)
        # 数量
        self.driver.find_element_by_class_name('od_quantity').send_keys('1')
        self.driver.find_element_by_xpath(
            '//*[@id="form1"]/div[3]/div[3]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[6]/input').click()
        # 最晚到货日期
        self.driver.find_element_by_xpath(
            '//*[@id="form1"]/div[3]/div[3]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[6]/input').send_keys(
            '20211111')
        # 项目编号
        self.driver.find_element_by_xpath(
            '//*[@id="form1"]/div[3]/div[3]/table/tbody/tr[2]/td[2]/div/div[1]/div[4]/div[1]/input').send_keys('1')
        self.driver.find_element_by_xpath(
            '//*[@id="form1"]/div[3]/div[3]/table/tbody/tr[2]/td[2]/div/div[1]/div[4]/div[1]/input').click()
        sleep(1)
        self.driver.find_element_by_id('170402ZYW04').click()
        Select(self.driver.find_element_by_class_name('od_department_one')).select_by_visible_text('管理中心')
        Select(self.driver.find_element_by_class_name('od_department_two')).select_by_visible_text('财务部')
        Select(self.driver.find_element_by_class_name('od_department_three')).select_by_visible_text('资金部')
        self.driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div[4]/textarea').send_keys('%s' % leixing)
        self.driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div[5]/textarea').send_keys('%s' % leixing)
        self.driver.find_element_by_id('btnSave').click()
        sleep(1)
        # 获取属性文本进行断言
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name('iframe'))
        a = self.driver.find_element_by_xpath('//*[@id="divNext"]/span/label').text
        if pinlei in ['无形资产', 'IDC', '业务通讯', '网络/内容安全', '电子支付', '平台支付', '产品安全', '产品优化']:
            assert '商务支持组' in a
        else:
            assert '采购初审组' in a
