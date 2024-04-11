import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def findText(driver, keyword):
    if keyword.lower() in driver.page_source.lower():
        return True
    else:
        return False

def countTagElem(driver, tag_name)->int:
    count = 0
    for tags in tag_name:
        count += len(driver.find_elements(By.TAG_NAME, tags))

def userAction(action, driver, reward_time, req_list)->float:
    total_reward_time = 0
    if action.upper() == "KEYWORD":
        for keyword in req_list:
            if findText(driver, keyword):
                print("found",keyword)
                time.sleep(reward_time)
                total_reward_time += reward_time
            else:
                print("not found")
    elif action.upper() == "IMAGE":
        num_images = countTagElem(driver, req_list)
        total_reward_time = reward_time*num_images
        time.sleep(total_reward_time)
    
    return total_reward_time

def clickLink(driver,href):
    links = driver.find_elements(By.TAG_NAME, "a")

    for link in links:
        link.click()

def main():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/")
    reword_time = 10
    total_reword_time = userAction("KEYWORD", driver, reword_time, ["student", "test"])
    tag_name = "img"
    total_reword_time += userAction("IMAGE", driver, reword_time, [tag_name])
    #clickLink(driver)
    
    driver.quit()
    print("Presence Time:", total_reword_time)

if __name__ == "__main__":
    main()