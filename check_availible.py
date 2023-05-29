from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import argparse 

# Create the argument parser
parser = argparse.ArgumentParser(description='Script to handle command-line arguments')

# Add the --time argument
parser.add_argument('--time', help='Specify the time')

# Parse the command-line arguments
args = parser.parse_args()

# Retrieve the value of the --time argument
time_value = args.time

# Print the value of the --time argument
print('Time:', time_value)

WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

driver = webdriver.Chrome(chrome_options=chrome_options)
#driver = webdriver.Chrome(executable_path='C:\Users\kscan\OneDrive\Desktop\chromedriver\chromedriver.exe')
#driver = webdriver.Chrome(executable_path=r'C:\Users\kscan\OneDrive\Desktop\chromedriver_win32\chromedriver.exe')


##driver.maximize_window()  

url = 'https://app.glofox.com/portal/#/branch/5b6dd1a5e90c2d1f403fccb6/classes-day-view?header=classes,courses'

driver.get(url)

# Add a delay to allow the page to load
time.sleep(2) 


# Find the element that displays the slots joined
# Find all elements that contain gym information
elements = driver.find_elements("css selector", "div.list-text-left")



# Iterate over the elements and extract the times for the "Red Gym"
red_gym_times = []
red_gym_joined = []

for element in elements:
    gym_info = element.find_element("css selector", "h4.ng-binding").text
    print("Gym Info:", gym_info)
    if "Red Gym" in gym_info:
        time_info = element.find_element("css selector", "p.ng-binding").text
        print("Time Info:", time_info)
        time_ = time_info.split(" - ")[0].strip()
        red_gym_times.append(time_)
        
        """ joined_info = element.find_element("css selector", "div.list-text-right b.ng-binding").text
        print("Joined Info:", joined_info)
        joined = joined_info.strip()
        red_gym_joined.append(joined) """
        
print("Red Gym Times:", red_gym_times)


joined_elements = driver.find_elements("css selector", "div.list-text-right b.ng-binding")

# Extract the "joined" information from each element
joined_info = [element.text.strip() for element in joined_elements if "Joined" in element.text and "65 Joined" in element.text]

# Print the "joined" information
for info in joined_info:
    red_gym_joined.append(info)
    #print("Joined Info:", info)
print("Red Gym Slots:", red_gym_joined)

for i in range(len(red_gym_joined)):
    
    print("Red Gym: ", red_gym_times[i], red_gym_joined[i])

if time_value != None:
    index = red_gym_times.index(time_value)
    print("Red Gym: ", red_gym_times[index], red_gym_joined[index])



driver.quit()
