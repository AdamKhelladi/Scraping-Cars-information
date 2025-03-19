# Scrape Porsche Cars Website: 

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def porsche_cars_info():
  url = f"https://www.porsche.com/middle-east/_egypt_/models/?compare" 
 
  html = requests.get(url).text  
  soup = bs(html, "html.parser")  

  models = soup.find_all("div", {"class": "m-14-model-series"})
  print(f"There Is: {len(models)} Models.", end="\n\n")

  master_list = [] 

  for model in models:
    model_name = model.find("h3", {"class": "m-14-model-series-divider"}).text
    
    cars = model.find_all("div", {"class": "m-14-model-tile-link-overview"})
    for car in cars: 
      car_img = car.find("img").get("data-image-src")

      car_name = car.find("div", {"class": "m-14-model-name"}).text
      car_price = car.find("div", {"class": "m-14-model-price"}).text.split()
      car_price = "".join(car_price)[6:14]

      car_info = {
        "Car Name": car_name,
        "Car Price": car_price,
        "Car Image Url": car_img
      }

      master_list.append(car_info)
  
  df = pd.DataFrame(master_list)
  df.to_csv("cars_info.csv", index=False)
  print("Flie Created.")

porsche_cars_info()


