import streamlit as st
from predict_page import show_predict_page


show_predict_page()

    

# Define the footer content
footer_content = """
<hr>
<p style="text-align:center">Made with ❤️ by Meshach Aderele</p>
"""

# Add the footer
st.markdown(footer_content, unsafe_allow_html=True)