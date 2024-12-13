from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat

model = GigaChat(
    credentials="ZmI1MjU5MGMtNjFmNi00MGYxLThmOTMtMmM4YmRkMjIwMDEwOjg3NmY4Njk0LTk5MzctNGNmZS04MzNkLTZmNjc3MWJhZWQ1Nw==",
    scope="GIGACHAT_API_PERS",
    model="GigaChat-Pro",
    streaming=False,
    verify_ssl_certs=False,
)


async def send_message(type_of_work, botRole):
    messages = []
    print(botRole)
    answer = "А вот и не вышло"
    if botRole != '':
        messages.append(SystemMessage(content=botRole))
    if type_of_work == 'analyze':
        messages.append(SystemMessage(content='Ты бот аналитик, который выполняет функцию '
                                              'анализировать и логически рассуждать'))
        answer = 'dada-ya analizituyu'
    elif type_of_work == 'brainStorm':
        messages.append(SystemMessage(content='Ты бот аналитик, который выполняет функцию '
                                              'анализировать и логически рассуждать'))
        answer = 'dada-ya shturmovik'
    elif type_of_work == 'genIdeas':
        messages.append(SystemMessage(content='Ты бот, который генерирует идеи '
                                              'твоя задача генерировать идеи в ответ на запрос'))
        answer = 'dada-ya generiruyu'
    elif type_of_work == 'chat':
        messages.append(SystemMessage(content='ты просто чат-бот'))
        answer = 'dada-ya obschauys'
    print(messages)
    return answer
