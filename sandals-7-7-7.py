from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json
import pandas as pd

# Existing Excel file path and filename
excel_file_path = "C:\Git\data.xlsx"

# ChromeDriver options
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Read in the existing Excel file
try:
    df = pd.read_excel(excel_file_path)
    print("Excel file loaded successfully.")
except FileNotFoundError:
    # Create a new DataFrame if the file does not exist
    df = pd.DataFrame()
    print("Excel file not found. Creating a new DataFrame.")
    
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

    # # Debug: Check the raw content (first 750 characters)
    # print("Extracted JSON Content (first 750 characters):", promotions_json[:750])

    # Locate and clean the JSON portion
    start = promotions_json.find('currentPromotions')  # Locate the start of the relevant JSON
    if start == -1:
        print("Error: currentPromotions not found in the script.")
        driver.quit()
        exit()

    # Start extracting after the '=' (i.e., after '=' sign)
    start = promotions_json.find("[", start)  # Find the first opening square bracket
    end = promotions_json.find("]", start) + 1  # Find the corresponding closing square bracket

    # Extract the JSON portion
    json_data = promotions_json[start:end]

    # Clean up any extra characters like semicolons or other JavaScript syntax
    json_data = json_data.strip()
    
    # Append the missing brackets to make the JSON complete
    json_data += ' } ] } ]'

    # Debug: Inspect cleaned JSON
    # print("Cleaned JSON Data (first 1000 characters):", json_data[:10000])

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
                    
                    # Ensure the resort code column exists
                    if resort_code not in df.columns:
                        df[resort_code] = None

                    # Check if the start date already exists in column A ("Start Date")
                    if start_date not in df["Start Date"].values:
                        # Add a new row with start date, end date, and room code in the appropriate column
                        new_row = {"Start Date": start_date, "End Date": end_date}
                        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
                    
                    # Find the row corresponding to the start date and update the room code in the correct column
                    row_index = df[df["Start Date"] == start_date].index[0]
                    df.at[row_index, resort_code] = room_code

    # Save updated data back to Excel
    df.to_excel(excel_file_path, index=False)
    print(f"Data has been updated and saved to {excel_file_path}.")

except json.JSONDecodeError as e:
    print("Error parsing JSON:", e)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
