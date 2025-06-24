# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.prompts import PromptTemplate
# from langchain_community.utilities import GoogleSerperAPIWrapper
# from langgraph.prebuilt import create_react_agent
# from langchain_core.messages import (
#     HumanMessage,
#     AIMessage,
#     SystemMessage,
#     trim_messages
# )
# #
#
# import json
# import dotenv
# import os
#
# # завантажити api ключі з папки .env
# dotenv.load_dotenv()
#
# # отримати сам ключ
# api_key = os.getenv('GEMINI_API_KEY')
#
# # створення чат моделі
# # Велика мовна модель(llm)
#
# llm = ChatGoogleGenerativeAI(
#     model='gemini-2.0-flash',  # назва моделі
#     google_api_key=api_key,    # ваша API
# )
#
# # інструмент
# # функція яка надає інформацію про погоду в місті
# def get_weather(city: str, time: str):
#     """
#     Отримує інформацію про погоду в певному місті в певний час.
#
#     Варіанти для параметра час:
#     * конкретна година -- 10:00, 15:40
#     * день -- понеділок, четвер
#     * дата -- 25 грудня
#     * слова 'завтра', 'сьогодні'
#
#     :param city: str, назва міста
#     :param time: str, час
#
#     :return: dict, опис погоди
#     """
#     print("hello from get_weather")
#
#     data = {
#         "name": city,
#         "temperature": 21,
#         "wind_speed": 2.1
#     }
#
#     return data
#
#
# def product(num1: int, num2: int):
#     """
#     Повертає добуток чисел
#     """
#
#     print('hello from product')
#     return num1*num2
#
#
# # інструмент по доступу до інтернету
# # отримати api
# api_key = os.getenv('SERPER_API_KEY')
# searcher = GoogleSerperAPIWrapper(serper_api_key=api_key)
#
# def seacrh_internet(query: str):
#     """
#     Шукає в інтернеті інформацію по запиту користувача
#
#     :param query: запит
#     :return: результати пошуку
#     """
#
#     response = searcher.run(query)
#
#     return response
#
#
# # надати доступ до інструмента get_weather
# # створення агента
# # Агент -- llm з великою кількістю інструментів
#
# # agent = create_react_agent(
# #     model=llm,  # модель(чат модель)
# #     tools=[get_weather]  # список з інструментами
# # )
#
# # створення чат бота з агентом
# # історія повідомлень
#
# # messages = [
# #     SystemMessage("""
# #     Ти ввічливий чат бот
# #     """)
# # ]
# #
# # human_message = HumanMessage("Привіт")
# # messages.append(human_message)
# #
# # # використання агента
# # response = agent.invoke({"messages": messages})
# # # response -- це вся історія повідомленнь + відповідь моделі
# #
# # print(response)
# # print(type(response))
# #
# # # отримати відповідь моделі
# # print(response['messages'][-1])
#
# # написання самого чат боту
#
# messages = {"messages": [
#     SystemMessage("""
#     Ти ввічливий чат бот
#     """)
#     ]
# }
#
# agent = create_react_agent(
#     model=llm,  # модель(чат модель)
#     tools=[get_weather, product, seacrh_internet]  # список з інструментами
# )
# #messages = agent.invoke(messages)
#
# while True:
#     # отримати повідомлення від користувача
#     user_text = input('Ви: ')
#
#     # умова зупинки
#     if user_text == '':
#         break
#
#     # змінити тип даних на HumanMessage
#     human_message = HumanMessage(user_text)
#
#     # змінити історію
#     messages['messages'].append(human_message)
#
#     # застосувати модель
#     messages = agent.invoke(messages)
#
#     # агент повертає всю історію повідомлень
#
#     # отримати останнє повідомлення(відповідь моделі)
#     ai_response = messages['messages'][-1]
#
#     # вивід результату
#     print(f"AI: {ai_response.content}")
#
#     # вивід всієї історії
#     print('\nІсторія')
#     for message in messages['messages']:
#         print(repr(message))
#     print()
# __________________________________________________________________________

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_community.utilities import GoogleSerperAPIWrapper
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
    trim_messages
)
#

