import streamlit as st
from ciphers import caesar as cipher
from text import caesar_cipher as info
from text import caesar_function as code_text
from set_page import set_page

# Set-up
title = 'Caesar Cipher 🥗'
options = ['Encrypt', 'Decrypt', 'Brute Force']
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
offset = 0
if st.session_state.job != 'Brute Force':
    st.number_input('Shift',step=1, key='offset')
    offset = st.session_state.offset
st.text_area('Type your plaintext below.', key='message')

if st.button(st.session_state.job):
    translated = cipher(st.session_state.job[0].lower(), st.session_state.message, offset)
    st.caption('Output')
    if isinstance(translated, str):
        st.write(translated)
    else:
        for i in translated:
            st.text(i)
else:
    st.caption('No output yet!')