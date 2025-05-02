from fastapi import FastAPI
import db_helper as db
from pydantic import BaseModel
from typing import List, Optional, Union
from datetime import date

class Expenses(BaseModel):
    amount: float
    category: str
    notes: str

app = FastAPI()

@app.get('/expenses/{entered_date}',response_model = List[Expenses])
def get_details(entered_date:date):
    return db.get_details_by_date(entered_date)

@app.post('/expenses/{entered_date}')
def add_update_data(entered_date:date,expenses:List[Expenses]):
    db.delete_data_by_date(entered_date)
    for i in expenses:
         db.insert_data(entered_date,i.amount,i.category,i.notes)
    return {'message': "inserted successfully"}

class AnalyticsDateIn(BaseModel):
    start_date: date
    end_date: date

class AnalyticsOut(BaseModel):
    category: str
    total_expense: float
    percentage: float

class DateError(BaseModel):
    message:str

@app.post('/analytics',response_model=Union[List[AnalyticsOut],List[DateError]])
def analytics(dates:AnalyticsDateIn):
    if dates.end_date < dates.start_date:
        return [{'message': 'Please enter valid date range'}]
    else:
        res =  db.fetch_expense_summary(dates.start_date,dates.end_date)
        if res:
            return res
        else:
            return [{'message': 'No Data in given range'}]


class MonthlyExpenses(BaseModel):
    Month:str
    Amount:float

@app.get('/monthly_expense_analytics',response_model=List[MonthlyExpenses])
def monthly_expense_analytics():
    res = db.monthly_expense_analysis()
    return res