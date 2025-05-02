import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import altair as alt

api_url = 'http://127.0.0.1:8000'

def analytics_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input('Start Date')
    with col2:
        end_date = st.date_input('End Date')
    button = st.button('Get Analytics')
    payload = {'start_date':start_date.strftime('%Y-%m-%d'),'end_date':end_date.strftime('%Y-%m-%d')}
    if button:
        try:
            response = requests.post(f'{api_url}/analytics',json= payload)
            response.raise_for_status()
            data = response.json()
            if isinstance(data,list) and data and 'message' in data[0]:
                st.error(data[0]['message'])
            else:

                df = pd.DataFrame(data)
                df.columns = ['Category', 'Total Expense', 'Percentage']
                df.sort_values('Percentage', ascending=True, inplace=True)

                st.markdown("#### 💰 Expense Summary by Category")

                chart = alt.Chart(df).mark_bar().encode(
                    x=alt.X('Percentage:Q'),
                    y=alt.Y('Category:N', sort=df['Category'].tolist()),  # Explicit order
                    tooltip=['Category', 'Percentage']
                ).properties(height=400)
                st.altair_chart(chart, use_container_width=True)
                df_cleaned = df.copy()
                df_cleaned['Total Expense'] = df_cleaned['Total Expense'].map(lambda x: f"{x:.2f}")
                df_cleaned['Percentage'] = df_cleaned['Percentage'].map(lambda x: f"{x:.2f}")
                df_cleaned.reset_index(drop = True,inplace = True)
                st.table(df_cleaned)
        except requests.exceptions.RequestException as e:
            st.error(f'Request Failed: {e}')
        except ValueError:
            st.error('Invalid response from server')