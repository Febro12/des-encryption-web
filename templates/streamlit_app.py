import streamlit as st
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

st.title("DES Encryption Web")
st.subheader("Kelompok 2 - Keamanan Komputer")

key = b'12345678'

pesan = st.text_input("Masukkan pesan")

if st.button("Encrypt & Decrypt"):

    cipher = DES.new(key, DES.MODE_ECB)

    encrypted = cipher.encrypt(pad(pesan.encode(), DES.block_size))
    decrypted = unpad(cipher.decrypt(encrypted), DES.block_size).decode()

    st.success("Ciphertext")
    st.code(encrypted.hex())

    st.success("Decrypted Text")
    st.code(decrypted)