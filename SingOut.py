import credent
import streamlit as st
import singin
from st_pages import Page, show_pages, add_page_title
credent.email = ""
credent.save = False
singin.singout()
st.markdown("""<style>[data-testid="stSidebar"]{visibility: hidden;}</style>""",unsafe_allow_html=True)
st.empty()
