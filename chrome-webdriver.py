from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import os
ROOT = os.path.dirname(os.path.abspath(__file__))
profile ="default"
profileDIR = ROOT  +"/"+profile  
if not os.path.isdir(profileDIR):
            os.mkdir(profileDIR)
Agent ="chrome user agent"
service =  Service(ChromeDriverManager().install())  
options = webdriver.ChromeOptions()
options.add_experimental_option( "excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("start-maximized") #fullscreen başlatır
options.add_argument('--no-sandbox')
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--ignore-certificate-errors")
options.add_argument('--profile-directory=default'.format(profile))
options.add_argument('--user-data-dir={}'.format(profileDIR))
options.add_argument(f'user-agent={Agent}') #agent
options.add_experimental_option("detach", True) #otomatik olarak kapatmasını önlemek için kullanılır.
driver = webdriver.Chrome(service=service  , options=options  )
driver.get("http://example.com")