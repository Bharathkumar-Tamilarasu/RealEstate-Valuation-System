import streamlit as st
from about import show_about_page
from predict_page import show_predict_page
from dataset import show_dataset_page
from streamlit_option_menu import option_menu

st.title("RealEstate Valuation System 🏘")

selected = option_menu(
    menu_title=None,
    options=["Prediction", "About", "Dataset"],
    icons=["graph-up", "info-circle", "database-exclamation"],
    menu_icon=["list"],
    default_index=0,
    orientation="horizontal",
)

if selected == "About":
    show_about_page()
elif selected == "Prediction":
    show_predict_page()
elif selected == "Dataset":
    show_dataset_page()
