from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

# ---------- CONFIG ----------
SEARCH_QUERY = "indian veg food"
SHORTS_SCROLL_LIMIT = 10  # Number of shorts to watch
WAIT_TIME = 10

# ---------- DRIVER SETUP ----------
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument("--headless")  # Uncomment for headless mode

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, WAIT_TIME)

try:
    # ---------- OPEN YOUTUBE ----------
    driver.get("https://www.youtube.com")

    # ---------- SEARCH ----------
    search_box = wait.until(
        EC.presence_of_element_located((By.NAME, "search_query"))
    )

    for char in SEARCH_QUERY:
        search_box.send_keys(char)
        sleep(0.2)

    search_box.send_keys(Keys.ENTER)

    # ---------- CLICK FIRST SHORT ----------
    first_short = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//ytd-reel-shelf-renderer//a")
        )
    )
    first_short.click()

    # ---------- SCROLL SHORTS ----------
    for _ in range(SHORTS_SCROLL_LIMIT):
        sleep(8)
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_DOWN)

except TimeoutException:
    print("❌ Element not found or page took too long to load.")

except Exception as e:
    print("⚠️ Unexpected error:", e)

finally:
    print("✅ Automation Finished")
    sleep(5)
    driver.quit()
