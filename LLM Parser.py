# from langchain_google_genai import GoogleGenerativeAI
# from langchain.prompts import PromptTemplate
# from langchain.output_parsers import ResponseSchema, StructuredOutputParser
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
# # створення моделі
# # Велика мовна модель(llm)
#
# llm = GoogleGenerativeAI(
#     model='gemini-2.0-flash',  # назва моделі
#     google_api_key=api_key,  # ваша API
# )
#
# # Користувач задає питання по книзі
# # Ваша задача:
# # 1. Дати відповідь на питання
# # 2. Порекомендувати схожі книги(на ту саму тему, того ж автора, жанру, ...)
#
# # має назву книги і питання -- хочемо отримати всю інформацію про книгу
# # і відповідь на питання
#
# # маючи інформацію про книгу порекомендувати щось схоже
#
#
# # ------------------------------
#
# # схема для відповідей
# schemas = [
#     ResponseSchema(name='answer', description='відповідь на питання користувача'),
#     ResponseSchema(name='theme', description='головна тема книги'),
#     ResponseSchema(name='author', description='автор книги'),
#     ResponseSchema(name='jaunre', description='жанр книги')
# ]
#
# # створення парсер
# parser = StructuredOutputParser.from_response_schemas(schemas)
#
# # отримати інструкція для llm
# instructions = parser.get_format_instructions()
#
# # print(instructions)
#
# # створення промпта
# prompt = PromptTemplate.from_template(
#     """
#     Ти асистент онлайн книгарні. Твоя задача давати відповіді
#     на питання користувачів. Відповіді мають бути чіткі та інформативні.
#     Загальний стиль спілкування ввічливий, іноді можеш використовувати
#     неформальний стиль.
#     Також ти повинен визначити параметри книжки про яку питає
#     користувач(наприклад жанр, автор, тема, ...)
#
#     Питання: {question}
#
#     Формат відповіді:
#     {instructions}
#     """,
#     partial_variables={"instructions": instructions}
# )
#
# # створення ланцюга
# chain = prompt | llm | parser
#
# response = chain.invoke({
#     "question": "Коли була написана книга 1984",
# })
#
# print(response)
# print(response['theme'])
# print(type(response))
#
# # # збереження у файл
# # with open('response.json', 'w', encoding='UTF-8') as file:
# #     json.dump(response, file)
# #
# # # завантаження з файлу
# # with open('response.json', 'r', encoding='UTF-8') as file:
# #     new_response = json.load(file)
# #
# # print(new_response)
#
#
# # рекомендація схожих книг
# prompt = PromptTemplate.from_template(
#     """
#     Ти асистент онлайн книгарні. Твоя задача давати рекомендації книг
#     користувачам певно жанру, теми та автора. Запропонуй по 3-5 книг по
#     кожному пункту.
#     Загальний стиль спілкування ввічливий, іноді можеш використовувати
#     неформальний стиль.
#
#     Жанр: {jaunre}
#     Автор: {author}
#     Тема: {theme}
#
#     Відповідь дай у вигляді списку, познач які книги до якого
#     пункту відносяться
#     * Книги на схожу тему
#     * Книги того ж автора
#     * Книги того ж жанру
#     """
# )
#
# chain_recommendation = prompt | llm
#
# recommendation = chain_recommendation.invoke({
#     "jaunre": response['jaunre'],
#     "author": response['author'],
#     "theme": response['theme'],
# })
#
# # print(recommendation)
#
# # дістати всі назви книг з рекомендації
#
# schemas = [
#     ResponseSchema(name='books', description='список з назвами книг')
# ]
#
# parser = StructuredOutputParser.from_response_schemas(schemas)
# instructions = parser.get_format_instructions()
#
# prompt = PromptTemplate.from_template(
#     """
#     Твоя задача дістати назви усіх книг з тексту.
#
#     Текст: {text}
#
#     Формат відповіді:
#     {instructions}
#     """,
#     partial_variables={"instructions": instructions}
# )
#
# chain_book_selector = prompt | llm | parser
#
# response = chain_book_selector.invoke({
#     "text": recommendation
# })
#
# print(response)
#
# for book in response['books']:
#     print(book)

# __________________________________________

# Завдання 2
# Напишіть модель для генерації листа:
#  Перший ланцюг отримує короткий опис листа та
# генерує основний зміст
#  Другий ланцюг отримує основний зміст та стиль
# листа(формальний, неформальний, тощо) та генерує
# лист
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser

import json
import dotenv
import os

# завантажити api ключі з папки .env
dotenv.load_dotenv()

