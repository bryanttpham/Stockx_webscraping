# importing necessary packages
import xlsxwriter
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import numpy
import csv
  
# for holding the resultant list
element_list = []
  
for page in range(1, 5, 1):
    
    page_url = "https://stockx.com/sneakers?page=" + str(page)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(page_url)
    name = driver.find_elements_by_class_name("css-1x3b5qq")
    price = driver.find_elements_by_class_name("css-1kph905")
    
    for i in range(len(name)):
        element_list.append([name[i].text, price[i].text])


# with open('stockx_sneaker.csv', 'w', newline='') as file:
#       mywriter = csv.writer(file, delimiter=',')
#       mywriter.writerows(element_list)
name_list= []
price_list=[]

with open('stockx_sneaker.csv','r')as file:
    filecontent=csv.reader(file)
    for lines in filecontent:
      name_list.append(lines[0])
      price_list.append(lines[1])

new_price=price_list
for x in new_price:

  newX=x.replace("$","")
  x= newX

price_list=[s.replace("$","") for s in price_list]
price_list=[s.replace(",","") for s in price_list]

jordan_count=0
adidas_count=0
nike_count=0
other=0

for x in name_list:
  if "Jordan" in x:
    jordan_count+=1
  elif "adidas" in x:
    adidas_count+=1
  elif "Nike" in x:
    nike_count+=1  
  else:
    other+=1

total=0

for x in price_list:
   total+=int(x)

average=(total/len(price_list))
print("Average Shoe Price: "+str(average)) 
print("Quantity of Jordans: "+str(jordan_count))
print("Quantity of Adidas: "+str(adidas_count))    
print("Quantity of Nikes:" +str(nike_count))    
print("Quanity of shoes from other brands: "+str(other))    

 

  
#closing the driver
driver.close()