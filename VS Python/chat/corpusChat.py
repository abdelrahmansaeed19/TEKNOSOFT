from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request

app = Flask(__name__)

bot = ChatBot("chatbot", read_only = False, logic_adapters = [
  {"import_path":"chatterbot.logic.BestMatch", 
   "default_response":"Sorry, i'm still learning",
   "maximum_similarity_threshold": 0.9
   }])

trainer = ChatterBotCorpusTrainer(bot)

trainings = ['english', 'spanish', 'bangla', 'chinese', 'french', 'german', 'hebrew', 'hindi', 'italian', 'portuguese']

for i in range(len(trainings)):
  trainer.train("chatterbot.corpus." + trainings[i])

@app.route("/")
def main():
  return render_template("index.html")

# while True:
#   print("Chatbot:", bot.get_response(input("You: ")))

@app.route("/get")
def get_chatbot_response():
  userText = request.args.get('userMessage')
  return str(bot.get_response(userText))

if __name__ == "__main__":
  app.run(debug=True)
