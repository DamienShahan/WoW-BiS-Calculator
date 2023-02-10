# Import libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Read item_data csv file
itemData = pd.read_csv('./item_data_evoker.csv', header=0,delimiter=',')
itemData = itemData.fillna(0)

# Read item-names.json
# This step can take up to 1 minute
itemNames = pd.read_json('item-names.json')
itemNames = itemNames.ItemSparse.apply(pd.Series)

# Loop through items in itemData to get their IDs
for index, item in enumerate(itemData['Name']):
    itemData['id'][index] = itemNames.loc[itemNames['en_US'] == item][:1].index[0]

# Verification step
print(itemData)

# List of error items
errorList = []

# request data for all items
for index, item in itemData.iterrows():
    # Wowhead request
    currentItemName = item["Name"].replace(" ","_").replace("'","")
    try:
        url = f'https://www.wowhead.com/item={item["id"]}/{currentItemName}?ilvl={item["ilvl"]}'
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        spans = soup.find_all('span')

        # Only use first value found
        intOpen = True
        critOpen = True
        versOpen = True
        masteryOpen = True
        hasteOpen = True

        # Get stat values
        for span in spans:
            if "Intellect" in str(span) and intOpen:
                intSplit = str(span).split('+',1)[1].split('<',1)[0].split(' ',1)
                itemData.at[index, 'Int'] = intSplit[0].replace(",","")
                intOpen = False

            if "Critical Strike" in str(span) and critOpen:
                critSplit = str(span).split('>',2)[2].split(' ',1)
                itemData.at[index, 'Crit'] = str(critSplit[0])
                critOpen = False

            if "Mastery" in str(span) and masteryOpen:
                masterySplit = str(span).split('>',2)[2].split(' ',1)
                itemData.at[index, 'Mastery'] = str(masterySplit[0])
                masteryOpen = False

            if "Haste" in str(span) and hasteOpen:
                hasteSplit = str(span).split('>',2)[2].split(' ',1)
                itemData.at[index, 'Haste'] = str(hasteSplit[0])
                hasteOpen = False

            if "Versatility" in str(span) and versOpen:
                versSplit = str(span).split('>',2)[2].split(' ',1)
                itemData.at[index, 'Vers'] = str(versSplit[0])
                versOpen = False

    except:
        print(f"Error with {currentItemName}")
        errorList.append(currentItemName)
        continue

itemData

# Save updated itemData to csv file
itemData.to_csv('item_data_filled.csv',sep=',')

# Print finished message
print("Data saved to item_data_filled.csv")
print(f"Error with the following items")
print(errorList)