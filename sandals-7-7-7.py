from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json

# Set up ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Open the webpage and wait for it to load
    url = "https://www.sandals.com/specials/?scroll=best-value-suites"
    driver.get(url)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "script")))

    # Extract JSON from script tag
    promotions_json = driver.execute_script("""
        const scriptTags = [...document.querySelectorAll('script')];
        for (let tag of scriptTags) {
            if (tag.textContent.includes('currentPromotions')) {
                return tag.textContent;
            }
        }
        return null;
    """)

    # Locate and clean the JSON portion
    start = promotions_json.find('currentPromotions')  # Locate the start of the relevant JSON
    if start == -1:
        print("Error: currentPromotions not found in the script.")
        driver.quit()
        exit()

    # Start extracting after the '=' (i.e., after '=' sign)
    start = promotions_json.find("[", start)  # Find the first opening curly brace
    end = promotions_json.find("]", start) + 1  # Find the corresponding closing curly brace

    # Extract the JSON portion
    json_data = promotions_json[start:end]

    # Clean up any extra characters like semicolons or other JavaScript syntax
    json_data = json_data.strip()
    
    # Append the missing brackets to make the JSON complete
    json_data += ' } ] } ]'

    # Attempt to parse the cleaned JSON
    promotions = json.loads(json_data)
    
    # Filter and process 'BEST_VALUE_SUITES' promotions
    print("BEST_VALUE_SUITES Promotions:")
    for promotion in promotions:  # Iterate over the list of promotions
        if promotion.get("type") == "BEST_VALUE_SUITES":  # Now 'promotion' is a dictionary
            for promo_data in promotion.get("data", []):
                start_date = promo_data.get("startDate")
                end_date = promo_data.get("endDate")
                for room in promo_data.get("rooms", []):
                    room_code = room.get("roomCode")
                    resort_code = room.get("resortCode")
                    print(f"Start Date: {start_date}, End Date: {end_date}, Resort Code: {resort_code}, Room Code: {room_code}")

except json.JSONDecodeError as e:
    print("Error parsing JSON:", e)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()


# Sandals Resport Codes

# SBR   Sandals Royal Barbados
# SBD   Sandals Barbados
# SEB   Sandals Emerald Bay - Exuma Bahamas
# SAT   Sandals Antigua
# SGL   Sandals Grande St Lucia
# SLS   Sandals Grenada
# SHC   Sandals Halcyon - St Lucia
# SMB   Sandals Montego Bay
# SNG   Sandals Negril
# SGO   Sandals Ochi
# SLU   Sandals La Toc - St Lucia
# SRB   Sandals Royal Bahamian - Nassau
# SRC   Sandals Royal Caribbean - Montego Bay
# BRP   Sandals Royal Plantation - Ochos Rio
# SWH   Sandals South Coast - Whitehouse Jamaica
# SCR   Sandals Curacao
# SSV   Sandals Saint Vincent
# SDR   Sandals Dunn's River