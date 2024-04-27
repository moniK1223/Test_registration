# import time
# import pytest
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# @pytest.fixture(scope='class')
# def _drivers():
#     driver = webdriver.Chrome(options=opts)
#     driver.get('https://demowebshop.tricentis.com/')
#     time.sleep(2)
#     yield driver
#     driver.close()
#
# ## _drivers --> driver = webdriver.Chrome(options=opts)
#
# class TestDemoRegister:
#
#     def test_click_register(self, _drivers):        ## _drivers --> driver=webdriver.Chrome(options=opts)
#         _drivers.find_element('xpath', '//a[text()="Register"]').click()
#         time.sleep(2)
#
#     def test_gender_btn(self, _drivers):            ## _drivers --> driver
#         _drivers.find_element('xpath', '//input[@id="gender-female"]').click()
#
#     def test_firstname(self, _drivers):
#         _drivers.find_element('xpath', '//input[@id="FirstName"]').send_keys('Megha')
#
#     def test_lastname(self, _drivers):
#         _drivers.find_element('xpath', '//input[@id="LastName"]').send_keys('SriShankar')
#
#     def test_register_email(self, _drivers):
#         _drivers.find_element('xpath', '//input[@id="Email"]').send_keys('meghashankar@gmail.com')
#
#     def test_register_pwd(self, _drivers):
#         _drivers.find_element('xpath', '//input[@id="Password"]').send_keys('megha@12345')
#
#     def test_confirm_pwd(self, _drivers):
#         _drivers.find_element('xpath', '//input[@id="ConfirmPassword"]').send_keys('megha@12345')
#
#     time.sleep(3)


#---------------------------------------------------------------
## Using conftest

import time

class TestDemoRegister:

    def test_click_register(self, _drivers):
        _drivers.find_element('xpath', '//a[text()="Register"]').click()
        time.sleep(2)

    def test_gender_btn(self, _drivers):
        _drivers.find_element('xpath', '//input[@id="gender-female"]').click()

    def test_firstname(self, _drivers):
        _drivers.find_element('xpath', '//input[@id="FirstName"]').send_keys('Megha')

    def test_lastname(self, _drivers):
        _drivers.find_element('xpath', '//input[@id="LastName"]').send_keys('SriShankar')

    def test_register_email(self, _drivers):
        _drivers.find_element('xpath', '//input[@id="Email"]').send_keys('meghashankar@gmail.com')

    def test_register_pwd(self, _drivers):
        _drivers.find_element('xpath', '//input[@id="Password"]').send_keys('megha@12345')

    def test_confirm_pwd(self, _drivers):
        _drivers.find_element('xpath', '//input[@id="ConfirmPassword"]').send_keys('megha@12345')

    time.sleep(3)


















