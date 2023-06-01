# Silicon Valley Bank (SVB) Failure: Predictable or Not?
Repository for Correlation One's DS4A Data Engineering Program Final Project - Learning Team 21

Important Project Links: [Guidelines](https://drive.google.com/file/d/1FZSqTbi0DSPHU31S9_z4kfHyU1Hv58a9/view?usp=sharing), [Scoping Document](https://docs.google.com/document/d/1dYdz7k2DS9dHGHzhCxIIGScosOromXlmz7MtZj7FWxw/edit?usp=sharing), [GitHub Project](https://github.com/users/rod608/projects/1/views/1?visibleFields=%5B%22Title%22%2C%22Status%22%2C%22Milestone%22%2C%22Assignees%22%2C43218339%2C43219078%2C41561771%5D)

### [Team Formation]
|Role|Team Member|
|-------------------------------|-----------------------------|
|`Data Modeling + Data Science`|Simón Caicedo|
|`Data Engineering`|Rodney Nuñez|
|`Data Engineering`|Akin Onisile|
|`Data Modeling + Data Science`|Yifei Long|

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

## Data Sources 


### **Stock Information:**
  - Symbol (VARCHAR):
    - The unique identifier or ticker symbol for the publicly traded company.
  - Company Name (VARCHAR):
    - The official name of the publicly traded company.
  - Industry Name (VARCHAR):
    - The specific industry in which the company operates.


### **Company Profile**: Obtained via Yahoo Finance API

- Basic Company Information:
  - ticker (VARCHAR): 
    - Identifier of the company 
  - address1 (VARCHAR):
    - The street address of the company's HQ location.
  - city (VARCHAR):
    - The city in which the company's HQ reside.
  - state (VARCHAR):
    - The state in which the company's HQ reside.
  - zip (VARCHAR):
    - The zip code of the company's HQ.
  - country (VARCHAR):
    - The country in which the company's HQ reside.
  - phone (VARCHAR):
    - The main contact phone number for the company.
  - website (VARCHAR):
    - The official website URL for the company.
  - latitude (NUMERIC):
    - The latitude of the company's HQ.
  - longitude (NUMERIC):
    - The longitude of the company's HQ.

- Company Industry and Sector:
  - industry (VARCHAR):
    - The specific industry in which the company operates.
  - industryDisp (VARCHAR):
    - A displayed version of the specific industry in which the company operates.
  - sector (VARCHAR):
    - The general sector in which the company operates.

- Company Overview:
  - longBusinessSummary (TEXT):
    - A detailed description of the company's business model and operations.

- Company Employee Information:
  - fullTimeEmployees (NUMERIC):
    - The number of full-time employees working for the company.

- Company Risk Information:
  - auditRisk (NUMERIC):
    - The risk level associated with the company's audit, higher numbers imply higher risk.
  - boardRisk (NUMERIC):
    - The risk level associated with the company's board of directors, higher numbers imply higher risk.
  - compensationRisk (NUMERIC):
    - The risk level associated with the company's compensation structure, higher numbers imply higher risk.
  - shareHolderRightsRisk (NUMERIC):
    - The risk level associated with shareholder rights, higher numbers imply higher risk.
  - overallRisk (NUMERIC):
    - The overall risk level associated with the company, higher numbers imply higher risk.

  
   
### **Stock Prices Data**: Obtained via Yahoo Finance API 

- Stock Trading Data:
  - symbol (VARCHAR):
    - The unique identifier or ticker symbol for the publicly traded company.
  - date (DATE):
    - The specific date of the recorded trading data.
  - open (NUMERIC):
    - The opening price of the stock for the trading day.
  - high (NUMERIC):
    - The highest price of the stock reached in the trading day.
  - low (NUMERIC):
    - The lowest price of the stock reached in the trading day.
  - close (NUMERIC):
    - The closing price of the stock for the trading day.
  - volume (NUMERIC):
    - The number of shares of the stock that were traded during the trading day.
  - adjclose (NUMERIC):
    - The adjusted closing price of the stock for the trading day. This is typically adjusted for corporate actions such as dividends, stock splits, and new stock offerings.
  - dividends (NUMERIC):
    - The amount of dividends paid out on that trading day.
  - splits (NUMERIC):
    - The split ratio applied to the stock on that trading day. A split ratio of 2, for example, would represent a 2-for-1 stock split.
   
### **Financial Statements**

We obtained data both at the annual and quarterly level

- Balance Sheet Data:
  - Year (DATE): 
    - If it is the annual data, the year in which the data was recorded.
  - Quarter (DATE):
    - If it is the quarterly data, the quarter in which the data was recorded.
  - Cash & Equivalents (NUMERIC): 
    - The company's cash on hand, as well as assets that can be readily converted into cash.
  - Short-Term Investments (NUMERIC): 
    - Investments that are expected to be converted into cash within a year.
  - Cash & Cash Equivalents (NUMERIC): 
    - The sum of cash on hand and short-term investments.
  - Cash Growth (NUMERIC): 
    - The percentage growth in cash and cash equivalents from the previous year.
  - Receivables (NUMERIC): 
    - Money owed to the company by its customers from sales made on credit.
  - Other Current Assets (NUMERIC): 
    - Other assets that can or will be converted into cash within one year.
  - Total Current Assets (NUMERIC): 
    - The total value of all assets that are expected to be converted into cash within one year.
  - Property, Plant & Equipment (NUMERIC): 
    - The company's tangible fixed assets, such as land, buildings, and equipment.
  - Goodwill and Intangibles (NUMERIC): 
    - The value of a company's brand name, solid customer base, good customer relations, good employee relations, and any patents or proprietary technology.
  - Other Long-Term Assets (NUMERIC): 
    - Other assets that cannot be converted into cash within one year.
  - Total Long-Term Assets (NUMERIC): 
    - The total value of long-term assets.
  - Total Assets (NUMERIC): 
    - The total value of all the company's assets.
  - Accounts Payable (NUMERIC): 
    - The amount of short-term debt the company owes to its suppliers or creditors.
  - Current Debt (NUMERIC): 
    - The portion of debt due to be paid within one year.
  - Other Current Liabilities (NUMERIC): 
    - Other obligations due within one year.
  - Total Current Liabilities (NUMERIC): 
    - The total amount of liabilities due within one year.
  - Long-Term Debt (NUMERIC): 
    - The portion of debt that is due more than one year from now.
  - Other Long-Term Liabilities (NUMERIC): 
    - Other obligations due after one year.
  - Total Long-Term Liabilities (NUMERIC): 
    - The total amount of liabilities due after one year.
  - Total Liabilities (NUMERIC): 
    - The total amount of both current and long-term liabilities.
  - Total Debt (NUMERIC): 
    - The total amount of debt, both short-term and long-term.
  - Debt Growth (NUMERIC): 
    - The percentage growth in debt from the previous year.
  - Common Stock (NUMERIC): 
    - The total value of all outstanding common shares.
  - Retained Earnings (NUMERIC): 
    - The portion of net profits not paid out as dividends but instead reinvested in the core business or used to pay off debt.
  - Comprehensive Income (NUMERIC): 
    - The total change in equity for a reporting period other than transactions with owners (like dividends and share repurchases).
  - Shareholders' Equity (NUMERIC): 
    - The net value of the company, calculated by subtracting total liabilities from total assets.
  - Total Liabilities and Equity (NUMERIC): 
    - The sum of total liabilities and total equity. This should be equal to total assets.
  - Net Cash / Debt (NUMERIC): 
    - The difference between a company's cash and its total debt.
  - Net Cash Per Share (NUMERIC): 
    - The net cash per outstanding share of common stock.
  - Working Capital (NUMERIC): 
    - A measure of a company's operational liquidity. It's calculated as current assets minus current liabilities.
  - Book Value Per Share (NUMERIC): 
    - The value of a company if all its assets were sold and all its liabilities were paid off, divided by the number of outstanding shares.


- Cash Flow Statement Data:
  - Year (DATE): 
    - If it is the annual data, this variable is the year in which the data was recorded. 
  - Quarter (DATE): 
    - If it is the quarterly data, this variable is the quarter in which the data was recorded. 
  - Net Income (NUMERIC): 
    - The company's total profit or loss.
  - Depreciation & Amortization (NUMERIC): 
    - The decrease in value of the company's fixed assets due to wear and tear, and the gradual reduction in the value of intangible assets.
  - Other Operating Activities (NUMERIC): 
    - The cash inflows or outflows related to other operations that are not categorized under net income or depreciation & amortization.
  - Operating Cash Flow (NUMERIC): 
    - The cash generated by a company's regular business operations.
  - Operating Cash Flow Growth (NUMERIC): 
    - The percentage growth in operating cash flow from the previous year.
  - Change in Investments (NUMERIC): 
    - The net change in the company's investments over the period.
  - Other Investing Activities (NUMERIC): 
    - The cash inflows or outflows related to other investing activities that are not categorized under change in investments.
  - Investing Cash Flow (NUMERIC): 
    - The cash inflows or outflows from investments.
  - Dividends Paid (NUMERIC): 
    - The total dividends paid to shareholders during the period.
  - Share Issuance / Repurchase (NUMERIC): 
    - The net cash inflow (issuance) or outflow (repurchase) from equity financing.
  - Debt Issued / Paid (NUMERIC): 
    - The net cash inflow (debt issued) or outflow (debt paid) from debt financing.
  - Other Financing Activities (NUMERIC): 
    - The cash inflows or outflows related to other financing activities that are not categorized under dividends paid, share issuance/repurchase, or debt issued/paid.
  - Financing Cash Flow (NUMERIC): 
    - The net cash inflow or outflow from all financing activities.
  - Net Cash Flow (NUMERIC): 
    - The total change in a company's cash and cash equivalents during a period.
  - Free Cash Flow (NUMERIC): 
    - The cash a company generates from its operations that is free to be distributed to investors, calculated as operating cash flow minus capital expenditures.
  - Free Cash Flow Growth (NUMERIC): 
    - The percentage growth in free cash flow from the previous year.
  - Free Cash Flow Margin (NUMERIC): 
    - The free cash flow divided by total revenue, expressed as a percentage. It represents how much free cash flow is generated for each dollar of revenue.
  - Free Cash Flow Per Share (NUMERIC): 
    - The free cash flow divided by the total number of shares outstanding. It indicates the amount of free cash flow available per share.


- Income Statement Data:
  - Year (DATE): 
    - If it is the annual data, this variable is the year in which the data was recorded.

  - Quarter (DATE): 
    - If it is the quarterly data, this variable is the quarter in which the data was recorded.
  
  - Revenue (NUMERIC): 
    - The total money made from selling goods and services.
  - Revenue Growth (YoY) (NUMERIC): 
    - The percentage change in revenue from the previous year.
  - Gross Profit (NUMERIC): 
    - The profit a company makes after deducting the costs associated with making and selling its products, or the costs associated with providing its services.
  - Selling, General & Admin (NUMERIC): 
    - The sum of all direct and indirect selling expenses and all general and administrative expenses of a company.
  - Other Operating Expenses (NUMERIC): 
    - The category of expenditure that a business incurs as a result of performing its normal business operations.
  - Operating Expenses (NUMERIC): 
    - The sum of a business's operating expenses for a period of time.
  - Operating Income (NUMERIC): 
    - The profit realized from a business's operations.
  - Other Expense / Income (NUMERIC): 
    - Expenses or incomes that are unusual, not recurring, or not directly tied to the company's normal operations.
  - Pretax Income (NUMERIC): 
    - The income that a company makes before deducting the income taxes it owes.
  - Income Tax (NUMERIC): 
    - The amount of tax owed to the government based on reported income.
  - Net Income (NUMERIC): 
    - The company's total earnings or profit.
  - Net Income Growth (NUMERIC): 
    - The year-over-year growth rate of net income.
  - Shares Outstanding (Basic) (NUMERIC): 
    - The number of shares that are currently held by all its shareholders, including institutional investors.
  - Shares Outstanding (Diluted) (NUMERIC): 
    - The number of shares that would be outstanding if all possible sources of conversion, such as convertible bonds and stock options, were exercised.
  - Shares Change (NUMERIC): 
    - The percentage change in the number of outstanding shares from the previous year.
  - EPS (Basic) (NUMERIC): 
    - The portion of a company's profit allocated to each outstanding share of common stock.
  - EPS (Diluted) (NUMERIC): 
    - A calculation for earnings per share if all convertible securities were exercised.
  - EPS Growth (NUMERIC): 
    - The percentage change in EPS from the previous year.
  - Free Cash Flow Per Share (NUMERIC): 
    - The amount of free cash flow (cash a company has left over after it has paid expenses, interest, taxes, and long-term investments) allocated to each outstanding share of common stock.
  - Dividend Per Share (NUMERIC): 
    - The total dividends declared divided by the number of outstanding shares.
  - Dividend Growth (NUMERIC): 
    - The year-over-year growth rate of dividends per share.
  - Gross Margin (NUMERIC): 
    - Gross profit divided by revenues, expressed as a percentage.
  - Operating Margin (NUMERIC): 
    - Operating income divided by revenues, expressed as a percentage.
  - Profit Margin (NUMERIC): 
    - Net income divided by revenues, expressed as a percentage.
  - Free Cash Flow Margin (NUMERIC): 
    - Free cash flow divided by total revenue, expressed as a percentage.
  - Effective Tax Rate (NUMERIC): 
    - The average rate at which a company's pre-tax profits are taxed.
  - EBITDA (NUMERIC): 


    - Earnings before interest, taxes, depreciation, and amortization.
  - EBITDA Margin (NUMERIC): 
    - EBITDA divided by total revenue, expressed as a percentage.
  - Depreciation & Amortization (NUMERIC): 
    - The decrease in value of the company's assets over time.
  - EBIT (NUMERIC): 
    - Earnings Before Interest and Taxes, a measure of a firm's profit that includes all incomes and expenses except interest expenses and income tax expenses.
  - EBIT Margin (NUMERIC): 
    - EBIT divided by total revenue, expressed as a percentage.


- Ratios: 

  - Year:  If it is the annual data, this variable is the year in which the data was recorded.

  - Quarter: If it is the quarterly data, this variable is the quarter in which the data was recorded. 

  - Market Capitalization: This is the total value of a company's outstanding shares of stock, calculated by multiplying the share price by the number of outstanding shares.

  - Market Cap Growth: This shows the percentage change in the market capitalization from year to year.

  - Enterprise Value: This is a measure of a company's total value, considering not only its equity (like market capitalization does) but also its debt and cash.

  - PE Ratio (Price/Earnings Ratio): This ratio compares a company's current share price to its earnings per share (EPS).

  - PS Ratio (Price/Sales Ratio): This ratio compares a company's market capitalization with its annual revenue.

  - PB Ratio (Price/Book Ratio): This ratio compares a company's market capitalization to its book value (which is assets minus liabilities).

  - P/FCF Ratio (Price/Free Cash Flow Ratio): This compares a company's market capitalization to its free cash flow.

  - P/OCF Ratio (Price/Operating Cash Flow Ratio): This compares a company's market capitalization to its operating cash flow.

  - EV/Sales Ratio: This compares a company's enterprise value to its annual revenue.

  - EV/EBITDA Ratio: This compares a company's enterprise value to its earnings before interest, tax, depreciation, and amortization (EBITDA).

  - EV/EBIT Ratio: This compares a company's enterprise value to its earnings before interest and tax (EBIT).

  - EV/FCF Ratio: This compares a company's enterprise value to its free cash flow.

  - Debt / Equity Ratio: This measures a company's financial leverage by comparing its total debt with its total equity.

  - Debt / EBITDA Ratio: This compares a company's total debt to its EBITDA.

  - Debt / FCF Ratio: This compares a company's total debt to its free cash flow.

  - Asset Turnover: This ratio measures how efficiently a company uses its assets to generate revenue.

  - Return on Equity (ROE): This ratio measures the profitability of a company in relation to the equity held by shareholders.

  - Return on Assets (ROA): This ratio measures the profitability of a company in relation to its total assets.

  - Return on Capital (ROIC): This ratio measures the return that an investment generates for capital contributors, i.e., bondholders and shareholders.

  - Earnings Yield: This is the inverse of the P/E ratio and shows the percentage of each dollar invested in the stock that was earned by the company.

  - FCF Yield: This is the inverse of the P/FCF ratio and shows the percentage of free cash flow relative to the market capitalization of the company.

  - Dividend Yield: This shows how much a company pays out in dividends each year relative to its share price.

  - Payout Ratio: This measures the proportion of earnings a company pays shareholders in dividends.

  - Buyback Yield / Dilution: This measures the percentage change in the number of outstanding shares due to stock buybacks or dilution.

  - Total Shareholder Return: This measures the return of an investment in a company's stock, including both price appreciation and dividends.


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


## Important Dates & Project Concerns

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

### [Concerns]
- Data Quality: The accuracy and completeness of the data used to build the models could be a concern.
- Data Privacy: The project will involve working with sensitive data that may be subject to privacy regulations. 
- Model Performance & Bias: Since a failure event may be influenced by a variety of factors and some factors may be outside of the control, the accuracy and reliability of the models will be a major concern.
