import requests
from bs4 import BeautifulSoup

# item variables
ilvl = "418"
itemId = "193001"
itemName = "Elemental_Lariat"

# Wowhead request
url = 'https://www.wowhead.com/item=137341.0/Cragshapers_Fitted_Hood?ilvl=441'
#url = f'https://www.wowhead.com/item={itemId}/{itemName}?ilvl={ilvl}'
response = requests.get(url)
#soup = BeautifulSoup(response.text, 'lxml')
soup = BeautifulSoup(response.text, 'html.parser')
spans = soup.find_all('span')

# Starting stat values
stats = {'int':0,'crit':0,'haste':0,'mastery':0,'vers':0}

# Only use first value found
intOpen = True
critOpen = True
versOpen = True
masteryOpen = True
hasteOpen = True

# Get stat values
for span in spans:
    print(f"------------")
    print(span)

    if "Intellect" in str(span) and intOpen:
        print(f"found Intellect")
        intSplit = str(span).split('+',1)[1].split('<',1)[0].split(' ',1)
        stats['int'] = intSplit[0]
        intOpen = False

    if "Critical Strike" in str(span) and critOpen:
        print(f"found Critical Strike")
        critSplit = str(span).split('>',2)[2].split(' ',1)
        stats['crit'] = critSplit[0]
        critOpen = False

    if "Mastery" in str(span) and masteryOpen:
        print(f"found Mastery")
        masterySplit = str(span).split('>',2)[2].split(' ',1)
        stats['mastery'] = masterySplit[0]
        masteryOpen = False

    if "Haste" in str(span) and hasteOpen:
        print(f"found Haste")
        hasteSplit = str(span).split('>',2)[2].split(' ',1)
        stats['haste'] = hasteSplit[0]
        hasteOpen = False

    if "Versatility" in str(span) and versOpen:
        print(f"found Versatility")
        versSplit = str(span).split('>',2)[2].split(' ',1)
        stats['vers'] = versSplit[0]
        versOpen = False

print(stats)
