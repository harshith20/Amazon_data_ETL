# Amazon_data_ETL End to End Project


## Introduction
In today's data-driven world, I discovered the immense value of web scraping as a technique to extract valuable information from websites. Once I had collected the data, my next challenge was to clean, transform, and load it into a suitable storage solution for further analysis and visualization. In this article, I will share my journey and highlight how I leveraged the capabilities of Google Cloud to seamlessly go from web scraping to data visualization.

## Web -Scraping
I have done web scraping from amazon website , using beautiful soup .I have scraped details such as such as title, price, rating, brand, and specifications from the Amazon website.
Medium Artcile -https://medium.com/@harshithareti/web-scraping-amazon-e-commerce-extracting-mobile-phone-data-2ea18a2eabb

## Uploading Web-Scraped Data to Google Cloud
 I uploaded the web-scraped data from Amazon to Google Cloud. This involved utilizing a virtual machine with machine learning capabilities, specifically the MAGE AI, which I downloaded from the console. Through this virtual machine, I efficiently extracted and transformed the data.

## Cleaning and Transforming the Data (ETL) 
I have done extract transform load using Mage AI . This involved extracting numerical value froma string ,handling missing values, removing duplicates, standardizing formats, correcting errors, and transforming data types

## Loading Cleaned Data into BigQuery
Once I had cleaned and transformed the data, I loaded it into Google's data warehousing solution, BigQuery. BigQuery is a fully managed, highly scalable data warehouse that enables fast and efficient data querying.

## Data Visualization with Looker Studio
To visualize the cleaned data, I turned to Looker Studio, Google's data visualization tool. By connecting Looker Studio to BigQuery, I was a This enabled me to gain valuable insights through intuitive visualizations, enhancing my understanding of the data.




![data_visualization- Made with Clipchamp](https://github.com/harshith20/Amazon_data_ETL/assets/73159496/9cf07a0b-f816-495c-b3ce-3c338441411a)



## Conclusion
Throughout my journey, I followed a step-by-step process, from uploading web-scraped data to Google Cloud, to cleaning and transforming the data using a virtual machine, loading it into BigQuery, and ultimately visualizing it using Looker Studio. This comprehensive workflow allowed me to unlock the full potential of my web-scraped datasets, enabling me to extract meaningful insights.

Join me on this data journey with Google Cloud and experience firsthand how data transformation and visualization can reveal valuable insights from web-scraped data. Discover the power of Google Cloud and unleash the potential of your data like never before!
