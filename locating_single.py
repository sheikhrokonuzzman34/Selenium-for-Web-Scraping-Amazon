import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Edge WebDriver
driver = webdriver.Edge()

# Define search query
query = "laptop"
file = 0

# Create 'data' directory if it doesn't exist
os.makedirs("data", exist_ok=True)

for i in range(1, 3):
    # Navigate to the Amazon search results page
    driver.get(f"https://www.amazon.com/s?k={query}&page={i}&crid=2VQO2RIC01X4O&qid=1726999794&sprefix=l%2Caps%2C806&ref=sr_pg_2")

    # Allow the page to load
    time.sleep(3)

    # Use a more specific locator (XPATH example) to locate the search results
    try:
        # Locate the first result container (adjust XPATH as needed)
        elems = driver.find_elements(By.XPATH, "//div[@class='puisg-row']")
        print(f"{len(elems)} items found")
        for elen in elems:
            d = elen.get_attribute("outerHTML")
            # Save the result in the 'data' directory
            with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
                f.write(d)
                file += 1
        
    except Exception as e:
        print(f"Error locating element: {e}")

    # Wait for 6 seconds to observe before closing the browser
    time.sleep(1)

driver.close()