import json
import dotenv
import os

from pyexpat.errors import messages

# завантажити api ключі з папки .env
dotenv.load_dotenv()

# отримати сам ключ
api_key = os.getenv('GEMINI_API_KEY')
api_key_serper = os.getenv('SERPER_API_KEY')

# створення чат моделі
# Велика мовна модель(llm)

llm = ChatGoogleGenerativeAI(
    model='gemini-2.0-flash',  # назва моделі
    google_api_key=api_key,    # ваша API
)
#
#  Завдання 1
# Напишіть функцію яка перевіряє складність паролю:
#  кількість символів(>8)
#  наявність хоча б однієї літери\цифри\спеціального
# символу
#  наявність літер в різних регістрах
# Функція повертає тест з описом паролю(що добре, а що
# погано)
# На основі цієї функції створіть агента.


# def check_password(password: str):
#     '''
#     Перевіряє пароль на надійність
#
#     :param password: str, Пароль від користовача
#     :return: dict, Звіт по надійності паролю
#     '''
#     result = {}
#     if len(password) > 8:
#         result['довжина'] = 'добре'
#     else:
#         result['довжина'] = 'погано'
#
#     flag1 = False
#     flag2 = False
#     flag3 = False
#     flag4 = False
#     flag5 = False
#
#     for symb in password:
#         if symb.isdigit():
#             flag1 = True
#         elif symb.isalpha():
#             flag2 = True
#             if symb.isupper():
#                 flag4 = True
#             else:
#                 flag5 = True
#         else:
#             flag3 = True
#
#     result['Чи є цифра в паролі?'] = flag1
#     result['Чи є буква в паролі?'] = flag2
#     result['Чи є особливий символ в паролі?'] = flag3
#     result['Чи є хоч одна велика буква в паролі?'] = flag4
#     result['Чи є хоч одна маленька буква в паролі?'] = flag5
#
#     return result
#
# agent = create_react_agent(
#     model=llm,
#     tools=[check_password]
# )
#
# messages = {'messages': [
#     SystemMessage('Ти ввічливий чат бот по перевірянню паролів')
# ]}
#
# while True:
#     user = input('Ви: ')
#     if user == '':
#         break
#
#     human = HumanMessage(user)
#     messages['messages'].append(human)
#     messages = agent.invoke(messages)
#     result = messages['messages'][-1]
#     print(f'Чат бот: {result.content}')
#
#__________________________________________________________________
# Завдання 2
# Напишіть модель показує останні новини про певну
# людину. Якщо користувач вводить не ім’я людини, то вивести
# повідомлення «немає відповідної інформації»

searcher = GoogleSerperAPIWrapper(api_key_serper = api_key_serper)

def human_info_search(name: str):
    """
    Шукає останню новину про людину.

    :param name: str, імя людини
    :return: str, Результати пошуку останніх новин про людину.
    """

    result = searcher.results(f"Знайди останні новини про таку людину: {name}.")

    data = []
    for r in result['organic']:
        new_data = {'title': r['title'], 'link': r['link'], 'snippet': r['snippet']}
        data.append(new_data)

    print(result)

    return data

agent = create_react_agent(
    model = llm,
    tools = [human_info_search]
)

messages = {"messages":[
    SystemMessage("""
    Ти чат бот.
    Твоя задача отримувати від користувача імя людини та шукати останні новини про неї.
    Якщо користувач ввів не імя людини, то треба повідомити вивести повідомлення «немає відповідної інформації».
    Кожну новину виводь з нової строки.""")
]}

while True:
    user = input("Ви: ")

    if user == '':
        break

    user = HumanMessage(user)

    messages["messages"].append(user)

    messages = agent.invoke(messages)

    result = messages["messages"][-1]

    print(result.content)

