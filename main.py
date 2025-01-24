import streamlit as st
import io 
from PIL import Image
import base64
import ollama

st.subheader('Input')
image_input = st.file_uploader('',type=['png','jpg','jpeg'])

if image_input:
    st.image(image_input)
    image=Image.open(image_input)
    buffered = io.BytesIO()
    image.save(buffered,format='PNG')
    image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    st.image(image_input)


    describe = ollama.chat(
        model = 'llama3.2-vision',
        messages = [{
            'role':'user',
            'content' : """Please describe the drawing in detail. 
                            Try to understand the style.
                            If possible mention the artist.
                            Can you analyze the proportions of the character? 
                            Do they look too out of proportion? 
                            What improvements can you suggest? 
            """,
            'images' : [image_base64]
        }]
    )

    with st.expander('Image Description'):
        st.markdown(
            f"""
            <div style = "color : gold; padding: 10px; line-height: 1.6;">
            {describe['message'].content}
            """,
            unsafe_allow_html=True
        )