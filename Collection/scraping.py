import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker" \
           "=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_ps&as" \
           "-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=ad6bb660-fa57-479a-8a90-87b55f8556ed&as" \
           "-backfill=on"

num_pages = 45

data = {"Product Name": [], "Features": [], "Price": []}
for page_number in range(1, num_pages + 1):
    url = f"{base_url}&page={page_number}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title_divs = soup.select("div._4rR01T")
    features_class = "fMghEO"
    features = soup.find_all("div", class_=features_class)
    prices = soup.select("div._25b18c")
    for title in title_divs:
        data["Product Name"].append(title.string.split("-")[0].strip())

    for feature in features:
        laptop_feature = []
        li_elements = feature.find_all('li')
        for li in li_elements:
            if "," not in li.get_text():
                laptop_feature.append(li.get_text())
        data["Features"].append(laptop_feature)

    for price in prices:
        data["Price"].append(price.find("div").get_text())
        if len(data["Price"]) == len(data["Product Name"]):
            break

df = pd.DataFrame.from_dict(data)
df.to_csv("flipkart_laptop_data.csv", index=True)
