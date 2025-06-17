import pandas as pd
from sqlalchemy import create_engine
import os

CSV_FOLDER = './dataset'
csv_files = {
    # 'application_train.csv': 'application_train',
    'application_test.csv': 'application_test',
    'bureau_balance.csv': 'bureau_balance',
    'bureau.csv': 'bureau',
    'credit_card_balance.csv': 'credit_card_balance',
    'installments_payments.csv': 'installments_payments',
    'POS_CASH_balance.csv': 'pos_cash_balance',
    'previous_application.csv': 'previous_application',
    'sample_submission.csv': 'sample_submission'
    
    # 'HomeCredit_columns_description.csv': 'columns_description'  # optional
}

engine = create_engine('postgresql+psycopg2://postgres:Password123@localhost:5432/home_credit_risk')

# Import loop
for filename, table_name in csv_files.items():
    file_path = os.path.join(CSV_FOLDER, filename)
    
    if os.path.exists(file_path):
        print(f'📥 Importing {filename} → table `{table_name}`...')
        df = pd.read_csv(file_path)
        df.to_sql(table_name, engine, index=False, if_exists='replace')
        print(f' Done importing {table_name}.')
    else:
        print(f' File not found: {file_path}')

