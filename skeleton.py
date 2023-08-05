import streamlit as st
from cipher_bot_terminal import rot13 as cipher

# Set-up
title = ''
options = ['Encrypt', 'Decrypt']
classification = ''
description = """"""

def explainer():
    st.write("""" """)

# Information
st.title(title)
st.caption(f'Classification: **{classification}**')
st.write(description)

st.subheader('How it works')
explainer()

# Tool
st.divider()
st.radio('What do you want to do?', options, key='job', horizontal=True)
st.text_area('Input', key='message')

if st.button(st.session_state.job):
    translated = cipher(st.session_state.job[0].lower(), st.session_state.message)
    st.caption('Output')
    st.write(translated)
else:
    st.caption('No output yet!')
