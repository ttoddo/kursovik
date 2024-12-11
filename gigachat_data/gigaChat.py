from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat


model = GigaChat(
    credentials="ZmI1MjU5MGMtNjFmNi00MGYxLThmOTMtMmM4YmRkMjIwMDEwOjg3NmY4Njk0LTk5MzctNGNmZS04MzNkLTZmNjc3MWJhZWQ1Nw==",
    scope="GIGACHAT_API_PERS",
    model="GigaChat-Pro",
    streaming=False,
    verify_ssl_certs=False,
)

messages = [
]

