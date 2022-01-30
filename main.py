from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import Select

print("""Welcome to CVEScrape!
1: Most Recent CVE's
2: Search
3: Exit
""")

options = webdriver.ChromeOptions()
options.add_argument("--headless")

path = 'C://chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)

loop = "true"
while loop == "true":
        search = ""
        option = input("Please select your option number: ")
        if option == "1":
                search == ""
        elif option == "2":
                search = input("Please enter what you would like to search for, or leave blank for most recent: ")
        elif option == "3":
                exit()
        else:
                print("Invalid Option")
                break

        # If you run into any firewall issues you can uncomment this section and add in your own valid cookie and useragent for bypass
        # def interceptor(request):
        #         request.headers['cookie'] = "cookie"
        #         request.headers['user-agent'] = "DanSiebels"
        # driver.request_interceptor = interceptor

        if search == "":
                driver.get('https://www.exploit-db.com/')
                driver.implicitly_wait(5)
        else:
                driver.get("https://www.exploit-db.com/search?q=" + search)
                driver.implicitly_wait(5)

        try:
                WebDriverWait(driver, 3).until(EC.element_to_be_clickable((driver.find_element(By.ID, 'CybotCookiebotDialogBodyButtonAccept')))).click()
        except Exception as e:
                print(e)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = soup.find('table', id="exploits-table")
        table_hrefs = table.find_all('a', href=True)

        for b in table_hrefs:
                if ("exploits") in b['href']:
                        print()
                        print(b.string + " | DL: https://exploit.db.com" + b['href'].replace("exploits", "download"))