import controller
import view

step_by_step_var = False
task = []
str_task = ''
first = 0
second = 0
ops = ''
total = 0


def step_by_step():
    global step_by_step_var
    step_by_step_var = controller.step_by_step_choice('Вводить выражение шаг за шагом? (y-да, n-нет): ')


def one_task():
    global task
    global str_task
    str_task = input('Введите выражение одной строкой: ')
    task = controller.task_split(str_task)


def task_total():
    global task
    task = controller.task_calculation(task)


def init_first():
    global first
    first = controller.input_integer('Введите число: ')


def init_second():
    global second
    second = controller.input_integer('Введите число: ')


def init_ops():
    global ops
    ops = controller.input_operation('Введите операцию: ')
    if ops == '=':
        view.print_total()
        return True
