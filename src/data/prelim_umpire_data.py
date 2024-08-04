from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def load_umpire_data():
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

    try:
        driver.get('https://swishanalytics.com/mlb/mlb-umpire-factors')

        WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.table-responsive.table-umpires > table")))

        table = driver.find_element(By.CSS_SELECTOR, "div.table-responsive.table-umpires > table")

        rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")

        umpire_data = {}

        for row in rows:
            umpire_name = row.find_element(By.CSS_SELECTOR, "td.umps-name").text.strip()
            row_data = [cell.text.strip() for cell in row.find_elements(By.CSS_SELECTOR, "td")]
            
            i = 3
            while i < len(row_data):
                if len(row_data[i]) > 1:
                    if row_data[i].endswith('%'):
                        row_data[i] = round(float(row_data[i].strip('%')) / 100, 3)
                    elif row_data[i].endswith('x'):
                        row_data[i] = float(row_data[i].strip('x'))
                    else:
                        row_data[i] = float(row_data[i])
                else:
                    row_data[i] = 1.0
                i += 1
            
            umpire_data[umpire_name] = row_data[3:]
    
    finally:
        driver.close()
        driver.quit()
    
    return umpire_data
