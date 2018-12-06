import os,time
import platform
import selenium.webdriver as sw
from pynput.keyboard import Key, Controller

def main():
    email_id = ""                    # Enter email id from Gaana Profile
    password = ""                  # Enter Gaana Password
    any_track = ""               # Enter a song name from Gaana Favourites Playlist (copy-paste)
    chromedriver = ostype()
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = sw.Chrome(chromedriver)
    driver.maximize_window()
    driver.get("https://gaana.com/myfavoritetracks")
    Login(driver, email_id, password)
    Operate(driver,any_track)
    while True:
        pass

def Login(driver,email_id, password):
    driver.find_element_by_link_text('SIGNUP OR LOGIN').click()
    driver.implicitly_wait(10)
    driver.find_element_by_class_name("emailopt").click()

    e = driver.find_element_by_id('email')
    e.send_keys(email_id)
    driver.find_element_by_id('chk-mail').click()
    time.sleep(1)

    k=Controller()
    for char in password :
        k.press(char)
        k.release(char)
        time.sleep(0.12)
    k.press(Key.enter)
    k.release(Key.enter)

def Operate(driver,any_track):
   
    driver.find_element_by_link_text(any_track).click()
    


def ostype():
    if(platform.system()=="Linux"):
        return "./chromedriver_linux64"
    if(platform.system()=="Windows"):
        return "./chromedriver_win32.exe"


if __name__ == '__main__':
    main()
