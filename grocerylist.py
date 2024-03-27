import requests
from bs4 import BeautifulSoup

print("Enter your grocery list.\nEnter Done When you put everything in the list.")
List = []
addtoList = True

while(addtoList):
    print("Enter an item")
    Item = input()
    if(Item.lower() ==  "done"):
        addtoList = False
        break
    List.append(Item.lower())

print(List)

print("Do you want to remove an Item\nYes or No")
Q = input()
if(Q.lower() == "yes"):
    print("What do you want to remove?")
    print(List)
    remove = input()
    List.remove(remove.lower())

print(List)

//ignore the below
print("Enter the name of your town:")
location = input()

url = f"https://www.google.com/maps/search/grocery+store+in+{location}"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

restaurants = soup.find_all("div", class_="section-result-details-container")

for restaurant in restaurants:
    name = restaurant.find("h3", class_="section-result-title").text.strip()
    address = restaurant.find("span", class_="section-result-location").text.strip()
    
    print("Name:", name)
    print("Address:", address)
    print("-" * 50)
