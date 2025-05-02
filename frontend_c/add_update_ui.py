import streamlit as st
from datetime import datetime
import requests

api_url = 'http://127.0.0.1:8000'

def add_update_tab():
    selected_date = st.date_input('Enter Date', label_visibility='collapsed')
    response = requests.get(f'{api_url}/expenses/{selected_date}')
    if response.status_code == 200:
        existing_expenses = response.json()
    else:
        st.error('failed to retrieve expenses')
        existing_expenses = []
    expenses_in = []
    categories = ['Rent', 'Food', 'Shopping', 'Entertainment', 'Other']
    with st.form(key='expense_form'):
        for i in range(8):
            if i < len(existing_expenses):
                amount = existing_expenses[i]['amount']
                category = existing_expenses[i]['category']
                note = existing_expenses[i]['notes']
            else:
                amount = 0.0
                category = categories[2]
                note = ''
            col1, col2, col3 = st.columns(3)
            visibility = 'visible' if i == 0 else 'collapsed'
            with col1:
                amount_in = st.number_input(label='Amount', min_value=0.0, step=1.0, value=amount, key=f'amount_{i}',
                                            label_visibility=visibility)
            with col2:
                category_in = st.selectbox(label='Category', options=categories, index=categories.index(category),
                                           key=f'category_{i}', label_visibility=visibility)
            with col3:
                note_in = st.text_input(label='Note', value=note, key=f'note_{i}', label_visibility=visibility)
            expenses_in.append(
                {'amount': amount_in, 'category': category_in, 'notes': note_in}
            )
        filtered_expense_in = [i for i in expenses_in if i['amount'] > 0]
        submit_button = st.form_submit_button('Submit')

        if submit_button:
            send_req = requests.post(f'{api_url}/expenses/{selected_date}', json=filtered_expense_in)
            if send_req.status_code == 200:
                st.success('Submitted Successfully')
            else:
                st.error('Please Retry')