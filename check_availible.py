from selenium import webdriver

# Specify the path to the ChromeDriver executable
#webdriver_path = "C:\Users\kscan\OneDrive\Desktop\Random Code\chromedriver_win32\chromedriver.exe"

driver = webdriver.Firefox

##driver.maximize_window()  

url = 'https://app.glofox.com/portal/#/branch/5b6dd1a5e90c2d1f403fccb6/classes-day-view?header=classes,courses'

driver.get(url)

  
page_source = driver.page_source


print(page_source)

driver.quit()