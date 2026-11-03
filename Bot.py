import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

active_chats = set()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    active_chats.add(chat_id)

    await update.message.reply_text(
        "🔥 DH4CHU AI BOT PRO\n\n"
        "✅ Bot connected!\n"
        "🟢 Scanner: START requested\n"
        "📊 Market: Waiting for live data connection\n\n"
        "⚠️ Live OTC data source is not connected yet. "
        "No signals will be generated until verified live data is available.\n\n"
        "Use /stop to stop scanning.\n"
        "Use /status to check status."
    )


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    active_chats.discard(chat_id)

    await update.message.reply_text(
        "🛑 Scanner stopped!\n"
        "DH4CHU AI BOT PRO"
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    if chat_id in active_chats:
        state = "🟢 START requested"
    else:
        state = "🔴 STOPPED"

    await update.message.reply_text(
        "🤖 DH4CHU AI BOT PRO\n\n"
        f"Scanner: {state}\n"
        "Live data: Not connected\n"
        "Signals: Disabled until live data is verified."
    )


def main():
    if not TOKEN:
        raise RuntimeError(
            "TELEGRAM_BOT_TOKEN environment variable is missing"
        )

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stop", stop))
    app.add_handler(CommandHandler("status", status))

    print("DH4CHU AI BOT PRO is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
