from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Токен вашого бота
BOT_TOKEN = "7455789101:AAGcqz_nbjgchHq0X-fUu5Zn3vfKZ2HVRwI"

# Список системних блоків
systems = [
    {"name": "Системний блок 1", "price": "15000 грн", "description": "Intel i5, 16GB RAM, SSD 512GB"},
    {"name": "Системний блок 2", "price": "20000 грн", "description": "Intel i7, 32GB RAM, SSD 1TB"},
    {"name": "Системний блок 3", "price": "25000 грн", "description": "AMD Ryzen 5, 16GB RAM, SSD 1TB"},
]

# Стартова команда
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(system["name"], callback_data=f"system_{i}")]
        for i, system in enumerate(systems)
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Вітаю! Оберіть системний блок:", reply_markup=reply_markup)

# Обробка вибору системного блоку
async def handle_system_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Отримуємо індекс вибраного блоку
    selected_index = int(query.data.split("_")[1])
    selected_system = systems[selected_index]

    # Відправляємо інформацію про вибраний блок
    message = (
        f"**{selected_system['name']}**\n"
        f"Ціна: {selected_system['price']}\n"
        f"Опис: {selected_system['description']}\n"
        f"Для замовлення напишіть нам у чат!"
    )
    await query.edit_message_text(text=message, parse_mode="Markdown")

# Запуск бота
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_system_selection))

    print("Бот запущений!")
    app.run_polling()

if __name__ == "__main__":
    main()
