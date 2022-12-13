import streamlit as st
from json import loads
from pandas import read_csv


arquivo = st.file_uploader(
    'Suba o arquivo: ',
    type=['mp4','jpg','png','py','wav','csv','json']
)

if arquivo:
    print(arquivo.type)
    match arquivo.type.split('/'):
        case "application","json":
            st.json(loads(arquivo.read()))
        case "image",_:
            st.image(arquivo)
        case "text","scv":
            df =read_csv(arquivo)
            st.dataframe(df)
        case"text", "x-python":
            st.code(arquivo.read().read())
        case "audio",_:
            st.audio(arquivo)
        case "video",_:
            st.video(arquivo)
else:
    st.error("Arquivo não identificado.")
