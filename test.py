# import necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import process_time, sleep
import xlrd
import json 
import os
import ast
email_acc = "kevinnguyenjp2020@gmail.com"
email_pass = "fibo12358"
time_to_view = 4
file_read = 'CODE_PYTHON.xlsx'

def Login_twitter():
    
    # instantiate the Chrome class web driver and pass the Chrome Driver Manager
    exec_path_chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe" #Do not use this path that is extracted from "chrome://version/"
    exec_path_driver = "chromedriver"

    # ch_options = Options() #Chrome Options
    # ch_options.add_argument("user-data-dir = /home/ninja/.config/google-chrome/Default") #Extract this path from "chrome://version/"

    # driver = webdriver.Chrome(executable_path = exec_path_driver, options = ch_options) #Chrome_Options is deprecated. So we use options instead.

    # driver.get("https://stackoverflow.com/a/57894065/4061346")

    options = Options()
    # options.add_argument('--user-data-dir=D:\\tmp\\User Data')
    # options.add_argument('--profile-directory=Profile1')
    # options.add_argument('--lang=en')
    chromeDriverPath = 'chromedriver'
    userdatadir = '/home/ninja/Documents/autobot_ads/kevinnguyenjp'
    chromeOptions = webdriver.ChromeOptions() 
    chromeOptions.add_argument(f"--user-data-dir={userdatadir}") #Path to your chrome profile
    driver = webdriver.Chrome(chromeDriverPath, options=chromeOptions) 
    # driver.get("chrome://version")


    # driver = webdriver.Chrome(ChromeDriverManager().install())

    # Maximize the Chrome window to full-screen
    # driver.maximize_window()
    # go to Twitter's Homepage
    driver.get("https://twitter.com/")
    sleep(1)
    # click on the Login button
    try:
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div').click()
        sleep(1)
        # enter your email
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input').send_keys(email_acc)
        sleep(1)
        # enter your password
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').send_keys(email_pass)
        sleep(1)
        # click on the click button
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span').click()
        sleep(1)
        print("Login OK")
    except:
        print("Already OK Step")
    return driver

def Read_Excel_file():
    workbook = xlrd.open_workbook(file_read)
    sheet =workbook.sheet_by_index(0)
    row_count = sheet.nrows
    col_count = sheet.ncols
    cell = sheet.cell(0, 1)
    string_json = json.dumps(cell.value)
    # print(cell.value)
    converted_dict = ast.literal_eval(cell.value)
    # print(converted_dict[0])
    return converted_dict
def Get_Follow(driver,link):
    print(link)
    driver.get(link)
    followers = driver.find_elements_by_xpath('//*[contains(text(),"Yes, view profile")]')
    # followers = driver.find_elements_by_xpath('//*[@role="main"]/*/')
    print(followers)
    # followers.click()
    # //*[@role="main"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/div[3]/div/span/span
    #//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/div[3]
def Take_Control(driver,input_Json):
    print(input_Json[0])
    Control = input_Json[0]['command']
    # print(Control)
    if Control == 'follow':
        Get_Follow(driver,input_Json[0]['url_link'])

if __name__=='__main__':
    browser_driver = Login_twitter()
    control = Read_Excel_file()
    Take_Control(browser_driver,control[0])
