from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
    trim_messages
)

import json
import dotenv
import os

# завантажити api ключі з папки .env
dotenv.load_dotenv()

# отримати сам ключ
api_key = os.getenv('GEMINI_API_KEY')

# створення чат моделі
# Велика мовна модель(llm)

llm = ChatGoogleGenerativeAI(
    model='gemini-2.0-flash',  # назва моделі
    google_api_key=api_key,    # ваша API
)
#
# # response = llm.invoke("Привіт")
# #
# # print(type(response))
# # print(response)
# # print(repr(response))
#
#
# # # історія спілкування(чат)
# # messages = [
# #     SystemMessage("""
# #     Ти ввічливий чат бот. Твоя заача давати відповіді на питання
# #     користувача.
# #
# #     Закінчуй усі відповіді фразою "Чи залишились іще питання?"
# #     """),
# #     HumanMessage('Привіт'),
# #     AIMessage('Привіт, чим можу допомогти? Чи залишились іще питання?'),
# #     HumanMessage('Яка столиця Франції?'),
# #     AIMessage('Париж. Чи залишились іще питання?'),
# #     HumanMessage("Розкажи пару фактів про це місто")
# # ]
# #
# # response = llm.invoke(messages)
# #
# # print(response.content)
#
# # простий чат бот
#
# # messages = [
# #     SystemMessage("""
# #     Ти ввічливий чат бот. Твоя заача давати відповіді на питання
# #     користувача.
# #
# #     Закінчуй усі відповіді фразою "Чи залишились іще питання?"
# #     """)
# # ]
# #
# # # основний цикл
# # while True:
# #     # отримати повідомлення від користувача
# #     user_text = input('Ви: ')
# #
# #     # умова зупинки
# #     if user_text == '':
# #         break
# #
# #     # змінити тип даних на HumanMessage
# #     human_message = HumanMessage(user_text)
# #
# #     # змінити історію
# #     messages.append(human_message)
# #
# #     # застосувати модель
# #     response = llm.invoke(messages)
# #     # response -- AIMessage
# #
# #     # змінити історію
# #     messages.append(response)
# #
# #     # вивід результату
# #     print(f'AI: {response.content}')
#
# # очищення історії повідомлень
#
# # створення трімер
# trimmer = trim_messages(
#     strategy='last',  # залишати останні повідомлення
#
#     token_counter=len,  # рахуємо кількість повідомлень
#     max_tokens=5,  # залишати максимум 5 повідомлення(System, AI, Human)
#
#     start_on='human',  # історія завжди починатиметься з HumanMessage
#     end_on='human',  # історія завжди закінчуватиметься з HumanMessage
#     include_system=True  # SystemMessage не чіпати
# )
#
# messages = [
#     SystemMessage("""
#     Ти ввічливий чат бот. Твоя заача давати відповіді на питання
#     користувача.
#
#     Закінчуй усі відповіді фразою "Чи залишились іще питання?"
#     """)
# ]
#
# # # основний цикл
# # while True:
# #     # отримати повідомлення від користувача
# #     user_text = input('Ви: ')
# #
# #     # умова зупинки
# #     if user_text == '':
# #         break
# #
# #     # змінити тип даних на HumanMessage
# #     human_message = HumanMessage(user_text)
# #
# #     # змінити історію
# #     messages.append(human_message)
# #
# #     # почистити історію
# #     messages = trimmer.invoke(messages)
# #
# #     # застосувати модель
# #     response = llm.invoke(messages)
# #     # response -- AIMessage
# #
# #     # змінити історію
# #     messages.append(response)
# #
# #     # вивід результату
# #     print(f'AI: {response.content}')
# #
# #     # вивід історії
# #     print('\nІсторія')
# #     for message in messages:
# #         print(repr(message))
# #     print()
#
#
# # теж саме через ланцюг
# chain = trimmer | llm
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
#     messages.append(human_message)
#
#     # застосувати модель
#     response = chain.invoke(messages)
#     # response -- AIMessage
#
#     # змінити історію
#     messages.append(response)
#
#     # вивід результату
#     print(f'AI: {response.content}')
#
#     # вивід історії
#     print('\nІсторія')
#     for message in messages:
#         print(repr(message))
#     print()

# _____________________________________LAB
#
# Завдання 3
# Напишіть чат бота, який допомагає у вивченні
# англійської мови з наступним функціоналом:
#  якщо користувач просить перекласти слово або фразу
# то дається переклад слова та приклад використання в
# реченні
#  якщо користувач просить перекласти речення, то
# дається переклад самого речення, а також пояснення
# граматики, наприклад структура there is\are, питання в
# різних часових формах, тощо.

trimmer = trim_messages(
    strategy='last',  # залишати останні повідомлення

    token_counter=len,  # рахуємо кількість повідомлень
    max_tokens=5,  # залишати максимум 5 повідомлення(System, AI, Human)

    start_on='human',  # історія завжди починатиметься з HumanMessage
    end_on='human',  # історія завжди закінчуватиметься з HumanMessage
    include_system=True  # SystemMessage не чіпати
)

messages = [
    SystemMessage("""
    Ти — помічник з вивчення англійської мови. Твоя задача — перекладати слова або речення, а також надавати прості, зрозумілі пояснення граматики, якщо йдеться про речення.

    # Якщо користувач просить перекласти слово, ти:
    - даєш переклад
    - надаєш приклад речення з цим словом

    # Якщо користувач просить перекласти речення, ти:
    - даєш переклад
    - пояснюєш граматичну структуру, яку вжито

    Використовуй просту мову. Ось кілька прикладів:

    ---

    Користувач: Що означає слово genuine
    Асистент: Переклад: genuine — справжній, щирий.  
    Приклад: She gave me a **genuine** smile.  
    (Вона подарувала мені щиру усмішку.)

    ---

    Користувач: Переклади слово achievement і дай приклад у реченні.
    Асистент: Переклад: achievement — досягнення.  
    Приклад: Climbing Mount Everest was a great **achievement**.  
    (Сходження на Еверест було великим досягненням.)

    ---

    Користувач: Як буде відповідальність англійською
    Асистент: Переклад: responsibility.  
    Приклад: Taking care of a pet is a big **responsibility**.  
    (Піклування про домашню тварину — велика відповідальність.)

    ---

    Користувач: Переклади речення: Я щойно закінчив домашнє завдання.
    Асистент: Переклад: I have just finished my homework.  
    Граматика: Це **Present Perfect** — час, який ми використовуємо для дій, що щойно завершились. Структура: *have/has + дієслово в 3-й формі*.

    ---

    Користувач: На столі є дві книжки.
    Асистент: Переклад: There are two books on the table.  
    Граматика: Структура **there is/are** використовується, щоб сказати, що щось десь є. *There are* — для множини.

    ---

    Користувач: Як сказати: Якби я знав, я б тобі допоміг.
    Асистент: Переклад: If I knew, I would help you.  
    Граматика: Це умовне речення другого типу (Second Conditional), що описує уявну ситуацію. Структура: *if + past simple*, *would + інфінітив*.

    ---

    Користувач: Скажи англійською: Мене звати Оля, і я працюю вчителем.
    Асистент: Переклад: My name is Olya, and I work as a teacher.  
    Граматика: Це **Present Simple** — використовується для фактів і звичних дій. Структура: підмет + дієслово.

    ---

    Продовжуй у такому ж стилі.
    """)

]

while True:
    message = input("Ви: ")

    if message == '':
        break

    human_mes = HumanMessage(message)

    messages.append(human_mes)

    messages = trimmer.invoke(messages)

    response = llm.invoke(messages)

    messages.append(response)

    print(response.content)