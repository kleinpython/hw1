from aiogram import types, Dispatcher
from config import bot, dp

@dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    questions = "э! что это у тебя??"
    answer = [
        "не понял...",
        "камера",
        "собака",
        "сова",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=questions,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=3,
        explanation="пичальна"
    )

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")