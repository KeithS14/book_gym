from selenium import webdriver

try:
    driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    print("ChromeDriver found and instantiated successfully!")
    driver.quit()
except Exception as e:
    print("Unable to find or instantiate ChromeDriver. Error: ", e)