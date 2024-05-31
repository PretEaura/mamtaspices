import streamlit as st
from streamlit.web import cli as stcli
from streamlit import runtime
import sys

# Set page configuration
st.set_page_config(
    page_title="Website Template",
    page_icon=":earth_africa:",
    layout="wide",
    initial_sidebar_state="expanded",
)



# Wide banner
st.image("images/banner.jpg", use_column_width=True)

# Title and subtitle
st.title("Welcome to My Website")
st.subheader("This is a subtitle with a brief introduction.")

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    st.image("images/banner2.jpg", caption="This is an image", use_column_width=True)

with col2:
    st.header("Description")
    st.write("""
        Here you can provide a detailed description of the content, products, or services offered on your website.
        You can also include bullet points:
        - Bullet point 1
        - Bullet point 2
        - Bullet point 3
        """)

# Footer
st.write("---")
st.write("Footer content goes here. © 2024 Your Company Name")

