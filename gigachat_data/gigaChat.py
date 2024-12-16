from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat

model = GigaChat(
    credentials="ZmI1MjU5MGMtNjFmNi00MGYxLThmOTMtMmM4YmRkMjIwMDEwOjg3NmY4Njk0LTk5MzctNGNmZS04MzNkLTZmNjc3MWJhZWQ1Nw==",
    scope="GIGACHAT_API_PERS",
    model="GigaChat-Pro",
    streaming=False,
    verify_ssl_certs=False,
)


async def send_message(type_of_work, botRole, message):
    messages = []
    print(botRole)
    if type_of_work == 'analyze':
        messages.append(SystemMessage(content='Ты бот аналитик, который выполняет функцию '
                                              'анализировать и логически рассуждать'+botRole))
        messages.append(HumanMessage(content=message))
        res = model.invoke(messages)
        messages.append(res)
    elif type_of_work == 'brainStorm':
        messages.append(SystemMessage(content='Твоя функция - это мозговой штурм '
                                              'нужно осмыслить идеи и дать конструктивный ответ'+botRole))
        messages.append(HumanMessage(content=message))
        res = model.invoke(messages)
        messages.append(res)
    elif type_of_work == 'genIdeas':
        messages.append(SystemMessage(content='Ты бот, который генерирует идеи '
                                              'твоя задача генерировать идеи в ответ на запрос'+botRole))
        messages.append(HumanMessage(content=message))
        res = model.invoke(messages)
        messages.append(res)
    elif type_of_work == 'chat':
        messages.append(SystemMessage(content='ты просто чат-бот '+botRole))
        messages.append(HumanMessage(content=message))
        res = model.invoke(messages)
        messages.append(res)
    print(messages)
    return messages[-1].content

