import streamlit as st
import requests
import pandas as pd

api_url = 'http://127.0.0.1:8000'
def analytics_by_month_st():
    st.markdown("#### 💰 Expense Summary by Month")
    response = requests.get(f'{api_url}/monthly_expense_analytics')
    df = pd.DataFrame(response.json())
    st.bar_chart(df.set_index('Month'),use_container_width=True)
    df_cleaned = df.copy()
    df_cleaned['Amount'] = df_cleaned['Amount'].map(lambda x: f'{x:.2f}')
    st.table(df_cleaned)