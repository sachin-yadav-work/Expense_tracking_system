import streamlit as st
from datetime import datetime
import requests
from add_update_ui import add_update_tab
from analytics_by_category import analytics_tab
from analytics_by_month import analytics_by_month_st


st.title('Expense Tracking System')

tab_add_update, tab_analytics_category, tab_analytics_month = st.tabs(['Add/Update','Analytics by Category','Analytics by Month'])

with tab_add_update:
    add_update_tab()

with tab_analytics_category:
    analytics_tab()

with tab_analytics_month:
    analytics_by_month_st()