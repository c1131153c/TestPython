from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import random

global b_trc, s_trc, title


class Handle():
    # 登入
    def login():
        # 流程:
        # 判斷頁面是否正確, 輸入帳號密碼, 登入
        t_login = driver.find_element_by_xpath(
            "//*[@id='__layout']/div/div[1]/div/div/div/div[5]/form/div[6]/button/div/span"
        ).text
        print("頁面為:", t_login.strip())

        try:
            for i in range(len(title)):
                if title[i] == t_login.strip():
                    # print ("正確頁面!")
                    user = driver.find_element_by_name("account")
                    user.clear
                    user.send_keys("fb_20532710")
                    pwd = driver.find_element_by_name("password")
                    pwd.clear
                    pwd.send_keys("000000", Keys.ENTER)

                    driver.implicitly_wait(2)
                    # Handle.topup()
                    Handle.t_buy()
                else:
                    continue
        except Exception as e:
            print("頁面顯示錯誤.", format(e))
            driver.close()

    # 充值
    def topup():
        # 流程
        # 點選按鈕, 判斷頁面是否正確, 充值(法幣-支付方式-支付通道-支付金額(亂數5000-50000000)-確認)
        driver.find_element_by_xpath(
            "//*[@id='nuxt-page-wrapper']/div/div/div/div[4]/a[1]").click()
        t_topup = driver.find_element_by_xpath(
            "//*[@id='__layout']/div/header/div/span").text
        print("頁面為:", t_topup.strip())

        try:
            for i in range(len(title)):
                if title[i] == t_topup.strip():
                    # print ("正確頁面!")

                    # 充值(法幣-支付方式-支付通道-支付金額(亂數5000-50000000)-確認-再次確認)
                    driver.find_element_by_xpath(
                        "//*[@id='nuxt-page-wrapper']/div/div/div/div/div[1]/div/div[1]/span"
                    ).click()
                    driver.find_element_by_xpath(
                        "//*[@id='nuxt-page-wrapper']/div/div/div/div/div[2]/div/div/form/div[1]/div/div[1]"
                    ).click()
                    driver.find_element_by_xpath(
                        "//*[@id='nuxt-page-wrapper']/div/div/div/div/div[2]/div/div/form/div[2]/div[1]/div[2]/div/div/div"
                    ).click()
                    driver.find_element_by_xpath(
                        "//*[@id='nuxt-page-wrapper']/div/div/div/div/div[2]/div/div/form/div[2]/div[3]/div/div[2]/div[1]/ul/li[1]/div"
                    ).click()
                    driver.find_element_by_xpath(
                        "//*[@id='nuxt-page-wrapper']/div/div/div/div/div[2]/div/div/form/div[2]/div[3]/div/div[1]/button[2]"
                    ).click()
                    num = random.randrange(5000, 10000)
                    n_input = driver.find_element_by_xpath(
                        "//*[@id='nuxt-page-wrapper']/div/div/div/div/div[2]/div/div/form/div[3]/div/div[2]/div[1]/div/input"
                    )
                    n_input.clear
                    n_input.send_keys(num)
                    driver.find_element_by_xpath(
                        "//*[@id='nuxt-page-wrapper']/div/div/div/div/div[2]/div/div/form/div[6]/button"
                    ).click()
                    driver.find_element_by_xpath(
                        "//*[@id='nuxt-page-wrapper']/div/div/div/div[4]/button"
                    ).click()
                    Handle.t_buy()
                else:
                    continue
        except Exception as e:
            print("頁面顯示錯誤.", format(e))
            driver.close()

    # 現貨交易(買TRC)
    def t_buy():
        # 流程:
        # 點選按鈕, 判斷頁面是否正確, 選取現貨交易按鈕, 買入按鈕, 輸入買入多少, 確認
        driver.find_element_by_xpath(
            "//*[@id='nuxt-page-wrapper']/div/div/div/div[3]/div[2]").click()
        t1_trade = driver.find_element_by_xpath(
            "//*[@id='__layout']/div/header/div/span").text
        print("頁面為:", t1_trade.strip())

        try:
            for i in range(len(title)):
                if title[i] == t1_trade.strip():
                    # print ("正確頁面!")
                    driver.implicitly_wait(8)
                    driver.find_element_by_xpath(
                        "//*[@id='nuxt-page-wrapper']/div/div[1]/div/div[2]/div[2]/div/div[1]/button[1]"
                    ).click()
                    b_input = driver.find_element_by_xpath(
                        "//*[@id='nuxt-page-wrapper']/div/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/input"
                    )
                    b_input.clear
                    b_input.send_keys(b_trc)
                    driver.find_element_by_xpath(
                        "//*[@id='nuxt-page-wrapper']/div/div[1]/div/div[2]/div[2]/div/div[6]/button"
                    ).click()

                    print("完成買入TRC 交易!")
                    driver.implicitly_wait(2)
                    Handle.t_sell()
                else:
                    continue
        except Exception as e:
            print("頁面顯示錯誤.", format(e))
            driver.close()

    # 現貨交易(賣TRC)
    def t_sell():
        # 流程:
        # 點選按鈕, 判斷頁面是否正確, 選取現貨交易按鈕, 賣出按鈕, 輸入賣出多少, 確認
        # driver.find_element_by_xpath("//*[@id='nuxt-page-wrapper']/div/div/div/div[3]/div[2]").click()
        t2_trade = driver.find_element_by_xpath(
            "//*[@id='__layout']/div/header/div/span").text
        print("頁面為:", t2_trade.strip())

        try:
            for i in range(len(title)):
                if title[i] == t2_trade.strip():
                    # print ("正確頁面!")
                    driver.find_element_by_xpath(
                        "//*[@id='nuxt-page-wrapper']/div/div[1]/div/div[2]/div[2]/div/div[1]/button[2]"
                    ).click()
                    s_input = driver.find_element_by_xpath(
                        "//*[@id='nuxt-page-wrapper']/div/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/input"
                    )
                    s_input.clear
                    s_input.send_keys(s_trc)
                    driver.find_element_by_xpath(
                        "//*[@id='nuxt-page-wrapper']/div/div[1]/div/div[2]/div[2]/div/div[6]/button"
                    ).click()

                    print("完成賣出TRC 交易!")
                    driver.implicitly_wait(1)
                    driver.close()
                else:
                    continue
        except Exception as e:
            print("頁面顯示錯誤.", format(e))
            driver.close()


if __name__ == '__main__':
    title = ['login', 'speedBuy', 'descMiningTransaction', '登录', '快捷买币', '交易']

    # b_trc = input("欲購買TRC數:")
    # s_trc = input("欲販售TRC數:")
    b_trc = 5
    s_trc = 5

    url = "https://501-mining-dev.gg30cm.me/home"
    webdriver.ChromeOptions().add_argument(
        'user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'
    )
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_window_size(400, 1000)
    driver.get(url)

    Handle.login()

# python3.8
# 礦機測試 2021_0722
# filename: AutoTrade.py
# 登入-充值-交易(買入RTC)-現貨交易(賣出RTC)
# 帳:1747902812@qq.com
# 密:000000
