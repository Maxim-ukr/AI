#                                                                                       ЗРОБЛЕНО в.1(27-07)
# # streamlit
# import json
# import dotenv
# import os
# from uuid import uuid4
import streamlit as st

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from pinecone import Pinecone, ServerlessSpec
# from langchain_core.documents import Document
from langchain_pinecone import PineconeVectorStore
# from langchain.prompts import PromptTemplate
# from langchain_community.utilities import GoogleSerperAPIWrapper
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    trim_messages,
    SystemMessage
)


# отримати сам ключ
api_key = st.secrets.get('GEMINI_API_KEY')
pinecone_api_key = st.secrets.get('PINECONE_API_KEY')


# _____________КОД З ФАЙЛУ СідьверСредВБ______________________

# ____VDB____
# створення моделі для кодування текстів
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",  # назва моделі
    google_api_key=api_key
)

# створення векторної бази даних
pc = Pinecone(api_key=pinecone_api_key)

# назва таблиці з документами
index_name = "vbd-autism"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,  # назва таблиці
        dimension=768,  # кількість чисел у векторі
        metric="cosine",  # формула для обрахунку схожості
        spec=ServerlessSpec(
            cloud="aws",  # хмарна платформа(Амазон)
            region="us-east-1"  # регіон де знаходиться сервер(впливає на оплату)
        )
    )
    print(f"Created VBD {index_name}")

index = pc.Index(index_name)

vector_store = PineconeVectorStore(
    index=index,
    embedding=embeddings
)

# ____________ створення чат моделі _____________________
# створення LLM моделі
llm = ChatGoogleGenerativeAI(
    model='gemini-2.0-flash',
    google_api_key=api_key,
)

def vbd_doc_ser(user_text: str):
    '''
    Шукає документи, які підходять під питання користувача.
    Ця векторна база даних наукових статей про дослідження у сфері аутизму та корекції цього захворювання.

    :param user_text: str, питання користувача
    :return: list[Document], список знайдених у векторній базі даних документів.
    '''
    print("vbd_doc_ser")
    docs = vector_store.similarity_search(user_text, k=3) #В ПРОДУКТІ, ПІСЛЯ ЗАПОВНЕННЯ БД ЗМІНИТИ НА 10
    return docs


# створення агента
agent = create_react_agent(
    model=llm,
    tools=[vbd_doc_ser]
)

trimmer = trim_messages(
    strategy='last',  # залишати останні повідомлення
    token_counter=len,  # рахуємо кількість повідомлень
    max_tokens=7,  # залишати максимум 7 повідомлення(System, AI, Human)
    start_on='human',  # історія завжди починатиметься з HumanMessage
    # end_on='human',  # історія завжди закінчуватиметься з HumanMessage
    include_system=True  # SystemMessage не чіпати
)

# Велика мовна модель(llm)
# чат бот

# історія повідомлень
# session_state -- сховище для зберігання даних
# session_state -- словник

# якщо це перший запуск і історії повідомленнь ще немає
if 'messages' not in st.session_state:
    # добавляємо system message
    st.session_state['messages'] = [
        SystemMessage("""
    Ти чат-бот, який дає відповіді на питання користувача про аутизм.
    НІКОЛИ не спілкуйся російською мовою. На питання на російській мові ЗАВЖДИ відповідай: "Я НЕ РОЗМОВЛЯЮ РОСІЙСЬКОЮ!" 
    Надавай пріоритет даним, отриманим за допомогою "vbd_doc_ser". 
    ТІЛЬКИ якщо не можеш знайти інформацію за допомогою "vbd_doc_ser" або якщо інформації мало - давай відповідь самостійно.
    Надаючи відповідь на основі "vbd_doc_ser" враховуй дату публікації дослідження.  
    У відповіді надавай посилання на першоджерело, зазначене в векторній базі даних.
    """)
    ]

# запит від користувача
user_text = st.chat_input("Ви: ")

# usert_text може бути None якщо користувач нічого не ввів
# якщо користувач щось написав
if user_text:
    human_massege = HumanMessage(user_text)
    # Чи правильний підхід, що спочатку запитання впихуємо в діалог і передаємо Агенту, який передає ВСЕ це (весь діалог) на ЛЛМ -
    # вона на векторну БД цю всю історію і векторна БД аналізує усю історію спілкування, а не останній запит користувача
    # ТОБТО може правильніше зробити, щоб на векторну передавався тільки останній запит, а вже сама ЛЛМ враховувала історію з
    # урахуванням відповіді Векторної БД. Я так думаю для цього достатньо прописати в промті - "в векторну базу даних відправляй
    # тільки останній запит користувача"?
    st.session_state['messages'].append(human_massege)

    # response = agent.invoke(st.session_state['messages'])
    # Виникає Помилка langgraph.errors.InvalidUpdateError: Expected dict, got [...] говорить про те, що LangGraph очікував
    # результат у форматі dict, але отримав список повідомлень ([SystemMessage(...), HumanMessage(...)]).
    # Переробив як підказав чат
    result = agent.invoke({"messages": st.session_state['messages']})
    response = result["messages"][-1]  # Отримуємо останнє повідомлення від AI

    st.session_state['messages'].append(response)

    st.session_state['messages'] = trimmer.invoke(st.session_state['messages'])

# вивід історії спідкування
for message in st.session_state['messages']:
    text = message.content

    # визначити чиє повідомлення
    if isinstance(message, HumanMessage):
        role = 'human'
    elif isinstance(message, AIMessage):
        role = 'ai'
    else:  # SystemMessage пропускаємо
        continue

#     # вивід повідомлення з міткою
    with st.chat_message(role):
        st.markdown(text)

# _____________________________________________________________________СТРІМЛІТ

# основний заголовок
st.title('Проект «Срібна нитка»') # Silver Thread
st.markdown("<p style='text-align: right;'>«Ми йдемо за ниткою — до розуміння.»</p>", unsafe_allow_html=True) #We follow the thread — to understanding

# простий текст
# st.markdown(" ")
# st.markdown(" ")
st.markdown(" ")
st.markdown('''***Штучний інтелект у допомогу батькам дітей з аутизмом 
(на базі особистої бібліотеки наукових статей ГО "Центр Перспектива").***''')
st.markdown("---")
st.markdown(" ")
