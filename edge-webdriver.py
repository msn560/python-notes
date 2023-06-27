from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
from selenium import webdriver
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
profile = "default"
profileDIR = ROOT + "/" + profile
if not os.path.isdir(profileDIR):
    os.mkdir(profileDIR)

Agent = "edge user agent"
service = Service(EdgeChromiumDriverManager().install())
options = webdriver.EdgeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("start-maximized")
options.add_argument("--no-sandbox")
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--profile-directory=default".format(profile))
options.add_argument("--user-data-dir={}".format(profileDIR))
options.add_argument(f"user-agent={Agent}")
options.add_experimental_option("detach", True)

driver = webdriver.Edge(service=service, options=options)
driver.get("http://google.com")
