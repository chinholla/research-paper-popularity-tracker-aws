import streamlit as st
import requests
import json

# Define the API endpoint
api_url = "https://fxe5mg7ny3.execute-api.us-east-1.amazonaws.com/dev/scrape"

st.set_page_config(page_title="Query API", page_icon=":mag:")

st.header("ArXiv Paper Search")
# Input box for the query parameter
query = st.text_input('Enter your query:')

# Button to submit the query
if st.button('Submit'):
    # Make the GET request to the API
    response = requests.get(api_url, params={'query': query})
    
    # Display the response
    if response.status_code == 200:
        results = response.json()
        
        if results:
            for result in results:
                title = result.get("title", "No title")
                authors = result.get("authors", "No authors").replace(", ", ", ").replace("\n", "")
                abstract = result.get("abstract", "No abstract").replace("\n", " ").replace("▽ More", "...").replace("△ Less", "")
                
                st.subheader(title)
                st.markdown(f"*Authors:* {authors}")
                st.markdown(f"*Abstract:* {abstract}")
                st.markdown("---")
        else:
            st.write('No results found.')
    else:
        st.write('Error:', response.text)