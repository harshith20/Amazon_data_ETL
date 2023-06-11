#!/usr/bin/env python
# coding: utf-8

# In[5]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# In[2]:


URL='https://www.amazon.in/s?k=mobiles&ref=nb_sb_noss_1'
user_agent=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Saf=ari/537.36 Edg/113.0.1774.42','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36']


# In[3]:


# Headers for request
import random

HEADERS = ({'User-Agent' :random.choice(user_agent), 'Accept-Language': 'en-US, en;q=0.5'}) #add your user agent 


# In[4]:


# HTTP Request
webpage = requests.get(URL, headers=HEADERS)

# In[5]:


webpage

# In[6]:


# Soup Object containiang all data
soup = BeautifulSoup(webpage.content, "html.parser")
soup

# In[7]:


# Function to extract Product Title
def get_title(soup):

    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id":'productTitle'})
        
        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

# Function to extract features
def get_features(soup):

    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id":'productTitle'})
        
        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string
# Function to extract Product Price
def get_price(soup):

    try:
        price = soup.find("span", attrs={'class':'a-price-whole'}).text

    except AttributeError:

        try:
            # If there is some deal price
            price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()

        except:
            price = ""

    return price

# Function to extract Product Rating
def get_rating(soup):

    try:
        rating = soup.find("span", attrs={'data-hook':'rating-out-of-text','class':'a-size-medium a-color-base'}).text
    
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = ""	

    return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()

    except AttributeError:
        review_count = ""	

    return review_count

# Function to extract Availability Status
def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id':'availability'})
        available = available.find("span").string.strip()

    except AttributeError:
        available = "Not Available"	

    return available
def get_brand_name(soup):

    try:
        brand = soup.find("span", attrs={'class':'a-size-base po-break-word'}).text

    except AttributeError:
        brand = ""
        
    return brand
def get_extract_details(soup):
    
    
    rows = soup.find_all('tr')
    details = {"screen_size": [], "battery_power": [], "ram": [], "storage": [],
     "operating_system": [], "item_weight": []}
    
    for row in rows:
        span_element = row.find('span', class_='a-size-base')
        
        if span_element and span_element.text == 'Screen Size':
            td_element = row.find('td')
            if td_element:
                details['screen_size'] = td_element.text.strip()
            else:
                details['screen_size'] =''
        
        if span_element and span_element.text == 'Battery Power (In mAH)':
            td_element = row.find('td')
            if td_element:
                details['battery_power'] = td_element.text.strip()
            else:
                details['battery_power'] =''
        
        if span_element and span_element.text == 'RAM':
            td_element = row.find('td')
            if td_element:
                details['ram'] = td_element.text.strip()
            else:
                details['ram'] =''
        
        if span_element and span_element.text == 'Inbuilt Storage (in GB)':
            td_element = row.find('td')
            if td_element:
                details['storage'] = td_element.text.strip()
            else:
                details['storage'] =''
        
        if span_element and span_element.text == 'Operating System':
            td_element = row.find('td')
            if td_element:
                details['operating_system'] = td_element.text.strip()
            else:
                details['operating_system'] =''
        
        if span_element and span_element.text == 'Item Weight':
            td_element = row.find('td')
            if td_element:
                details['item_weight'] = td_element.text.strip()
            else:
                details['item_weight'] =''
            
    
    return details

    

# In[8]:


