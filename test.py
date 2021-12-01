from chatterbot import Chatbot
from chaterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Я")

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.russian")

while True:
    try:
        print(chatbot.get_response(input()))
    except KeyboardInterrupt:
        break
