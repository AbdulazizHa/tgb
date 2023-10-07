from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from db.queries import save_question

questions_router = Router()


class UserData(StatesGroup):
    name = State()
    email = State()
    age = State()
    job = State()
    book = State()
    question = State()

@questions_router.message(Command("ask"))
async def start_questions(message: Message, state: FSMContext):
    await state.set_state(UserData.name)
    kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="exit")]]
    )
    await message.answer(("To ask a question, enter your details. If you want to cancel press 'exit'"))
    await message.answer("Write your name")

@questions_router.message(F.text == 'Cancel')
@questions_router.message(Command("cancel"))
async def cancel_question(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Canceled", reply_markup=ReplyKeyboardRemove())

@questions_router.message(F.text, UserData.name)
async def process_name(message: Message, state: FSMContext):
        await state.update_data(name=message.text)
        await state.set_state(UserData.email)
        await message.answer("Write your email")

@questions_router.message(F.text, UserData.email)
async def process_email(message: Message, state: FSMContext):
    if not "@" in message.text:
        await message.answer("Write incorrect email")
    elif " " in message.text:
        await message.answer("Write incorrect email")
    else:
        await state.update_data(name=message.text)
        await state.set_state(UserData.email)
        await message.answer("Ask the question")

@questions_router.message(F.text, UserData.age)
async def process_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(UserData.job)
    await message.answer("Write your age")

    if message.text <= 1:
        await message.answer('Write age incorrect')
    elif message.text >= 100:
        await message.answer("Write age incorrect")
    else:
        await state.update_data(name=message.text)
        await state.set_state(UserData.age)


@questions_router.message(F.text, UserData.age)
async def process_job(message: Message, state: FSMContext):
    await state.update_data(job=message.text)
    await state.set_state(UserData.job)
    await message.answer("Write your job")
    if not "qwertyuiopasdfghjklzxcvbnm" in message.text:
        await message.answer('Write job incorrect')
    else:
          await state.update_data(name=message.text)
          await state.set_state(UserData.job)

@questions_router.message(F.text, UserData.question)
async def process_email(message: Message, state: FSMContext):
    await state.update_data(question=message.text)

    data = await state.get_data()
    await message.answer(
        "Thaks, its your answers: "
        f"Name: {data['name']}, email: {data['email']}, age: {data['age']}, job: {data['job']}, your request: {data['question']}",
        reply_markup=ReplyKeyboardRemove()
    )
    save_question(data, message.from_user.id)
    await state.clear()