print(soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'}.get('href')))


# In[9]:


links = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

    # Store the links
links_list = []

    # Loop for extracting links from Tag Objects
for link in links:
        links_list.append(link.get('href'))

print(links_list)

# In[10]:


links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

    # Store the links
links_list = []

    # Loop for extracting links from Tag Objects
for link in links:
        links_list.append(link.get('href'))

# In[11]:


links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

    # Store the links
links_list = []

    # Loop for extracting links from Tag Objects
for link in links:
        links_list.append(link.get('href'))

# In[12]:


links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

    # Store the links
links_list = []

    # Loop for extracting links from Tag Objects
for link in links:
        links_list.append(link.get('href'))

# In[13]:


new_webpage = requests.get("https://www.amazon.in/realme-Segment-Fastest-Charging-High-res/dp/B0BZ48VZMR/ref=sr_1_3?keywords=mobiles&sr=8-3&th=1", headers=HEADERS)

new_soup = BeautifulSoup(new_webpage.content, "html.parser")


# In[14]:



print(new_soup.find("span", attrs={'class':'a-price-whole'}).text)
print(new_soup.find("span", attrs={"id":'productTitle'}).text)
# print( new_soup.find('span', attrs={'id':'inline-twister-expanded-dimension-text-size_name','class':'a-size-base a-color-base inline-twister-dim-title-value a-text-bold'}).text)
print(new_soup.find("span", attrs={'data-hook':'rating-out-of-text','class':'a-size-medium a-color-base'}).text)
print(new_soup.find("span", attrs={'class':'a-size-base po-break-word'}).text)

# print(new_soup.select('span.a-size-base:contains("RAM")').find("td", attrs={'class':'base-item-column'}).text)
# print(new_soup.select_one("span[a-size-base*=RAM]"))

rows = new_soup.find_all('tr')
for row in rows:
    span_element = row.find('span', class_='a-size-base')
    if span_element and span_element.text == 'Screen Size':
        td_element = row.find('td')
        if td_element:
            print(td_element.text.strip())
    if span_element and span_element.text == 'Battery Power (In mAH)':
        td_element = row.find('td')
        if td_element:
            print(td_element.text.strip())
    if span_element and span_element.text == 'RAM':
        td_element = row.find('td')
        if td_element:
            print(td_element.text.strip()) 
    if span_element and span_element.text == 'Inbuilt Storage (in GB)':
        td_element = row.find('td')
        if td_element:
            print(td_element.text.strip()) 
    if span_element and span_element.text == 'Operating System':
        td_element = row.find('td')
        if td_element:
            print(td_element.text.strip())        
    if span_element and span_element.text == 'Item Weight':
        td_element = row.find('td')
        if td_element:
            print(td_element.text.strip())
        break



# In[ ]:


# soup.select_one('.s-pagination-item.s-pagination-next')['href']
# webpage = requests.get(URL, headers=HEADERS)
# soup = BeautifulSoup(webpage.content, "html.parser")

# In[15]:


d = {"title": [], "price": [], "rating": [],"brand":[],
        "screen_size": [], "battery_power": [], "ram": [], "storage": [],
        "operating_system": [], "item_weight": []}
import time
for i in range(20):
        
    links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

        # Store the links
    links_list = []

        # Loop for extracting links from Tag Objects
    for link in links:
            links_list.append(link.get('href'))
    

    # Loop for extracting product details from each link 
    for link in links_list:
        delay = random.uniform(1, 3)
        time.sleep(delay)
        new_webpage = requests.get("https://www.amazon.in" + link, headers=HEADERS)

        new_soup = BeautifulSoup(new_webpage.content, "html.parser")

        # Function calls to display all necessary product information
        d['title'].append(get_title(new_soup))
        d['price'].append(get_price(new_soup))
        d['rating'].append(get_rating(new_soup))
        d['brand'].append(get_brand_name(new_soup))
        details = get_extract_details(new_soup)

        # Append the values from the 'details' dictionary to the main dictionary 'd'
        print(len(details))
        for key, value in details.items():
            
            d[key].append(value)
            if value=='':

                print('null' ,key,'value',value)

    URL=soup.select_one('.s-pagination-item.s-pagination-next')['href']
    webpage = requests.get("https://www.amazon.in" + URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")


# In[16]:



for key, value in d.items():
        print(len(d[key]),key)

len(d)

# In[17]:



phone_data=pd.DataFrame(d)

# In[22]:


phone_data.to_csv('amazon_phones.csv')

# In[1]:


import pandas as pd
import numpy as np
data =pd.read_csv('amazon_phones.csv')

# In[2]:


data.info()
data_transformed=data.copy()

# In[3]:


data_transformed['price']=data['price'].str.replace(',','').str.replace('.', '').fillna('-20').astype(int).replace({-20:np.nan})

# In[4]:


def transform_rating(df):
    try :

        df=df.split()[0]
        return df

    except AttributeError:
        return df


# In[5]:


data_transformed['rating']
data_transformed['rating']=data_transformed['rating'].apply(lambda x: transform_rating(x))
data_transformed['rating'][data_transformed['rating'].apply(lambda x: len(x) > 3)]=np.nan


# In[6]:


data_transformed['rating']=data_transformed['rating'].astype(float)
data_transformed['rating'].isnull().sum()


# In[7]:


def convert_units(value):
    
    parts = value.split()
    converted_value=0
        
    if len(parts) == 2:
        numeric_part = float(parts[0])
        unit = parts[1]
            
        if unit == 'cm':
            converted_value = numeric_part * 0.393701  # Convert cm to inches
        else:
            converted_value = numeric_part  # Keep the original value
        
        
    
    return converted_value

# In[8]:


strings =data_transformed['screen_size'].apply(lambda x: transform_rating(x))
index=strings[strings.apply(lambda x: len(x) > 4)].index


# In[9]:


data_transformed['screen_size'].apply(lambda x: convert_units(x)).loc[index]

# In[10]:


data_transformed['screen_size']=data_transformed['screen_size'].apply(lambda x: convert_units(x))

# In[11]:


data_transformed['battery_power'][pd.to_numeric(data_transformed['battery_power'], errors='coerce').isna()]

# In[12]:


data_transformed['battery_power'][pd.to_numeric(data_transformed['battery_power'], errors='coerce').isna()]=='[]'

# In[13]:


import re
def convert_abnormal_value(value):
    
    match = re.search(r'\d+(\.\d+)?', value)
    if match:
        return float(match.group())
    if re.match(r'^\d+(\.\d+)?$', value):
        return float(value)
    else:
        return float('nan')


# In[14]:


import matplotlib.pyplot as plt
data_transformed['battery_power'].apply(convert_abnormal_value)
plt.hist(data_transformed['battery_power'].apply(convert_abnormal_value))  # Drop NaN values and specify number of bins
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of Converted Data')
plt.show()

# In[15]:


index=data_transformed['battery_power'][pd.to_numeric(data_transformed['battery_power'], errors='coerce').isna()].index

print(data_transformed['battery_power'].apply(convert_abnormal_value).loc[index])

data_transformed['battery_power'].apply(convert_abnormal_value).loc[index].isna().sum()

# In[16]:


data_transformed['battery_power']=data_transformed['battery_power'].apply(convert_abnormal_value)


# In[17]:


def transform_ram(df):
    try :

        df=int(df.split()[0])
        return df

    except ValueError:
        return np.nan

# In[18]:


data_transformed['ram'].apply(lambda x: transform_ram(x)).value_counts()

# In[19]:


data_transformed[data_transformed['ram'].apply(lambda x: transform_ram(x))==32]



# In[20]:


from scipy import stats



transformed_data, lambda_value = stats.boxcox( data_transformed['ram'].apply(lambda x: transform_ram(x)))

q25 , q75 = np.percentile(transformed_data, [25, 75])
q25=data_transformed['ram'].apply(lambda x: transform_ram(x)).quantile(0.25)
q75=data_transformed['ram'].apply(lambda x: transform_ram(x)).quantile(0.75)

iqr = q75 - q25
lower_bound = q25 - 1.5 * iqr
upper_bound = q75 + 1.5 * iqr

outliers = (transformed_data < lower_bound) | (transformed_data > upper_bound)

print(sum(outliers==False),lambda_value,upper_bound)

# In[21]:


data_transformed['ram']=data_transformed['ram'].apply(lambda x: transform_ram(x))

# Here  some ram values are abnormal  with storage space having less than them , lets eliminate those values

# In[22]:


data_transformed[data_transformed['ram']==32]

# In[23]:


data_transformed['ram'][data_transformed['ram']>16] = np.nan

# In[24]:


data_transformed['ram'].value_counts()

# In[26]:


data_transformed['storage'].value_counts()

# In[81]:


def transform_storage(df):
    try :
        if len(df.split())>1 and df.split()[1] != 'MB':
            df=int(df.split()[0])
            return df

        
        return np.nan

    except ValueError:
        return np.nan

# In[71]:


data_transformed['storage'].str.split()[1][0]

# In[88]:


data_transformed['storage']=data_transformed['storage'].apply(lambda x: transform_storage(x))

# In[91]:



# data_transformed[data_transformed['storage'].apply(lambda x: transform_storage(x))==512]
data_transformed['storage'][data_transformed['storage']<12]=np.nan

# In[94]:


def transform_weight(df):
    try :
        
        df=int(df.split()[0])
        return df


    except ValueError:
        return np.nan

# In[98]:


data_transformed['item_weight'].apply(lambda x: transform_weight(x))
plt.hist(data_transformed['item_weight'].apply(lambda x: transform_weight(x)))  # Drop NaN values and specify number of bins
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of Converted Data')
plt.show()

# In[99]:


import scipy.stats as stats
import matplotlib.pyplot as plt

# Perform QQ plot
qqplot = stats.probplot(data_transformed['item_weight'].apply(lambda x: transform_weight(x)), dist="norm", plot=plt)

# Display the QQ plot
plt.title("QQ Plot - item_weight")
plt.show()

# In[100]:


import seaborn as sns

# Create histogram plot with KDE
sns.histplot(data_transformed['item_weight'].apply(lambda x: transform_weight(x)), kde=True)

# Set plot title and labels
plt.title("Histogram Plot with KDE - item_weight")
plt.xlabel("Item Weight")
plt.ylabel("Frequency")

# Display the plot
plt.show()

# In[102]:


data_transformed['item_weight']=data_transformed['item_weight'].apply(lambda x: transform_weight(x))

# In[104]:


data_transformed.columns 

# In[105]:


# Remove the column 'Unnamed: 0'
data_transformed = data_transformed.drop('Unnamed: 0', axis=1)

# Rename the columns
data_transformed = data_transformed.rename(columns={
    'screen_size': 'screen_size(inches)',
    'ram': 'ram(GB)',
    'storage': 'storage(GB)',
    'item_weight': 'item_weight(grams)'
})








# In[108]:


data_transformed = data_transformed.rename(columns={
    'battery_power': 'battery_power(MAH)'})

# In[109]:


data_transformed.describe()
