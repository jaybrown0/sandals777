import os
import requests
import re
import json
import pandas as pd
from bs4 import BeautifulSoup
from openpyxl import load_workbook, Workbook

# Define constants
url = "https://www.sandals.com/specials/suite-deals/"
today_date = pd.Timestamp.today().strftime("%Y-%m-%d")  # Format: yyyy-mm-dd

# Existing Excel file path and filename
excel_file_path = "C:\Git\data.xlsx"

# Define headers for HTTP request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Fetch the webpage
response = requests.get(url, headers=headers)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract all script contents
    script_contents = [script.string for script in soup.find_all("script") if script.string]

    # Search for JSON-like structures containing "promotionTitle"
    promotion_data = set()  # Use a set to store unique promotions

    for script in script_contents:
        matches = re.findall(r'({.*?promotionTitle.*?})', script, re.DOTALL)
        for match in matches:
            try:
                promo_json = json.loads(match)
                promotion_title = promo_json.get("promotionTitle", "")
                rst_code = promo_json.get("rstCode", "N/A")
                room_category = promo_json.get("roomCategory", "N/A")

                if promotion_title.startswith("7-7-7 Savings"):
                    # Store unique promotions
                    promotion_data.add((promotion_title, rst_code, room_category))
            except json.JSONDecodeError:
                continue

    # Convert to DataFrame
    df = pd.DataFrame(list(promotion_data), columns=["promotionTitle", "rstCode", "roomCategory"])
    # Convert to DataFrame (current promotions only)
    df_current_promotions = pd.DataFrame(list(promotion_data), columns=["promotionTitle", "rstCode", "roomCategory"])

    # Sort DataFrame by rstCode
    df_current_promotions = df_current_promotions.sort_values(by=["rstCode"]).reset_index(drop=True)

    # Load or create an Excel file
    if os.path.exists(excel_file_path):
        wb = load_workbook(excel_file_path)
        sheet = wb.active
    else:
        wb = Workbook()
        sheet = wb.active
        sheet.title = "7-7-7 Promotions"
        sheet.append(["Start Date"])  # Initialize headers

    # Check if today's date already exists in column A
    start_dates = [sheet.cell(row=i, column=1).value for i in range(2, sheet.max_row + 1)]
    
    if today_date in start_dates:
        # Find existing row index
        existing_row = start_dates.index(today_date) + 2  # Offset by 2 due to header row
    else:
        # Find the next available row for today's date
        existing_row = sheet.max_row + 1
        sheet.cell(row=existing_row, column=1, value=today_date)  # Set the Start Date in column A

    # Get existing headers (Rst Codes)
    headers = [sheet.cell(row=1, column=col).value for col in range(2, sheet.max_column + 1)]

    for promotion_title, rst_code, room_category in df.itertuples(index=False):
        if rst_code not in headers:
            # Find next available column
            next_col = len(headers) + 2  # Start after column A
            sheet.cell(row=1, column=next_col, value=rst_code)  # Add new header
            headers.append(rst_code)  # Update local header tracking

        # Get column index
        col_index = headers.index(rst_code) + 2

        # Check if roomCategory is already in the cell, if not, update it
        existing_value = sheet.cell(row=existing_row, column=col_index).value
        if existing_value:
            # Avoid duplication in the same cell (comma-separated)
            room_categories = set(existing_value.split(", "))
            room_categories.add(room_category)
            sheet.cell(row=existing_row, column=col_index, value=", ".join(room_categories))
        else:
            sheet.cell(row=existing_row, column=col_index, value=room_category)

    # Save the updated Excel file
    wb.save(excel_file_path)
    wb.close()
    print(f"Data successfully updated in {excel_file_path}")

    # Print only today's extracted promotions, sorted by rstCode
    print("\nToday's Extracted Promotions (Sorted by rstCode):\n")
    print(df_current_promotions)

else:
    print(f"Failed to fetch the webpage. Status Code: {response.status_code}")
