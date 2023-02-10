# WoW-BiS-Calculator
A quick script to get all item data for a personal character bis list. The bis list can be created in a spreadsheet or with further scripts. The content of this project is currently just to get all the required item data. 

![BiS Spreadsheet](https://i.imgur.com/0Iel8Xv.png)

# Usage guide
* Download and install the require packages: pandas, requests, bs4 (BeautifulSoup)
* Create or download the item data csv (e.g. item_data_evoker.csv) with the following fields: Type,Name,id,ilvl,Source,Amount,Int,Crit,Haste,Mastery,Vers
* Update the file name in main.py on line 7.
* Execute main.py
* The script will output a file called item_data_filled.csv with the following fields filled out: id, Int, Crit, Haste, Mastery, Vers

# Error handling
If items are not being filled out, or can not be found entirly, check the corresponding wowhead page. The script scrapes the wowhead item page for the stat info.

The wowhead link is build like this: https://www.wowhead.com/item={item["id"]}/{currentItemName}?ilvl={item["ilvl"]}

It is important to note, that all whitespaces ( ) are substituted with an underscore (_) and all single quotation marks (') are removed removed without a substitute.