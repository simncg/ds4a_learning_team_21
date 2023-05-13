# Silicon Valley Bank (SVB) Failure: Predictable or Not?
Repository for DS4A project - Learning Team 21

Important Project Links: Guidelines, Scoping Document

## Project Topic

### [Reasoning]
Our team chose this topic because it's an important and timely issue in the financial industry. Investigating the predictability of SVB's failure offers valuable insights that can be applied to detect early warning signs in other financial institutions, potentially averting similar situations in the future.

The relevance of this topic can be attributed to several factors:

- Ensuring financial stability: By examining the factors that contributed to SVB's failure, we can better understand the risks and vulnerabilities within the financial sector. This knowledge will help in formulating strategies that promote financial stability, safeguarding the interests of depositors, investors, and the overall economy.
- Regulatory considerations: If we find that SVB's failure was predictable, it raises questions about the effectiveness of current regulations and supervisory practices. Our findings could be valuable for policymakers and regulators to assess and improve existing regulatory frameworks, preventing similar failures in the future.
- Restoring investor confidence: Gaining insights into the factors that led to SVB's failure will help investors make more informed decisions when investing in financial institutions. By shedding light on potential risks and warning signs, we aim to help investors regain confidence in the financial markets. 
- Learning opportunities for the industry: Our investigation into the circumstances surrounding SVB's failure will offer lessons for other financial institutions. By learning from these events, they can enhance their risk management practices and protect their operations from encountering similar issues.

In summary, we believe that exploring the predictability of SVB's failure is both crucial and relevant because it addresses key concerns in the financial sector. Our work has the potential to contribute to the development of strategies that maintain a stable and resilient financial system.


## Client Analysis

### [What needs to be measured?]
Our team needs to measure various financial data and company information to analyze the predictability of the Silicon Valley Bank (SVB) failure. Specifically, we need to measure:

- Financial statements of all publicly traded financial institutions, including balance sheets, income statements, and cash flow statements. 
- Stock data, such as market capitalization and stock prices. 
- Financial ratios like ROE, ROA, CAR, NIM, and NLP, can help in assessing the financial health of institutions. 
- Basic company information, such as GICS code, sector of activity or industry, headquarters’ location, and number of employees, among others. 
- The end product for this pipeline will be a dashboard comprised of the above information. 

### [Who will measure it?]
Our data engineering team will be responsible for collecting and processing the data. Once the data is available in the data warehouse, the client (data analyst) will measure and assess the variable to assess the predictability of SVB’s failure and provide insights to inform decision-making. 

### [What variables will we be using?]
Some of the variables that we will be using include:

- Balance sheet items, such as assets, liabilities, and equity.  
- Income statement items, including revenues, expenses, and net income. 
- Market capitalization and stock prices. 
- Financial ratios (ROE, ROA, CAR, NIM, and NLP) 
- Company information: GICS code, sector, location data (latitude, longitude, county, zip code, etc), number of employees, and branch locations. 

### [Time Interval?]
The time interval to be measured will cover the period from January 2017 to March 2022. This range allows us to analyze financial data and trends leading up to SVB’s failure, providing a comprehensive view of the factors that could have contributed to the event. 

## Data Sources (not final)
### [Background Information]
- All Publically Traded Financial Institutions: NASDAQ Stock Screener
 - Symbol (VARCHAR):
   - Unique identifier for the publicly traded financial institution.
 -Name (VARCHAR):
   - The name of the publicly traded financial institution
 -Last Sale (NUMERIC):
   - The price of the most recent trade for the publicly traded financial institution
 - Net Change (NUMERIC):
   - The change in the price of the publicly traded financial institution since the previous trading day. 
 - % Change (NUMERIC):
   - The percentage change in the price of the publicly traded financial institution since the previous trading day.
- Basic Company Information (GICS code, Sector of activity, HQ & Branch Locations): 
U.S Securities and Exchange Commission
 - Name (VARCHAR):
   - The name of the publicly traded financial institution, as well as additional information about the company's sector, headquarters location, and other details.
   
### [Historic Data]
- Balance sheets, income statements, and cash flow statements
 - Name (VARCHAR):
   - The name of the financial statements for a publicly traded financial institution. These statements provide a snapshot of the financial health of the institution and include information about its assets, liabilities, revenues, expenses, and cash flows.
