import streamlit as st

st.title("Bienvenue sur votre site de Machine Learning")
st.write('''
    # Toutes nos salutations!
    Nous calculons l'indice de masse corporelle.
''')

weigth=st.number_input("Entrez votre poids (en Kilogrammes) : ")
status=st.radio("Sélectionnez le format de taille : ", ("Mètres", "Centimètres"))

try:
    if status=="Centimètres": bmi=weigth/((st.number_input("Centimeters")/100)**2)
    else: bmi=weigth/(st.number_input("meters")**2)
    button = st.button("Calculer")
    if button:
        st.write("Votre indice de masse corporelle est : ", round(bmi))
        problem="sous poids"
        if bmi>18.5:
            if bmi<25: problem="bonne santé"
            else: problem="surpoids"
        st.error("Alerte! Vous etes en "+problem)
except: pass