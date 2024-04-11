import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def countElem(driver, tag_name)->int:
   return len(driver.find_elements(By.TAG_NAME, tag_name))

def main():
    # Initialize browser
    driver = webdriver.Chrome()

    # Navigate to your website 
    driver.get("http://localhost:3000/")
    reword_time = 10
    total_reword_time = 0
    keywords = ["student", "test"]
    tags = ["img"]
    for key in keywords:
        if findKeyword(driver, keywords):
            total_reword_time += reword_time
            time.sleep(reword_time)
    driver.quit()
    print("Presence Time:", total_reword_time)

if __name__ == "__main__":
    main()