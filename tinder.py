#!/usr/bin/python3

from selenium import webdriver
from time import sleep
from login import username, password
from random import random

class tinder():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self):
        self.driver.get('https://tinder.com/')

        sleep(2)

        acpt_cok = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        acpt_cok.click()
        sleep(5)

        login_button = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        login_button.click()

        sleep(2)

        log_in = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div/div/button')
        log_in.click()

        basewindow = self.driver.window_handles[0]
        popup = self.driver.switch_to_window(self.driver.window_handles[1])
        #login to google email
        email_id = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_id.send_keys(username)
        next_btn = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
        next_btn.click()
        sleep(2)
        pass_field = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        pass_field.send_keys(password)
        next_btn_2 = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
        next_btn_2.click()
        sleep(5)
        self.driver.switch_to_window(basewindow)
        sleep(5)
        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()
        sleep(2)
        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()
        sleep(8)
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div[3]/button[2]')
        popup_3.click()
        sleep(4)

    def like(self):
        try:
            swipe_like = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
            swipe_like.click()
        except Exception:
            self.close_popup()

    def dislike(self):
        try:
            swipe_dislike = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div[1]/div[2]/div[2]/button')
            swipe_dislike.click()
        except:
            swipe_dislike = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button')
            swipe_dislike.click()

    def close_match_window(self):
        close_wind = self.driver.find_element_by_xpath("//*[@id="modal-manager"]/div/div/div/div[3]/button[2]")
        close_wind.click()


    def auto_swipe(self):
        swipes = 1000
        like, dislike = 0,0
        while swipes > 0:
            sleep(1)
            try:
                rand = random()
                if rand < .80:
                    self.like()
                    swipes = swipes - 1
                    like += 1
                    print('{} like'.format(like))
                else:
                    self.dislike()
                    swipes = swipes - 1
                    dislike += 1
                    print('{} dislike'.format(dislike))
            except Exception:
                try:
                    close_popup()
                except Exception:
                    try:
                        match_close()
                    except Exception:
                        try:
                            close_match_window()
                        except Exception:
                            break


    def close_popup(self):
        try:
            close_pop = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
            close_pop.click()
        except Exception:
            try:
                close_pop = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]')
                close_pop.click()
            except Exception:
                try:
                   close_pp = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]')
                   close_pp.click()
                except Exception:
                   close_popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]/span')
                   close_popup_2.click()

    def match_close(self):
        close_match = self.driver.find_element_by_xpath('')
        close_match.click()

    def auto_chat(self):
        matches = self.driver.find_element_by_class_name('matchListItem')
        matches[0].click()

bot = tinder()
bot.login()
bot.auto_swipe()
