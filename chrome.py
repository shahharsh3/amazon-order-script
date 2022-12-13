import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# filename = "imdb_top_4.xlsx"
# header = ("Rank", "Rating", "Title")

# updater(filename)
s=Service('/Users/harshshah/Documents/Chromedriver/chromedriver')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.amazon.com/ap/signin?ie=UTF8&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&switch_account=signin&ignoreAuthState=1&disableLoginPrepopulate=1&ref_=ap_sw_aa")
email = driver.find_elements(By.XPATH, "//*[@class='c-stepper-input__plus']")
email.click()
email.send_keys("test@gmail.com")
cont = driver.find_element(By.ID, 'continue')
cont.submit()
pswd = driver.find_element(By.ID, 'ap_password')
pswd.send_keys("123456")
submit= driver.find_element(By.ID, 'signInSubmit')
submit.submit()
time.sleep(3)
current_url = driver.current_url
url = "https://www.amazon.com/?ref_=nav_ya_signin&"
if url == current_url:
    order = driver.find_element(By.ID, 'nav-orders')
    print(order)
    order.click()
    orders_list = driver.find_elements(By.CSS_SELECTOR, 'a-size-medium a-color-base a-text-bold')
    order_details = driver.find_element(By.CSS_SELECTOR, 'a-link-normal')
    for i in orders_list:
        data = [
            (i, orders_list[i], order_details[i]),
        ]
        writer(header, data, filename, "write")
        print("file created")

    order_details.click()

driver.quit()

def writer(header, data, filename, option):
        with open(filename, "w", newline="") as csvfile:
            if option == "write":

                movies = csv.writer(csvfile)
                movies.writerow(header)
                for x in data:
                    movies.writerow(x)
            elif option == "update":
                writer = csv.DictWriter(csvfile, fieldnames=header)
                writer.writeheader()
                writer.writerows(data)
            else:
                print("Option is not known")


def updater(filename):
    with open(filename, newline="") as file:
        readData = [row for row in csv.DictReader(file)]
        # print(readData)
        readData[0]['Rating'] = '9.4'
        # print(readData)

    readHeader = readData[0].keys()
    writer(readHeader, readData, filename, "update")
