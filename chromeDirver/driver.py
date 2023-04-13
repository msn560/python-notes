import glob
import keyboard
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
import time,os 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def driver(profile ="newProfile" ):
    root = os.path.dirname(os.path.abspath(__file__))
    
    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
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
    options.add_argument(f'user-agent={agent}')
    options.add_experimental_option("detach", True)
    # options.add_argument("...")
    driver = webdriver.Chrome(service=_service, options=options)
    stealth(driver, languages=["en-US", "en"], vendor="Google Inc.", platform="Win32",
            webgl_vendor="Intel Inc.", renderer="Intel Iris OpenGL Engine")

    try:
        time.sleep(1)
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {  "userAgent": agent}) 
        jsLoad = glob.glob(os.path.join(root+"/execute_script/", "*.js")) 
        for js in jsLoad:
            with open(js, "r", encoding="utf-8") as f: 
                driver.execute_script("""{}""".format(f.read())) 
        #driver.get("chrome://version/")
    except Exception as e:
        return driver
    return driver
 

def wait(driver, element=(By.XPATH, "/html/head/title"), waitTime=5 ):
    try:
        wait = WebDriverWait(driver,waitTime) 
        element = wait.until(
            lambda driver: driver.find_elements(element[0], element[1]))
         
    except Exception as e:
        print("e:",e)
        return None
    return element
def waitkey(key = "q"):
    print("İşlemi bitirmek için [{}] tuşuna basın.".format(key))
    while True:
        if keyboard.is_pressed(key):
            print("Döngü klavyeden sonlandırıldı.")
            break
        else:
            continue
