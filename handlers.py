from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import flags
from aiogram.fsm.context import FSMContext
import asyncio

import utils
from states import Schedule
from datetime import datetime
import db

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! я что-то делаю. как со мной работать\n"
                     "1.Добавление задач\n"
                     "/task\n"
                     "Ваш текст\n"
                     "2.Просмотр расписания\n"
                     "/schedule\n"
                     "/today")


@router.message(F.text == "/task")
async def init_task_adding(msg: Message, state: FSMContext):
    await state.set_state(Schedule.init_adding_task)
    await msg.answer("Напишите вашу задачу")


@router.message(Schedule.init_adding_task)
async def add_task(msg: Message, state: FSMContext):
    object_to_write = {"user_id": msg.from_user.id,
                       "data": {
                           "text": msg.text,
                           "created": f"{datetime.now()}",
                           "deadline": None}
                       }

    await db.write(object_to_write)
    await msg.answer("Задача успешно записана!")
    await state.clear()



@router.message(F.text == "/schedule")
async def init_task_adding(msg: Message, state: FSMContext):
    await state.set_state(Schedule.init_showing_task)
    await msg.answer("Ваше расписание")


@router.message(Schedule.init_showing_task, F.text == "/today")
async def show_task_today(msg: Message, state: FSMContext):
    text = await db.read()
    print(text)
    await msg.answer(f"{text}")
    await state.clear()
