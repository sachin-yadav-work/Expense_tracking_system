from dotenv import load_dotenv
import os
import mysql.connector
from contextlib import contextmanager
from logger import get_logger

load_dotenv()
logger = get_logger('db_helper','expense_tracking.log')

@contextmanager
def get_cursor(commit = False):
    try:
        connection = mysql.connector.connect(host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"))
        cursor = connection.cursor(dictionary = True)
        logger.info('MySQL connection established')
        yield cursor
        if commit:
            connection.commit()
            logger.info('Transaction Committed')
    except Exception as e:
        logger.error(f'Database error: {e}')

def get_details_by_date(date):
    with get_cursor() as cursor:
        if cursor:
            logger.info(f'Details fetched for date {date}')
            cursor.execute('select * from expenses where expense_date = %s',(date,))
            res = cursor.fetchall()
            logger.debug(f'Query result {res}')
            return res if res else []
        else:
            logger.warning('Cursor not available')
            return []

def insert_data(date,amount,category,notes):
    with get_cursor(commit = True) as cursor:
        cursor.execute('insert into expenses (expense_date,amount,category,notes) values (%s,%s,%s,%s)',(date,amount,category,notes))

def delete_data_by_date(date):
    with get_cursor(commit = True) as cursor:
        cursor.execute('delete from expenses where expense_date = %s',(date,))

def fetch_expense_summary(start_date,end_date):
    with get_cursor() as cursor:
        cursor.execute('''SELECT category, round(sum(amount),2) as total_expense, round(sum(amount)* 100/(select sum(amount) FROM expenses where expense_date between %s and %s),2) as percentage
                                 FROM expenses
                                 where expense_date between %s and %s
                                 group by category
                                 order by total_expense desc''',(start_date,end_date,start_date,end_date))
        res = cursor.fetchall()
        return res

def monthly_expense_analysis():
    with get_cursor() as cursor:
        cursor.execute('''select monthname(expense_date) as Month,sum(amount) as Amount
                          from expenses group by monthname(expense_date) 
                          order by Amount''')
        res = cursor.fetchall()
        return res


if __name__ == '__main__':
    # delete_data_by_date('2025-08-02')
    # get_details_by_date('2025-08-02')
    # insert_data(233,'2025-08-02',1200,'dance','aise hi')
    # get_details_by_date('2025-08-02')
     #print(fetch_expense_summary('2024-08-02','2024-08-06'))
    #print(get_details_by_date('2025-08-01'))
    print(monthly_expense_analysis())