# отримати сам ключ
api_key = os.getenv('GEMINI_API_KEY')

# створення моделі
llm = GoogleGenerativeAI(
    model='gemini-2.0-flash',  # назва моделі
    google_api_key=api_key,  # ваша API
    temperature = 0.2
)

shemas = [
    ResponseSchema(name='Content', description='основні пункти листа')
]

parser = StructuredOutputParser.from_response_schemas(shemas)

instructions = parser.get_format_instructions()

prompt = PromptTemplate.from_template(
    """
    Ти помічник в написанні листа. Твоя задача використовуючи опис генерувати основні пункти листа  з 3-5 пунктів. 

    Приклад:
    Опис: Звернення в посольство по отриманню документів.
    Пункти:  Привітання
    Інформація про себе
    Основний запит ( отримання документів)
    Контактна інформація

    Опис: Запит на прийняття на роботу.
    Пункти:  Привітання
    Інформація про себе(досвід роботи, навички)
    Очікування ( очікувана зарплата, умови праці)
    Чому необхідно обрати мене
    Контактна інформація

    Опис: {desc}

    Формат відповіді :{instractions}
    """,
    partial_variables={"instractions": instructions}
)

chain_list = prompt | llm | parser

desc = "Прохання про підвищення зарплати "

response = chain_list.invoke({"desc": desc})

print(response)

#  Другий ланцюг отримує основний зміст та стиль
# листа(формальний, неформальний, тощо) та генерує
# лист
llm = GoogleGenerativeAI(
    model='gemini-2.0-flash',  # назва моделі
    google_api_key=api_key,
    temperature=0.7  # ваша API
)

prompt = PromptTemplate.from_template(
    """
    Ти помічник в написанні листа. Твоя задача використовуючи  основні пункти листа написати лист в певному стилі 

    Пункти: {points}
    Стиль: {style}
    """
)
style = "Офіційний"

chain_letter_creator = prompt | llm

letter = chain_letter_creator.invoke({
    "points": response["Content"],
    "style": style
})

print(letter)

# Завдання 3
# Напишіть модель для генерації резюме:
#  Перший ланцюг отримує опис вакансії та повертає
# основні навички, які необхідні
#  Другий ланцюг отримує основні навички та опис
# кандидата і генерує резюме
#
# from langchain_google_genai import GoogleGenerativeAI
# from langchain.prompts import PromptTemplate
# from langchain.output_parsers import ResponseSchema, StructuredOutputParser
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
# # створення моделі
# # Велика мовна модель(llm)
#
# llm = GoogleGenerativeAI(
#     model='gemini-2.0-flash',  # назва моделі
#     google_api_key=api_key,  # ваша API
# )
#
# # Напишіть модель для генерації резюме:
# #  Перший ланцюг отримує опис вакансії та повертає
# # основні навички, які необхідні
# #  Другий ланцюг отримує основні навички та опис
# # кандидата і генерує резюме
#
# schemas = [
#     ResponseSchema(name='skills', description='список навичок які згадані в вакансії')
# ]
#
# parser = StructuredOutputParser.from_response_schemas(schemas)
# instructions = parser.get_format_instructions()
#
# prompt = PromptTemplate.from_template(
#     '''
#     Твоя задача - дістати всі навички з опису вакансії.
#     Результатом має бути список.
#
#     Опис вакансії:
#     {description}
#
#     Формат відповіді:
#     {instructions}
#     ''',
#     partial_variables={"instructions": instructions}
# )
#
# chain = prompt | llm | parser
#
# with open('vacancy.txt', 'r', encoding='UTF-8') as file:
#     description = file.read()
#
# result = chain.invoke({"description": description})
# print(result)
#
# resume_prompt = PromptTemplate.from_template(
#     '''
#     Твоя задача - написати резюме використовуючи опис кандидата.
#     Для данної вакансії також є список необхідних навичок.
#     Ти повинен використовувати лише навички які знає кандидат.
#
#     Навичкі які вимагаються:
#     {skills}
#     Опис кандидата:
#     {candidate}
#     '''
# )
#
# resume_chain = resume_prompt | llm
#
# candidate = 'Молодий спеціаліст у сфері машинного навчання з ґрунтовними знаннями Python, бібліотек Scikit-learn, Pandas та основ глибокого навчання. Має досвід реалізації невеликих проєктів з класифікації та аналізу даних. Орієнтований на результат, швидко навчається, зацікавлений у розвитку в напрямку MLOps та комп’ютерного зору.'
#
# resume = resume_chain.invoke({
#     'skills': result['skills'],
#     'candidate': candidate
# })
#
# print(resume)