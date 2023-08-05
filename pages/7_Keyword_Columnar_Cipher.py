import streamlit as st
from ciphers import keyword_col as cipher
from text import keyword_columnar_cipher as info
from text import keyword_columnar_function as code_text
from set_page import set_page

# Set-up
title = 'Keyword Columnar Cipher 🔑'
options = ['Encrypt', 'Decrypt']
classification, rating_count, explain, description = info
set_page(title)

def explainer():
    st.write(explain)
    st.caption('Note that in this implementation, non-alphabetical characters are ignored.')


# Information
st.title(title)
st.caption(f'Classification: **{classification}**'.upper())
st.markdown(description)
st.caption(f'Security rating: {"🔒" * rating_count}'.upper())

with st.expander('How it works'):
    explainer()
with st.expander('Sample code'):
    st.code(code_text)

# Tool
st.divider()
st.radio('What do you want to do?', options, key='job', horizontal=True)
st.text_input('Keyword', 0, key='keyword', placeholder='Type a keyword (e.g. dog)')
st.text_area('Type your plaintext below.', key='message')

if not (st.session_state.keyword == '0' and len(st.session_state.message) == 0):
    if len(st.session_state.keyword) >= len([i for i in st.session_state.message if i.isalpha()]):
        st.button(st.session_state.job, disabled=True)
        st.error("Keyword length is longer than input length.", icon='⚠️')
    else:
        if st.button(st.session_state.job):
            translated = cipher(st.session_state.job[0].lower(), st.session_state.message, st.session_state.keyword)
            st.caption('Output')
            st.write(translated)
        else:
            st.caption('No output yet!')