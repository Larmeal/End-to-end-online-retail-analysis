# End-to-end online retail analysis (Data Engineer project)
## Project Overview:
![Flow Chart 2](https://user-images.githubusercontent.com/95965281/192148727-b1acfa5a-c988-46cd-b7b6-38e4fcd288b6.jpg)

This project was created to practice the beginner-level data engineer for understanding the end-to-end data pipeline process starting with the extraction of the raw data to transformation to analytic data and loading to the data warehouse and basic visualization on the dashboard. The project was modified from "Road to Data Engineer" course which was instructed by Mr.Perth and Ms.Fony on [DataTH](https://www.facebook.com/datasciencechill) Facebook fanpage.

## Project Desciption:
The project was simulated to the gift shop in London, named "Worldwide gift shop", Which contains a transnational data set which occurred between 01/12/2018 and 09/12/2019 for a UK-based and registered non-store online retail. on [UCI website](https://archive.ics.uci.edu/ml/datasets/Online+Retail)

Attribute Information:
- InvoiceNo: Invoice number. Nominal, a 6-digit integral number uniquely assigned to each transaction. If this code starts with letter 'c', it indicates a cancellation.
- StockCode: Product (item) code. Nominal, a 5-digit integral number uniquely assigned to each distinct product.
- Description: Product (item) name. Nominal.
- Quantity: The quantities of each product (item) per transaction. Numeric.
- InvoiceDate: Invice Date and time. Numeric, the day and time when each transaction was generated.
- UnitPrice: Unit price. Numeric, Product price per unit in sterling.
- CustomerID: Customer number. Nominal, a 5-digit integral number uniquely assigned to each customer.
- Country: Country name. Nominal, the name of the country where each customer resides.

the objective:
1. Build the report which shows the top 10 best-sellers of products in Thai baht (THB).

Guidelines:
1. Upload the raw data from [Online retail](https://drive.google.com/file/d/1BYej-MzFBptFdbyCavLNCM5Kqy8B250k/view?usp=sharing) to a local database such as **MySQL** for starting the project.
2. Download the raw data to the local machine for transforming the data later, and **Google Cloud Storage** to preserve the raw data.
3. In **extraction step**, you have to collect 2 datasets. including, \
3.1 The transaction data of online retial from [Online retail](https://drive.google.com/file/d/1BYej-MzFBptFdbyCavLNCM5Kqy8B250k/view?usp=sharing). \
3.2 The British Pounds (GBP) exchange rate to convert the "UnitPrice" column from GBP to THB from [GBP exchange rate API](https://de-training-2020-7au6fmnprq-de.a.run.app/currency_gbp/all).
4. In **transformation step**, you should clean the data to prepare the analytical data according to the conditions. thus, \
4.1 The "StockCode" column should be 5-digit pure integral number. \
4.2 The "Quantity" and "UnitPrice" value should be more than 0. \
4.3 The "InvoiceDate" should be date column type before ingesting to **BigQuery**. \
4.4 Create the "InvoiceTimeStamp" column which refers to the "InvoiceDate" column and has a timestamp column type. \
4.5 The data must have the "THBprice" column before ingesting to **BigQuery**.
5. Before cleaning the data, Upload the cleaned data to **Google Cloud Storage** to perserve the analytical data
6. In **Loading step**, Build the airflow pipeline in **Composer** service for containing the cleaned data in **Google Cloud Storage** to **BigQuery**
7. And **Final step** Build the report which shows the top 10 best-sellers of products on **Data Studio** based on your design Example by the illustration.
![dashboard 1](https://user-images.githubusercontent.com/95965281/192213230-38c75d02-8377-44a7-bd64-5b094761500b.png) 
![dashboard 2](https://user-images.githubusercontent.com/95965281/192213298-571a0661-1400-4e9a-a45e-1a58d04b2c7a.png)












