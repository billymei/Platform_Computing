import time 
from selenium import webdriver

def countElem(driver, tag_name)->int:
   return len(driver.find_elements(By.TAG_NAME, tag_name))

def main():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/")
    reword_time = 10
    total_reword_time = 0
    tags = ["img"]
    for tag in tags:
        num_images = countElem(driver, tag)
        total_reword_time += reword_time*num_images
        time.sleep(total_reword_time)
    driver.quit()
    print("Presence Time:", total_reword_time, "second(s)")

if __name__ == "__main__":
    main()