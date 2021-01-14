import datetime
import time
from selenium import webdriver


# 此步骤很重要
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome()


def login():
    # 打开淘宝登录页，并进行扫码登录
    driver.get("https://passport.jd.com")
    time.sleep(3)
    if driver.find_element_by_link_text("你好，请登录"):
        driver.find_element_by_link_text("你好，请登录").click()
        # 以下四行可注释掉扫码登陆
        driver.find_element_by_class_name("login-tab-r").click()
        driver.find_element_by_id("loginname").send_keys("13681985667")
        driver.find_element_by_id("nloginpwd").send_keys("2982052guxing")
        driver.find_element_by_class_name("btn-entry").click()
        print("请在10秒内完成登陆")
        # while True:
        #     try:
        #         getPic()
        #     except:
        #         print("登陆成功----")
        #     break
        time.sleep(10)
        driver.get("https://item.jd.com/100012043978.html")
    time.sleep(3)
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy():
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        buytime = datetime.datetime.now().strftime('%Y-%m-%d 09:59:59.000000')
        # 对比时间，时间到的话就点击结算
        if now >= buytime:
            try:
                driver.refresh()
                # 点击抢购
                if driver.find_element_by_link_text("抢购"):
                    print("开始抢购！")
                    driver.find_element_by_link_text("抢购").click()
                    time.sleep(0.05)
                    while now >= buytime:
                        try:
                            if driver.find_element_by_class_name('checkout-submit'):
                                print("开始提交订单！")
                                driver.find_element_by_class_name('checkout-submit').click()
                                print("提交订单完成！")
                                time.sleep(0.3)
                                # driver.switch_to.window(driver.window_handles[1])
                            if driver.find_element_by_class_name('submit-btn'):
                                print("提交订单！")
                                driver.find_element_by_class_name('submit-btn').click()
                                time.sleep(0.3)
                                # driver.switch_to.window(driver.window_handles[1])
                            if driver.find_element_by_id('order-submit'):
                                print("提交订单完成！")
                                driver.find_element_by_id('order-submit').click()
                        except:
                            time.sleep(0.02)
            except:
                time.sleep(0.08)
        print("当前时间："+now+"___________设定抢购时间："+buytime)
        time.sleep(0.05)

# def getPic():
#     # 用于找到登录图片的大图
#     s2 = r'//div/div[@class="JDJRV-bigimg"]/img'
#     # 用来找到登录图片的小滑块
#     s3 = r'//div/div[@class="JDJRV-smallimg"]/img'
#     bigimg = driver.find_element_by_xpath(s2).get_attribute("src")
#     smallimg = driver.find_element_by_xpath(s3).get_attribute("src")
#     print(smallimg + '\n')
#     print(bigimg)
#     # 背景大图命名
#     backimg = "backimg.png"
#     # 滑块命名
#     slideimg = "slideimg.png"
#     # 下载背景大图保存到本地
#     request.urlretrieve(bigimg, backimg)
#     # 下载滑块保存到本地
#     request.urlretrieve(smallimg, slideimg)
#     # 获取图片并灰度化
#     block = cv2.imread(slideimg, 0)
#     template = cv2.imread(backimg, 0)
#     # 二值化后的图片名称
#     blockName = "block.jpg"
#     templateName = "template.jpg"
#     # 将二值化后的图片进行保存
#     cv2.imwrite(blockName, block)
#     cv2.imwrite(templateName, template)
#     block = cv2.imread(blockName)
#     block = cv2.cvtColor(block, cv2.COLOR_RGB2GRAY)
#     block = abs(255 - block)
#     cv2.imwrite(blockName, block)
#     block = cv2.imread(blockName)
#     template = cv2.imread(templateName)
#     # 获取偏移量
#     result = cv2.matchTemplate(block, template, cv2.TM_CCOEFF_NORMED) # 查找block在template中的位置，返回result是一个矩阵，是每个点的匹配结果
#     x, y = np.unravel_index(result.argmax(), result.shape)
#     print("x方向的偏移", int(y * 0.4 + 18), 'x:', x, 'y:', y)
#     # 获取滑块
#     element = driver.find_element_by_xpath(s3)
#     ActionChains(driver).click_and_hold(on_element=element).perform()
#     ActionChains(driver).move_to_element_with_offset(to_element=element, xoffset=y, yoffset=0).perform()
#     ActionChains(driver).release(on_element=element).perform()
#     time.sleep(3)

if __name__ == "__main__":
    # times = input("请输入抢购时间：时间格式：2020-08-06 10:00:00.000000")
    # 时间格式："2018-09-06 11:20:00.000000"
    # url = input("请输入抢购地址：")
    login()
    buy()
# https://item.jd.com/100012043942.html#none
# https://item.jd.com/100012043978.html
# https://item.jd.com/100012043978.html
