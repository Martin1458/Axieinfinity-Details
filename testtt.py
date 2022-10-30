from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


priceLink = 'https://www.axie.tech/axie-pricing/'
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"
options = webdriver.ChromeOptions()
options.add_argument("headless")


AxieId = 4368946
priceAxieLink = priceLink + str(AxieId)
#driver = webdriver.Chrome(desired_capabilities=caps, executable_path=r'C:\webdrivers\chromedriver.exe', options=options)
#ser =
driver = webdriver.Chrome(desired_capabilities=caps, service=Service('C:\webdrivers\chromedriver.exe'), options=options)

driver.get(priceAxieLink)

x = None
while (x == None):
    try:
        x = str(driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/a/div[1]/div[1]/div[1]/p'))
        #print(x)
    except:
        #print('lol')
        pass

rarity = str(driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div/div[1]/span').text)
priceLast = str(driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div[4]/div/div[1]/div/span').text)
priceQuick = str(driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div[4]/div/div[2]/div/span').text)
priceReasonable = str(driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div[4]/div/div[3]/div/span').text)
pricePatient = str(driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div[4]/div/div[6]/div/span').text)
similarAxies = str(driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div/div[2]/span/span').text)

if priceLast != 'N/A':
    priceLast = priceLast.replace('Ξ', '')
    priceLast = str(priceLast + ' WETH')

priceQuick = priceQuick.replace('Ξ', '')
priceQuick = str(priceQuick + ' WETH')
priceReasonable = priceReasonable.replace('Ξ', '')
priceReasonable = str(priceReasonable + ' WETH')
pricePatient = pricePatient.replace('Ξ', '')
pricePatient = str(pricePatient + ' WETH')

print('rarity' + rarity)
print('priceLast: ' + priceLast)
print('priceQuick: ' + priceQuick)
print('priceReasonable: ' + priceReasonable)
print('pricePatient: ' + pricePatient)
print('similarAxies: ' + similarAxies)

driver.quit()
