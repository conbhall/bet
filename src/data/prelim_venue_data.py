from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def load_venue_data():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-images")
    prefs = {
        'profile.default_content_setting_values': {
            'images': 2,
            'javascript': 2,
            'stylesheet': 2
        }
    }
    options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    venue_data = {}

    try:
        driver.get('https://swishanalytics.com/mlb/mlb-park-factors')

        WebDriverWait(driver, 12).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'h4.lato#vert-mid')))

        venue_elements = driver.find_elements(By.CSS_SELECTOR, "h4.lato#vert-mid")

        #"//h4[contains(@class, 'venue-title')]"

        for venue in venue_elements:
            venue_name = venue.text.strip()
            venue_table = venue.find_element(By.XPATH, "./following::table[1]")
            venue_rows = venue_table.find_elements(By.TAG_NAME, 'tr')

            venue_data[venue_name] = {'L': [], 'R': []}

            for row in venue_rows[1:]:
                venue_cells = row.find_elements(By.TAG_NAME, 'td')
                venue_row_data = [cell.text for cell in venue_cells]
                venue_data[venue_name]['L'].append(float(venue_row_data[0]))
                venue_data[venue_name]['R'].append(float(venue_row_data[2]))
    
    finally:
        driver.close()
        driver.quit()
    
    return venue_data

