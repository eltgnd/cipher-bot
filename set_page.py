import streamlit as st

def set_page(title=''):

    st.set_page_config(
        page_title=title[:-1],
        page_icon=title[-1]
        # menu_items={
        #     'Get Help': 'https://www.extremelycoolapp.com/help',
        #     'Report a bug': "https://www.extremelycoolapp.com/bug",
        #     'About': "# This is a header. This is an *extremely* cool app!"
        # }
    )