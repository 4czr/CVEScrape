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

# Set the webdriver and --headless flag to start the driver hidden
options = webdriver.ChromeOptions()
options.add_argument("--headless")

# Define driver
path = 'C://chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)

loop = "true"
while loop == "true": # Loop until exit
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
        # Although you shouldn't, everything should be fine
        # def interceptor(request):
        #         request.headers['cookie'] = "cookie"
        #         request.headers['user-agent'] = "DanSiebels"
        # driver.request_interceptor = interceptor

        if search == "": # If there's nothing to search
                driver.get('https://www.exploit-db.com/') # Get main page
                driver.implicitly_wait(5) # Just wait a lil'
        else: # If there IS search data
                driver.get("https://www.exploit-db.com/search?q=" + search) # Well then I guess I had best search for it
                driver.implicitly_wait(5) # and also wait a lil'

        try:
                # Wait until the driver can accept cookies, and accept them (so Cookiebot doesn't interfere with the requests)
                WebDriverWait(driver, 3).until(EC.element_to_be_clickable((driver.find_element(By.ID, 'CybotCookiebotDialogBodyButtonAccept')))).click() 
        except Exception as e:
                print(e)
        
        # Parse the HTML with BeautifulSoup and find the TABLE element with the ID #exploits-table
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = soup.find('table', id="exploits-table")
        table_hrefs = table.find_all('a', href=True) # Find all a hrefs in that table
        
        # For all the links in the table, and if the link contains "exploits" then
        for b in table_hrefs:
                if ("exploits") in b['href']:
                        print()
                        print(b.string + " | DL: https://exploit.db.com" + b['href'].replace("exploits", "download")) # Print the text of the a href, and also the replace the of the CVE page link with download link
