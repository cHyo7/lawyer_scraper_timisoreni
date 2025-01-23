import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Initialize the base URL and number of pages
base_url = 'https://www.timisoreni.ro/info/avocati'
total_pages = 69  # Total pages to scrape

# Step 2: Create a list to store the lawyer data
lawyer_data = []

# Step 3: Loop through all pages
for page_num in range(1, total_pages + 1):
    # Construct the URL for the current page
    if page_num == 1:
        url = base_url  # The first page does not have a numbered suffix
    else:
        url = f'{base_url}/{page_num}.htm'

    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve page {page_num}. Skipping...")
        continue

    # Step 4: Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 5: Find all lawyer blocks on the current page
    lawyers = soup.find_all('a', itemprop='url')

    # Extract names and phone numbers
    for lawyer in lawyers:
        name = lawyer.find('span', itemprop='name').text.strip() if lawyer.find('span', itemprop='name') else 'No name found'
        phone_tag = lawyer.find_next('b', itemprop='telephone')
        phone = phone_tag.text.strip() if phone_tag else 'No phone number found'

        # Append the data to the list
        lawyer_data.append({'Name': name, 'Phone': phone})

    print(f"Page {page_num} scraped successfully.")

# Step 6: Create a DataFrame
df = pd.DataFrame(lawyer_data)

# Step 7: Save the DataFrame to an Excel file
file_name = 'lawyer_leads_all_pages.xlsx'
df.to_excel(file_name, index=False, engine='openpyxl')

print(f"Excel file '{file_name}' created successfully with {len(lawyer_data)} records.")
