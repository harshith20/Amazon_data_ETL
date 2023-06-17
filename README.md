# Amazon_data_ETL End to End Project


## Introduction
In this  end-to-end project, I leveraged cloud technology to collect data through web scraping, performed ETL operations to transform and clean the raw Data, and then visualized it to gain valuable insights.

## Web -Scraping
I have done web scraping from amazon website , using beautiful soup .I have scraped details such as such as title, price, rating, brand, and specifications from the Amazon website.
To get detailed info
Medium Artcile -https://medium.com/@harshithareti/web-scraping-amazon-e-commerce-extracting-mobile-phone-data-2ea18a2eabb

## Uploading Web-Scraped Data to Google Cloud
 I uploaded the web-scraped data from Amazon to Google Cloud. This involved utilizing a virtual machine with machine learning capabilities, specifically the MAGE AI, which I downloaded from the console. Through this virtual machine, I efficiently extracted and transformed the data.

## Cleaning and Transforming the Data (ETL) 
I have done extract transform load using Mage AI . This involved extracting numerical value froma string ,handling missing values, removing duplicates, standardizing formats, correcting errors, and transforming data types

## Loading Cleaned Data into BigQuery
Once I had cleaned and transformed the data, I loaded it into Google's data warehousing solution, BigQuery. BigQuery is a fully managed, highly scalable data warehouse that enables fast and efficient data querying.

## Data Visualization with Looker Studio
To visualize the cleaned data, I turned to Looker Studio, Google's data visualization tool. By connecting Looker Studio to BigQuery, I was a This enabled me to gain valuable insights through intuitive visualizations, enhancing my understanding of the data.



![Untitled video - Made with Clipchamp](https://github.com/harshith20/Amazon_data_ETL/assets/73159496/829b41d3-9e42-44df-a15f-cb2dbc5337de)



