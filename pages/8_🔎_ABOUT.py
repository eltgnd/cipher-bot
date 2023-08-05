import streamlit as st
from set_page import set_page

st.title('About CipherBot 🔎')
st.write('CipherBot is a passion project that sparked from an exploration of classic cryptography.')

st.image("photo.png",width=200)
with st.container():
    st.caption('The Developer')
    st.write("Hi! I'm Val, a sophomore at Ateneo de Manila University. CipherBot was the result of my interest in programming and cryptography. After exploring some cryptography techniques in my 'Mathematics in the Modern World' course, I challenged myself to implement these ciphers algorithmically on Python. I hope this could help students and anyone really, to learn and appreciate cryptography! 🥳")
with st.container():
    st.caption('Contact')
    st.markdown('View CipherBot\'s [GitHub Repository](https://github.com/eltgnd/cipherbot)! 💻')
    st.markdown('Let\'s connect on [LinkedIn](https://www.linkedin.com/in/val-eltagonde-8b6282141/)! 🤝')
    st.markdown('Contact me at val.eltagonde@obf.ateneo.edu. ✉️')
