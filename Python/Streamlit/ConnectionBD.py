import streamlit as st
import mysql.connector
from datetime import datetime, date

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="financaspessoais"
)
with st.form('Formulário de conta'):

    cursor = banco.cursor()
    banco1 = st.text_input("Nome do banco")
    divida = st.text_input("Nome da divida")
    datatext = st.date_input("Data da Compra:")
    valor = st.text_input("valor da dívida")
    cursor.execute("select id from contabanco where nomebanco = '" + banco1 + "'")
    StrA = cursor.fetchall()
    StrA = (str(StrA).strip('[]'',''()'))
    # data = str(datetime.strptime(str(datatext), "%Y-%m-%d").date())
    # print(type(data)) # trabalhar no tratamento da data
    if st.form_submit_button('ENVIAR'):
        try:
            cursor.execute("insert into dividafixa (nome,data, valor, idmes, idconta) values ('" + divida + "','" + "2022/11/11" + \
                                   "','" + valor + "','" + "1" + "','" + StrA + "')")
            banco.commit()
        except:
            print("Deu ruim")


