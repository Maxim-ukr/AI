# Прочитайте файл data/lesson9/return_policy.txt та
# напишіть простий чат для відповідей на питання користувачів
# стосовно повернення товару.
# Діалог завершується коли користувач ввів порожній
# рядок.
# Модель отримує інструкцію з вмістом файлу та всю
# історію спілкування разом з новим повідомленням у форматі
# Instruction: …
# Human: message1
# AI: message2
# Human: message3
# AI: message4

from langchain_google_genai import GoogleGenerativeAI
import dotenv
import os

# завантажити api ключі з папки .env
dotenv.load_dotenv()

# отримати сам ключ
api_key = os.getenv('GEMINI_API_KEY')

with open("data/lesson9/return_policy.txt", "r", encoding="UTF-8") as file:
    instruction = file.read()

llm = GoogleGenerativeAI(
    model='gemini-2.0-flash',  # назва моделі
    google_api_key=api_key,    # ваша API
    #top_k=10,                  # серед скількох найбільш ймовірних слів обирати нове слово
    temperature=0.3,            # температура
    #max_output_tokens=10        # максимальна довжина відповіді у токенах
)

print("Введіть Ваше питання з приводу повернення товару або залиште порожній рядок для закінчення.")

dialog = (f"""Ти чат-бот з питань повернення товару. Правила повернення знаходяться в файлі {instruction}. 
            При спілкуванні будь тактовним.
            Діалог:
            """)

while True:
    question = input("Користувач: ")

    if question == '':
        break

    query = f'''{dialog} 
Користувач: {question}'''

    # print(query)

    answer = llm.invoke(query) # хоча думаю логіка була б краще якби тут при задачі питання ллм ми використовували
    # Ф-рядок Діалог + Квері, а сам квері і ансвер добавлялися б простим += до Діалогу. - Так скоріше б працювало.

    print(answer)

    dialog = f""""{query}.
        AI:{answer}"""