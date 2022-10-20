import logger
import model
import view


def step_by_step_choice(enter):
    while True:
        a = input(enter)
        if a in ['y', 'n']:
            if a == "y":
                return True
            else:
                return False
        else:
            print("Введите 'y' если да и 'n' если нет.")


def input_integer(enter):
    while True:
        try:
            a = int(input(enter))
            return a
        except:
            view.error_value()


def input_operation(enter):
    while True:
        a = input(enter)
        if a in ['+', '-', '*', '/', '=']:
            return a
        else:
            view.error_value()


def operation():
    match model.ops:
        case '+':
            model.total = model.first + model.second
        case '-':
            model.total = model.first - model.second
        case '*':
            model.total = model.first * model.second
        case '/':
            while model.second == 0:
                print('На ноль делить нельзя!')
                model.init_second()
            model.total = int(model.first / model.second)

        case _:
            view.error_value()
    logger.logger(f'{model.first} {model.ops} {model.second} = {model.total}')


def task_split(enter):
    a = enter
    buf = ''
    task = []
    for i in a:
        if i.isdigit():
            buf += i
        else:
            task.append(int(buf))
            buf = ''
            task.append(i)
    task.append(int(buf))
    return task


def task_div(task):
    for i in range(len(task)):
        if task[i] == '/':
            task[i - 1] = task[i - 1] / task[i + 1]
            del task[i:i + 2]
            return task


def task_mul(task):
    for i in range(len(task)):
        if task[i] == '*':
            task[i - 1] = task[i - 1] * task[i + 1]
            del task[i:i + 2]
            return task


def task_add(task):
    for i in range(len(task)):
        if task[i] == '+':
            task[i - 1] = task[i - 1] + task[i + 1]
            del task[i:i + 2]
            return task


def task_sub(task):
    for i in range(len(task)):
        if task[i] == '-':
            task[i - 1] = task[i - 1] - task[i + 1]
            del task[i:i + 2]
            return task


def task_calculation(task):
    i = 0
    while ('/' in task) or ('*' in task):
        if i < len(task):
            if task[i] == '/':
                task = task_div(task)
                i -= 1
            if task[i] == '*':
                task = task_mul(task)
                i -= 1
        i += 1
    i = 0
    while ('+' in task) or ('-' in task):
        if i < len(task):
            if task[i] == '+':
                task = task_add(task)
                i -= 1
            if task[i] == '-':
                task = task_sub(task)
                i -= 1
        i += 1
    model.total = model.task[0]
    logger.logger(f'{model.str_task} = {model.total}')
    return task
