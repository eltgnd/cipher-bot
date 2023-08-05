import streamlit as st
from ciphers import rot13 as cipher
from text import atbash_function as code_text
from set_page import set_page

title = 'CipherBot 💻'
set_page(title)

# playfair, rail fence, autokey, hill, one-time pad

st.title('CipherBot 🤖')
st.write('Delve into the intriguing world of classical cryptography. CipherBot is an educational web app that features classic cryptography techniques. **Understand the magic behind the codes that kept secrets safe throughout history** and learn how simple shifts in letters and mathematical functions can beautifully conceal plaintext into cryptic codes. ✨')

st.subheader('What can CipherBot do?')
st.write("""On CipherBot, you'll find detailed explanations of various classic ciphers. Each cipher is presented with a short description, a comprehensive guide explaining how it works, a security rating, and sample code written in Python.""")

expand=False
with st.expander('**Step-by-step guides** ⚒️', expanded=expand):
    st.write('Each featured cipher comes with a comprehensive explanation, illuminating how they transform plain text into secret code. Here\'s an example for the infamous Caesar cipher:')
    st.caption("""1. Decide on a shift value, this will be your encryption key.\n2. For each letter in your plaintext, shift it over by the encryption key. So, if your key is 3, an 'A' becomes 'D', a 'B' becomes 'E', and so on. For letters at the end of the alphabet, loop back to the start. So, a 'Z' with a key of 1 becomes 'A'.\n3. This gives you your ciphertext. To decrypt, just do the same process in reverse.""")
    st.write('\n')
with st.expander('**Interactive tool** 👆', expanded=expand):
    st.write('Each cipher comes with an integrated tool that allows everyone to try out the cipher for themselves. They can encrypt, decrypt, and even brute force the ciphers where feasible. Try out the ROT13 cipher as an example!')
    st.text_input('Type your plaintext below.', key='message')
    if st.button('Transform'):
        st.balloons()
        translated = cipher(st.session_state.message)
        st.write(translated)

with st.expander('**Sample code** 🧑‍💻', expanded=expand):
    st.write('Each featured cipher also includes a Python implementation to better understand the algorithmic processes involved. Here\'s a code snippet for the Atbash cipher!')
    st.code(code_text)




# tool to easily encrypt and decrypt classic cryptography techniques


st.subheader('Get started')
st.write('To get started, choose a cipher to use in the sidebar.')

import os
print(os.path.basename(__file__))