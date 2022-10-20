import controller
import model
import view

model.step_by_step()
if model.step_by_step_var:
    model.init_first()
    while True:
        if model.init_ops():
            break
        model.init_second()
        controller.operation()
        view.print_total()
        model.first = model.total
else:
    try:
        model.one_task()
        model.task_total()
        view.print_total()
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
        view.error_value()
