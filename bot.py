from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from flask import Flask
import threading

# Фейковый веб-сервер для Render
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Бот работает!"

def run_flask():
    flask_app.run(host='0.0.0.0', port=10000)

# Сам бот
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я — твой бот-трансформер ✨")

app = ApplicationBuilder().token("7490490193:AAG8fggplEnB33WzOutnwgy8SAIj8Fw2ZFE").build()
app.add_handler(CommandHandler("start", start))

# Запуск Flask и бота
threading.Thread(target=run_flask).start()
app.run_polling()
