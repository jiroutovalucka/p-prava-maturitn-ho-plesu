import streamlit as st


st.set_page_config(page_title="Maturitní ples - Přípravy", page_icon="🎓")


# Vlastní barvy
st.markdown("""
    <style>
    .stApp { background-color: lightpink; }
    h1 { color: black; text-align: center; }
    h2 { color: #db2777; }
    </style>
""", unsafe_allow_html=True)


st.title("🎓 Přípravy na maturitní ples")
st.write("Přehled všeho, co musíme zařídit, a užitečné odkazy.")


st.divider()


# 1. SEKCE: SÁLY
st.header("🏛️ Výběr sálu")
st.markdown("""
- [DK Rumburk](https://www.dk-rumburk.cz/clanky/o-nas-saly.html?id_clanky=414) 
- [Lidová zahrada Varnsdorf](http://www.lidovazahrada.cz/)
- [Pivovar Kocour](https://www.pivovar-kocour.cz/cz/eventy/)
""")


st.divider()


# 2. SEKCE: KAPELA
st.header("🎵 Kapela")
st.markdown("""
- [Hudební skupina U-style](https://u-style.cz/)
- [Corebells](https://www.corebells.cz/) 
""")


st.divider()


# 3. SEKCE: DJ
st.header("🎧 DJ")
st.markdown("""
- [DJ Mathew](https://www.instagram.com/mathew_deejay)
- [DJ Georgedahouse](https://www.instagram.com/georgedahouse)
""")


st.divider()


# 4. SEKCE: MODERÁTOR
st.header("🎤 Moderátor")
st.markdown("""
- [Dan Syrovátka](https://www.instagram.com/dansyrovatka)
""")


# 5. SEKCE: VÝZDOBA
st.header("🎈 Výzdoba")
st.markdown("""
- [Balónkový baron](https://www.instagram.com/balonkovybaron)
""")


st.divider()


# 6. SEKCE: SEZNAM VĚCÍ
st.header("✅ Co je potřeba zařídit")
st.write("Odškrtněte si, co už máme hotové:")


st.checkbox("Rezervovat termín sálu **(ke konci druháku)**")
st.checkbox("Zamluvit kapelu, DJ, moderátora **(ke konci třeťáku)**")
st.checkbox("Téma plesu **(ve třeťáku)**")
st.checkbox("Najít si choreografa **(ve třeťáku)**")
st.checkbox("Zařídit mezivystoupení **(konec třeťáku)**")
st.checkbox("Hledat sponzory **(na začátku čtvrťáku)**")
st.checkbox("Zamluvit fotografy **(začátek čtvrťáku)**")
st.checkbox("Objednat šerpy, skleničky, stužky **(září)**")
st.checkbox("Zařídit stužkovák **(začít v září)**")
st.checkbox("Vytisknout lístky **(říjen/listopad)**")
st.checkbox("Objednat kostýmy **(co nejdříve)**")
st.checkbox("Program plesu **(listopad)**")
st.checkbox("Vybrat hudbu")
st.checkbox("Tombola + lidi **(cca měsíc před plesem)**")

st.checkbox("Text pro moderátora **(po domluvě)**")
