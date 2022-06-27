from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

profile_path = r'C:\Users\User\AppData\Roaming\Mozilla\Firefox\Profiles\nahd6ha2.default'
options=Options()
options.set_preference('profile', profile_path)
service = Service(r'C:\chromedriver\geckodriver.exe')

driver = Firefox(service=service, options=options)

driver.get("https://selenium.dev")

driver.quit()

