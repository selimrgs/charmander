import streamlit as st

st.title("Sifre Analiz Sistemi")

sifre = st.text_input("Sifre giriniz:", type="password")

if sifre:
    puan = 0
    if len(sifre) >= 8: puan += 1
    if any(c.isupper() for c in sifre): puan += 1
    if any(c.islower() for c in sifre): puan += 1
    if any(c.isdigit() for c in sifre): puan += 1
    if any(c in "!@#$%^&*()_+-=" for c in sifre): puan += 1

    if puan <= 2:
        st.write("Durum: Charmander")
        st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/4.png", width=200)
    elif 3 <= puan <= 4:
        st.write("Durum: Charizard")
        st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png", width=250)
    else:
        st.write("Durum: Mega Charizard X")
        st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/10059.png", width=300)
