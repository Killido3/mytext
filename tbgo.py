from selenium import webdriver
import datetime
import time


# 此步骤很重要
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome()


def login():
    # 打开淘宝登录页，并进行扫码登录
    driver.get("https://www.taobao.com")
    time.sleep(3)
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()
        print("请在15秒内完成扫码")
        time.sleep(15)
        driver.get("https://chaoshi.detail.tmall.com/item.htm?spm=a3204.14194314.9341139540.1.5bddc6c02H41n7&id=20739895092&skuId=4227830352490")
    time.sleep(3)
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy():
    while True:

        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

        buytime = datetime.datetime.now().strftime('%Y-%m-%d 19:59:59.000000')

        # 对比时间，时间到的话就点击结算
        if now >= buytime:
            try:
                driver.refresh()
                # 点击抢购
                if driver.find_element_by_id("J_LinkBasket"):
                    print("速度点击！！！")
                    driver.find_element_by_id("J_LinkBasket").click()
                    time.sleep(0.05)
                    while now >= buytime:
                        try:#tb-text mui-amount-input
                            if driver.find_element_by_class_name('tm-mcCartBtn'):
                                print("赶紧买！！！")
                                driver.find_element_by_class_name('tm-mcCartBtn').click()
                                time.sleep(0.1)
                                driver.switch_to.window(driver.window_handles[1])
                                driver.find_element_by_id('J_Go').click()
                                time.sleep(0.1)
                                driver.switch_to.window(driver.window_handles[1])
                                driver.find_element_by_class_name('go-btn').click()
                        except:
                            time.sleep(0.02)
            except:
                time.sleep(0.08)
        print("当前时间："+now+"___________设定抢购时间："+buytime)
        time.sleep(0.05)


if __name__ == "__main__":
    # times = input("请输入抢购时间：时间格式：2020-07-07 20:00:00.000000")
    # 时间格式："2018-09-06 11:20:00.000000"
    login()
    buy()
# https://chaoshi.detail.tmall.com/item.htm?spm=a3204.14194314.9341139540.1.5bddc6c02H41n7&id=20739895092&skuId=4227830352490
