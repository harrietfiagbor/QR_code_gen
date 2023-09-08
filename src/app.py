import streamlit as st
import segno
from urllib.request import urlopen

st.title('QR Codify')

encode_type = st.radio(
    label="What are you encoding?",
    options=["URL :link",
             "Text :pencil"],
    captions=["Link to the object",
              "A text eg. I love you Enny :love"]
)

encode = st.text_input("What to encode",
                       placeholder="https://my-url or 'Hello World'")

if encode:
    qrcode = segno.make(encode)
    if encode_type == "URL :link":
        url = urlopen(encode)
        qrcode.to_artistic(
        )

        qrcode.save("data.png", scale=5)
    st.image("data.png")
