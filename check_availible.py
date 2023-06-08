from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import argparse 
import telegram
import asyncio

class ChromeDriver:
    def __init__(self):
        
        
        self.driver = None
        self.url = 'https://app.glofox.com/portal/#/branch/5b6dd1a5e90c2d1f403fccb6/classes-day-view?header=classes,courses'
        self.free_slot = False
        self.time_value = self.process_args_time()
        self.time_valid = True
        
        
    def driver_get_url(self):
        WINDOW_SIZE = "1920,1080"
        #CHROMEDRIVER_PATH = "C:\Users\kscan\OneDrive\Desktop\chromedriver_win32\chromedriver.exe"
        CHROMEDRIVER_PATH = r"C:\Users\kscan\OneDrive\Desktop\chromedriver_win32\chromedriver.exe"
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        self.driver =  webdriver.Chrome(options=chrome_options, executable_path=CHROMEDRIVER_PATH)
        self.driver.get(self.url)
        #print("Delay")
        #time.sleep(2) 
        
    
    def process_args_time(self):
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
        return time_value
    
    def send_notif(self):
        async def main():
            api_key = '6008231050:AAGAZ68BXofK5n14uzC7zdQsrLlYYoxpDME'
            user_id = '6087124042'

            #bot = Bot(token=api_key)
            bot = telegram.Bot(token=api_key)
            await bot.send_message(chat_id=user_id, text=f'Spot availible at {self.time_value}')
            print("Message sent!")
        asyncio.run(main())

 
    
    def check_free_slot(self):
        
        while self.free_slot == False and self.time_value != None and self.time_valid:
            self.driver_get_url()
            times , slots = self.process_info()
            if self.time_valid:
                index = times.index(self.time_value)
                print("Requested time slot:")
                print("Red Gym: ", times[index], slots[index])
                
                if int(slots[index].split("/")[0]) < 65:
                    print("Spot availible !")
                    self.free_slot = True
            else:
                self.driver.quit()
                print("Invalid time")
                print("Valid times: ", times)
            #print(int(slots[index].split("/")[0]))
            self.driver.quit()
        if self.free_slot:
            self.send_notif()
             
        
    
    def process_info(self):
        
        #elements_present = WebDriverWait(self.driver, 20).until(
        #    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.list-text-left"))
        #)
        time.sleep(2)
        # Find the element that displays the slots joined
        # Find all elements that contain gym information
        elements = self.driver.find_elements("css selector", "div.list-text-left")

        # Iterate over the elements and extract the times for the "Red Gym"
        red_gym_times = []
        red_gym_joined = []

        for element in elements:
            gym_info = element.find_element("css selector", "h4.ng-binding").text
            #print("Gym Info:", gym_info)
            if "Red Gym" in gym_info:
                time_info = element.find_element("css selector", "p.ng-binding").text
                #print("Time Info:", time_info)
                time_ = time_info.split(" - ")[0].strip()
                red_gym_times.append(time_)
                
        if self.time_value not in red_gym_times:
            self.time_valid = False 
            #print(self.time_valid)
        #print("Red Gym Times:", red_gym_times)
        
        joined_elements = self.driver.find_elements("css selector", "div.list-text-right b.ng-binding")

        # Extract the "joined" information from each element
        joined_info = [element.text.strip() for element in joined_elements if "Joined" in element.text and "65 Joined" in element.text]

        # Print the "joined" information
        for info in joined_info:
            red_gym_joined.append(info)
            #print("Joined Info:", info)
           # print("Red Gym Slots:", red_gym_joined)
        
        for i in range(len(red_gym_joined)):
            print("Red Gym: ", red_gym_times[i], red_gym_joined[i])
        return red_gym_times, red_gym_joined







driver = ChromeDriver()
driver.check_free_slot()