- Historical NASDAQ Stock Data: NASDAQ, Yahoo Finance, Google Finance
 - Date (DATE):
   - The date for which the historical stock data is being reported.
 - Open (FLOAT):
   - Price per share upon market opening.
 - High (FLOAT):
   - Highest price per share reached during the day's trading period.
 - Low (FLOAT):
   - Smallest price per share reached during the day’s trading period.
 - Close (FLOAT):
   - The price per share of the publicly traded financial institution when the market closes for trading.
 - Adjusted Close (FLOAT):
   - The price per share of the publicly traded financial institution when the market closes for trading on a particular day, adjusted for any dividends or other corporate actions that may have occurred during the day.
 - Volume (INTEGER):
   - The total number of shares of the publicly traded financial institution that were traded during the day's trading period.
 - Quarterly Market Capitalization (FLOAT)
   - The total market value of the publicly traded financial institution, based on the number of outstanding shares of stock and the current market price per share, as of the end of a particular quarter.
   
### [Calculations]
- Financial Ratio Calculations: U.S Securities and Exchange Commission, Macrotrends
  - Name (VARCHAR):
   - Specific financial ratio
 - Current ratio (FLOAT):
   - A liquidity ratio that measures a company's ability to pay off its short-term liabilities with its current assets.
 - Debt-to-equity ratio (FLOAT): 
   - A leverage ratio that indicates the proportion of equity and debt a company is using to finance its assets.
 - Gross profit margin (FLOAT): 
   - A profitability ratio that measures the amount of revenue that exceeds the cost of goods sold, expressed as a percentage of revenue.
 - Return on equity (FLOAT): 
   - A profitability ratio that measures how much profit a company generates from the shareholders' investments.
 - Price-to-earnings ratio (FLOAT): 
   - A valuation ratio that compares a company's current stock price to its earnings per share (EPS).

### [Strengths]
NASDAQ: 
- Provides real-time stock quotes and data.
- Contains a wide range of data on publicly traded companies including financial data, news, and analysis.
- Offers tools for screening stocks based on specific criteria.

U.S Securities and Exchange Commission
- Provides reliable and official information about publicly traded companies.
- SEC filings are required by law, so the data is relatively standardized and consistent.
- Contains a wide range of financial data, which includes financial statements and other relevant information.

Macrotrends
- Provides a wide range of financial data, including historical stock prices, financial ratios, and economic indicators.
- Offers interactive charts and tools for analyzing the data.
- Data is easy to access and download.

Yahoo & Google Finance
- Provides real-time stock quotes and data.
- Offers a wide range of financial data and analysis tools.

### [Weaknesses]
NASDAQ
- Some of the data is only available to paying customers.
- Limited customization options for data extraction.

U.S Securities and Exchange Commission
- Data can be delayed or incomplete, particularly for smaller companies.
- SEC filings can be difficult to parse and analyze, especially for less experienced data engineers.

Macrotrends
- Some of the data is sourced from third-party providers, which can make it less reliable or accurate.
- Data can be limited for smaller or less well-known companies.
- Limited customization options for data extraction.

Yahoo & Google Finance
- Some of the data is sourced from third-party providers, which can make it less reliable or accurate.


## Role Delegation & Important Dates

### [Team Formation]
|Role|Team Member|
|-------------------------------|-----------------------------|
|`Data Modeling + Data Science`|Simón Caicedo|
|`Data Engineering`|Rodney Nuñez|
|`Data Engineering`|Akin Onisile|
|`Data Modeling + Data Science`|Yifei Long|

### [Project Timeline]
|Role|Team Member|
|-------------------------------|-----------------------------|
|`Week 1`|Team Formation & Project Ideas|
|`Week 2`|Idea Finalized; Start Project Scoping|
|`Week 3`|Project Scoping Completed|
|`Week 4`|Data Procurement|
|`Week 5`|Data Storage|
|`Week 6`|Data Modeling: Design|
|`Week 7`|Data Modeling: Implementation|
|`Week 8`|Data Modeling: Testing|
|`Week 9`|Data Modeling: Refinement|
|`Week 10`|Data Modeling: Documentation|
|`Week 11`|Initial Draft of Presentation|
|`Week 12`|Final Draft of Presentation|

### [Milestones]
1. Data Collection
	1. Gather data from various sources such as databases, APIs, and CSV files.
	1. Data Schema Definition. Ensure that the collected data is in the appropriate format for processing and analysis. This includes selecting an appropriate database technology and designing the database schema.
2. Data Preprocessing
	1. Clean and ensure that the collected data is accurate, complete, and consistent.
	1. Includes handling missing or corrupted data, performing feature engineering, and transforming the data into a format suitable for modeling.
3. Data Pipeline Development
	1. Develop and deploy data pipelines to automate the data engineering process.
	1. Use technologies such as Apache Airflow or AWS Glue to schedule and orchestrate data processing tasks.
4. Data Modeling
	1.  Build and test models to predict the likelihood of SVB failure.
	1. Includes testing different algorithms, evaluating their performance using various metrics, and fine-tuning the models to improve their accuracy.
5. Documentation/Presentaton.
	1. Create detailed technical specifications, documenting code and data flows, and providing clear and concise user documentation.
	1. Prepare for the final presentation.
