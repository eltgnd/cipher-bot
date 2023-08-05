import streamlit as st
from ciphers import simple_col as cipher
from text import simple_columnar_transposition_cipher as info
from text import simple_columnar_function as code_text
from set_page import set_page

# Set-up
title = 'Simple Columnar Cipher 📅'
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
st.number_input('Key', 1, key='num')
st.text_area('Type your plaintext below.', key='message')

if not (st.session_state.num == 1 and len(st.session_state.message) == 0):
    if st.session_state.num >= len([i for i in st.session_state.message if i.isalpha()]):
        st.button(st.session_state.job, disabled=True)
        st.error("Key must be less than input length.", icon='⚠️')
    else:
        if st.button(st.session_state.job):
            translated = cipher(st.session_state.job[0].lower(), st.session_state.message, st.session_state.num)
            st.caption('Output')
            st.write(translated)
        else:
            st.caption('No output yet!')
