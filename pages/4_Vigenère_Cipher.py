import streamlit as st
from ciphers import vigenere as cipher
from text import vigenere_cipher as info
from text import vigenere_function as code_text
from set_page import set_page

# Set-up
title = 'Vigenère Cipher 🔐'
options = ['Encrypt', 'Decrypt']
classification, rating_count, explain, description = info
set_page(title)

def explainer():
    st.write(explain)
    st.write('\n')

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
st.text_input('Keyword', key='keyword')
st.text_area('Type your plaintext below.', key='message')

if st.button(st.session_state.job):
    translated = cipher(st.session_state.job[0].lower(), st.session_state.message, st.session_state.keyword)
    st.caption('Output')
    st.write(translated)
else:
    st.caption('No output yet!')
