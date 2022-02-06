import sys, getopt
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

args = sys.argv[1:]
cmdoptions = "hs:r"
long_options = ["Help", "Search", "Recent"]

try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        path = 'C://chromedriver.exe'
        service = Service(executable_path=path)
        driver = webdriver.Chrome(service=service, options=options)


        arguments, values = getopt.getopt(args, cmdoptions, long_options)
        for currentArgument, currentValue in arguments:
                if currentArgument in ("-h", "--Help"):
                        print ("Displaying Help\n python3 main.py -h | Displays this text\npython3 main.py -s | Search for CVE by keyword\npython3 main.py -r | Displays the most recent CVEs posted")
                        exit()
                elif currentArgument in ("-s", "--Search"):
                        search = ("% s") % (currentValue)
                        driver.get("https://www.exploit-db.com/search?q=" + search)
                        driver.implicitly_wait(5)
                elif currentArgument in ("-r", "--Recent"):
                        driver.get('https://www.exploit-db.com/')
                        driver.implicitly_wait(5)
                else:
                        print("Displaying Help\n python3 main.py -h | Displays this text\npython3 main.py -s | Search for CVE by keyword\npython3 main.py -r | Displays the most recent CVEs posted")
                        exit()

                # If you run into any firewall issues you can uncomment this section and add in your own valid cookie and useragent for bypass
                # def interceptor(request):
                #         request.headers['cookie'] = "cookie"
                #         request.headers['user-agent'] = "DanSiebels"
                # driver.request_interceptor = interceptor

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
except getopt.error as err:
        # output error, and return with an error code
        print (str(err))
        print("\nDisplaying Help\n\npython3 main.py -h | Displays this text\npython3 main.py -s | Search for CVE by keyword\npython3 main.py -r | Displays the most recent CVEs posted")
        exit()
