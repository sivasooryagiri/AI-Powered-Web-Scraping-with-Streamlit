import streamlit as st
from scrape import scrape_website,extract_body_content,clean_body_content,split_dom_content
from parse import  parse_with_ollama

st.title("AI Web Scraper")
url= st.text_input("Enter a website URL: ")

if st.button("Scrape Site"):
  st.write("Scraping the Website")

  raw_dom = scrape_website(url)
  body_content = extract_body_content(raw_dom)
  cleaned_content = clean_body_content(body_content)

  st.session_state.dom_content=cleaned_content
  
  with st.expander("View DOM Contents"):
    st.text_area("DOM Content", cleaned_content, height=300)
if "dom_content" in st.session_state:
  parse_description=st.text_area("Describe what you want to prase?")

  if st.button("Prase Content"):
    if parse_description:
      st.write("Prasing the content")

      dom_chunks=split_dom_content(st.session_state.dom_content)
      result = parse_with_ollama(dom_chunks,parse_description)
      st.write(result)
      print(result)

# streamlit run main.py