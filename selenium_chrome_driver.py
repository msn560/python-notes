from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
import time,os 
from webdriver_manager.chrome import ChromeDriverManager
root = os.path.dirname(os.path.abspath(__file__))
profile ="game" 
profile_dir = root+"/"+profile
if not os.path.isdir(profile_dir):
    os.mkdir(profile_dir)
 
_service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option(
    "excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("start-maximized")
options.add_argument('--no-sandbox')
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--ignore-certificate-errors")
options.add_argument('--profile-directory={}'.format(profile))
options.add_argument('--user-data-dir={}'.format(profile_dir))
options.add_experimental_option("detach", True)
# options.add_argument("...")
driver = webdriver.Chrome(service=_service, options=options)
stealth(driver, languages=["en-US", "en"], vendor="Google Inc.", platform="Win32",
        webgl_vendor="Intel Inc.", renderer="Intel Iris OpenGL Engine")
try:
    driver.get("https://accounts.google.com/signin/v2/identifier")
except Exception as e:
    print("e:",e)
 
