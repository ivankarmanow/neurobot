from aiogram.fsm.state import StatesGroup, State

class Schedule(StatesGroup):
    init_adding_task = State()
    init_showing_task = State()
