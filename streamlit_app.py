import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.markdown("[![Click me](app/static/example.jpg)](https://streamlit.io)")


html_content = f"""
<iframe
    src= "https://pdfobject.com/pdf/sample.pdf",
    style="width: 100%; height: 500px"
    type="application/pdf"
    frameborder="0"
></iframe>
"""

st.markdown(html_content, unsafe_allow_html=True)

html_content_2 = f"""
<iframe
    src= "app/static/sample.pdf",
    style="width: 100%; height: 500px"
    type="application/pdf"
    frameborder="0"
></iframe>
"""

st.markdown(html_content_2, unsafe_allow_html=True)