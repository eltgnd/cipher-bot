import streamlit as st
from ciphers import affine as cipher
from text import affine_cipher as info
from text import affine_function as code_text
from set_page import set_page

# Set-up
title = 'Affine Cipher 🧮'
options = ['Encrypt', 'Decrypt', 'Brute Force']
classification, rating_count, explain, description = info
set_page(title)

def explainer():
    st.markdown(explain)
    st.markdown('In our case, m is 26. Thus, possible values of a are: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, and 25.')
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
a,b = 0,0
if st.session_state.job != 'Brute Force':
    st.number_input("'a' value", 1,26,1, key='a')
    st.number_input("'b' value", step=1, key='b')
    a,b = st.session_state.a, st.session_state.b
st.text_area('Type your plaintext below.', key='message')

if a in [1,3,5,7,9,11,15,17,19,21,23,25]:
    if st.button(st.session_state.job):
        translated = cipher(st.session_state.job[0].lower(), st.session_state.message, a,b)
        st.caption('Output')
        if isinstance(translated, str):
            st.write(translated)
        else:
            for i in translated:
                st.text(i)
    else:
        st.caption('No output yet!')
else:
    st.button(st.session_state.job, disabled=True)
    st.error("'a' and 'm' must be coprime!", icon='⚠️')
