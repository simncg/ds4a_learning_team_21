COPY financial_radar.stock_price
FROM 's3://learning-team-21/processed/stock_price.csv'
IAM_ROLE 'arn:aws:iam::aws_account_id:role/redshift_s3_role'
REGION 'us-east-1'
FORMAT AS CSV
IGNOREHEADER 1
DELIMITER ',';


COPY financial_radar.balance_sheet_annual
FROM 's3://learning-team-21/processed/balance_sheet_annual.csv'
IAM_ROLE 'arn:aws:iam::aws_account_id:role/redshift_s3_role'
REGION 'us-east-1'
FORMAT AS CSV
IGNOREHEADER 1
DELIMITER ',';



COPY financial_radar.balance_sheet_quarterly
FROM 's3://learning-team-21/processed/balance_sheet_quarterly.csv'
IAM_ROLE 'arn:aws:iam::aws_account_id:role/redshift_s3_role'
REGION 'us-east-1'
FORMAT AS CSV
IGNOREHEADER 1
DELIMITER ',';



COPY financial_radar.cash_flow_statement_annual
FROM 's3://learning-team-21/processed/cash_flow_statement_annual.csv'
IAM_ROLE 'arn:aws:iam::aws_account_id:role/redshift_s3_role'
REGION 'us-east-1'
FORMAT AS CSV
IGNOREHEADER 1
DELIMITER ',';



COPY financial_radar.cash_flow_statement_quarterly
FROM 's3://learning-team-21/processed/cash_flow_statement_quarterly.csv'
IAM_ROLE 'arn:aws:iam::aws_account_id:role/redshift_s3_role'
REGION 'us-east-1'
FORMAT AS CSV
IGNOREHEADER 1
DELIMITER ',';



COPY financial_radar.income_statement_annual
FROM 's3://learning-team-21/processed/income_statement_annual.csv'
IAM_ROLE 'arn:aws:iam::aws_account_id:role/redshift_s3_role'
REGION 'us-east-1'
FORMAT AS CSV
IGNOREHEADER 1
DELIMITER ',';



COPY financial_radar.income_statement_quarterly
FROM 's3://learning-team-21/processed/income_statement_quarterly.csv'
IAM_ROLE 'arn:aws:iam::aws_account_id:role/redshift_s3_role'
REGION 'us-east-1'
FORMAT AS CSV
IGNOREHEADER 1
DELIMITER ',';




COPY financial_radar.profile
FROM 's3://learning-team-21/processed/profile.csv'
IAM_ROLE 'arn:aws:iam::aws_account_id:role/redshift_s3_role'
REGION 'us-east-1'
FORMAT AS CSV
IGNOREHEADER 1
DELIMITER ',';



COPY financial_radar.ratios_annual
FROM 's3://learning-team-21/processed/ratios_annual.csv'
IAM_ROLE 'arn:aws:iam::aws_account_id:role/redshift_s3_role'
REGION 'us-east-1'
FORMAT AS CSV
IGNOREHEADER 1
DELIMITER ',';




COPY financial_radar.ratios_quarterly
FROM 's3://learning-team-21/processed/ratios_quarterly.csv'
IAM_ROLE 'arn:aws:iam::aws_account_id:role/redshift_s3_role'
REGION 'us-east-1'
FORMAT AS CSV
IGNOREHEADER 1
DELIMITER ',';


