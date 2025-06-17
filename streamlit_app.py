import streamlit as st
from streamlit_extras.pdf_viewer import pdf_viewer
st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

pdf_viewer(
        "https://pdfobject.com/pdf/sample.pdf",
    )