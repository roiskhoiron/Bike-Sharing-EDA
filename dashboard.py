# Daftar library yang digunakan
import streamlit as st
from streamlit_option_menu import option_menu
from module.about import about
from module.wrangling import wrangling
from module.exploratory import exploratory
from module.explanatory import explanatory
from module.conclusion import conclusion

def on_change(key):
    selection = st.session_state[key]
    st.header(f'{selection} :bike: Bike Sharing :sparkles:')


# Dictionary untuk switch case
menu_options = {
    "Resume": about,
    "Data Wrangling": wrangling,
    "Exploratory Data Analysis (EDA)": exploratory,
    "Visualization & Explanatory Analysis": explanatory,
    "Conclusion": conclusion
}

with st.sidebar:
    selected = option_menu("Main Menu", ["Resume", "Data Wrangling", 'Exploratory Data Analysis (EDA)', 'Visualization & Explanatory Analysis', 'Conclusion'],  default_index=0, on_change=on_change, key='menu')

# Menampilkan konten berdasarkan pilihan menu menggunakan dictionary
if selected in menu_options:
    menu_options[selected]()
else:
    st.write("Please select a valid option from the menu.")
