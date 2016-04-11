#!/usr/bin/env python
# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


if __name__ == '__main__':
    timeout = 20
    count = 1
    while True:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get('http://www.baidu.com')
        try:
            print 'the %dth locate' % count
            WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_id('kw').is_displayed())
            driver.find_element_by_id('kw').send_keys(u'自动化测试')
            break
        except TimeoutException:
            print 'no such element!'
            if count == 3:
                break
            else:
                continue
        except NoSuchElementException:
            print 'locate timeout!'
            if count == 3:
                break
            else:
                continue
        finally:
            count = count + 1
    driver.find_element_by_id('su').click()
    pass
