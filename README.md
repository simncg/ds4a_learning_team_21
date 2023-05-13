# Silicon Valley Bank (SVB) Failure: Predictable or Not?
Repository for DS4A project - Learning Team 21

Project Guidelines:

## Project Topic

### Reasoning
Our team chose this topic because it's an important and timely issue in the financial industry. Investigating the predictability of SVB's failure offers valuable insights that can be applied to detect early warning signs in other financial institutions, potentially averting similar situations in the future.

The relevance of this topic can be attributed to several factors:

- Ensuring financial stability: By examining the factors that contributed to SVB's failure, we can better understand the risks and vulnerabilities within the financial sector. This knowledge will help in formulating strategies that promote financial stability, safeguarding the interests of depositors, investors, and the overall economy.
- Regulatory considerations: If we find that SVB's failure was predictable, it raises questions about the effectiveness of current regulations and supervisory practices. Our findings could be valuable for policymakers and regulators to assess and improve existing regulatory frameworks, preventing similar failures in the future.
- Restoring investor confidence: Gaining insights into the factors that led to SVB's failure will help investors make more informed decisions when investing in financial institutions. By shedding light on potential risks and warning signs, we aim to help investors regain confidence in the financial markets. 
- Learning opportunities for the industry: Our investigation into the circumstances surrounding SVB's failure will offer lessons for other financial institutions. By learning from these events, they can enhance their risk management practices and protect their operations from encountering similar issues.

In summary, we believe that exploring the predictability of SVB's failure is both crucial and relevant because it addresses key concerns in the financial sector. Our work has the potential to contribute to the development of strategies that maintain a stable and resilient financial system.


## Client Analysis

### What needs to be measured?
Our team needs to measure various financial data and company information to analyze the predictability of the Silicon Valley Bank (SVB) failure. Specifically, we need to measure:

- Financial statements of all publicly traded financial institutions, including balance sheets, income statements, and cash flow statements. 
- Stock data, such as market capitalization and stock prices. 
- Financial ratios like ROE, ROA, CAR, NIM, and NLP, can help in assessing the financial health of institutions. 
- Basic company information, such as GICS code, sector of activity or industry, headquarters’ location, and number of employees, among others. 
- The end product for this pipeline will be a dashboard comprised of the above information. 

### Who will measure it?
Our data engineering team will be responsible for collecting and processing the data. Once the data is available in the data warehouse, the client (data analyst) will measure and assess the variable to assess the predictability of SVB’s failure and provide insights to inform decision-making. 

### What variables will we be using?
Some of the variables that we will be using include:

- Balance sheet items, such as assets, liabilities, and equity.  
- Income statement items, including revenues, expenses, and net income. 
- Market capitalization and stock prices. 
- Financial ratios (ROE, ROA, CAR, NIM, and NLP) 
- Company information: GICS code, sector, location data (latitude, longitude, county, zip code, etc), number of employees, and branch locations. 

### Time Interval?
The time interval to be measured will cover the period from January 2017 to March 2022. This range allows us to analyze financial data and trends leading up to SVB’s failure, providing a comprehensive view of the factors that could have contributed to the event. 

## Role Delegation & Important Dates

### Team Formation
|Role|Team Member|
|-------------------------------|-----------------------------|
|`Data Modeling + Data Science`|Simón Caicedo|
|`Data Engineering`|Rodney Nuñez|
|`Data Engineering`|Akin Onisile|
|`Data Modeling + Data Science`|Yifei Long|

### Project Timeline
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

### Milestones
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
