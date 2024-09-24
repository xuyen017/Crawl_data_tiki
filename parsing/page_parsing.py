import  logging
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

logger = logging.getLogger()

#constructor contains product data
class product_info:
 def __init__(self, brand, category, price, title , discount, rating, total_sales, prod_id):
    self.brand = brand
    self.category = category
    self.price = price
    self.title = title
    self.discount = discount
    self.rating = rating 
    self.total_sales = total_sales
    self.prod_id = prod_id

def count(self):
   return len(self.prod_id)
#constructor contains link of each product
class product_link:
  def __init__(self, image, product):
    self.image = image
    self.product = product

def process_page(website_path, link, i):
  tuple_data=[]
  tuple_data_page=[]
  request_url = website_path + link+ '?page='+ i
  html= urlopen(request_url)
  bs = BeautifulSoup(html, 'html.parser') 
  list_prod_id = bs.find_all('div', attrs={'class': re.compile('CatalogProducts')})

  for prod in list_prod_id:
    #extracting data with pattern
    try:
      brand_elemnt = prod.find('div', class_ = 'above-product-name-info')
      brand = brand_elemnt.find(class_= 'span').text.strip() if brand_elemnt else 'Unknow'

      product_name = prod.find('h3').text.strip()
      price = prod.find(class_='price-discount__price').text.strip()

      discount_element = prod.find(class_ = 'price-discount__percent')
      discount = discount_element.text.strip() if discount_element else '0%'

      image_url = prod.find('img')['srcset']

      full_stars = prod.find_all('svg', class_='star-icon')
      half_stars = prod.find_all('svg', class_='half-star')
      rating = len(full_stars) + len(half_stars) * 0.5

      total_sales = prod.find('span', class_='quantity has-border').text.split()[-1]

      product_url = "https:" + prod.previous['href']

      data_review = prod.find("p", attrs={"class":"review"}).contents
      data_rating = prod.find("span", attrs={"style": re.compile('.*')})['style']
    except AttributeError:
        discount = 0
    except Exception:
        data_review = ['null']
        data_rating = 'null'

     #store and append into tuple object
    product_data = product_info(prod_id=hash(product_name), brand = brand, category=link,price=price,title=product_name,
                                 rating=rating, total_sales=total_sales, discount=discount,)
      
    tuple_data = tuple([
                    product_data.prod_id,
                    product_data.brand,             
                    product_data.category,
                    product_data.price,
                    discount,
                    product_data.title,
                    product_data.total_sales,
                    product_data.rating,                                     
                    image_url,
                    product_url,
                    link+i
              ])
    tuple_data_page.append(tuple_data)
            
  return tuple_data_page