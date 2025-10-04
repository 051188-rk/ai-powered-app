# helper to display streaming responses in Streamlit
import streamlit as st
import time

def stream_response(container, generator):
    placeholder = container.empty()
    full = ''
    for chunk in generator:
        full += chunk
        placeholder.markdown(full + '▌')
        # small sleep to keep UI responsive
        time.sleep(0.01)
    placeholder.markdown(full)
    return full
