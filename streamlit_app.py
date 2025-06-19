import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


html_content = f"""
<iframe
    src= "https://pdfobject.com/pdf/sample.pdf",
    style="width: 100%; height: 500px"
    type="application/pdf"
    frameborder="0"
></iframe>
"""

st.markdown(html_content, unsafe_allow_html=True)