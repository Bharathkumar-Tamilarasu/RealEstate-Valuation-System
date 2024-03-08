import csv
import streamlit as st
import pandas as pd


def show_dataset_page():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/Bharathkumar-Tamilarasu/RealEstate-Valuation-System/main/cleaned_bengaluru_house_prices.csv"
    )

    rows = int(df.shape[0])
    ip_rows = st.number_input(
        """#### Choose the number of rows you'd like to see:""",
        key=int,
        step=5,
        value=30,
    )

    if ip_rows < rows:
        st.write(f"""#### Displaying the first {ip_rows} rows (Cleaned Data)""")
        st.write(df.head(ip_rows))
    else:
        st.write(f"""#### Displaying all the rows (Cleaned Data)""")
        st.write(df.head(rows))

    st.download_button(
        label="Download Full Dataset",
        data="https://raw.githubusercontent.com/Bharathkumar-Tamilarasu/RealEstate-Valuation-System/main/cleaned_bengaluru_house_prices.csv",
        file_name="House Prices Data_Cleaned.csv",
    )
