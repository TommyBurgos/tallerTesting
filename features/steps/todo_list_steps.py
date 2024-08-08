# Paso 1: Dado que la lista de tareas está vacía
@given('the to-do list contains tasks')
def step_impl(context):
    context.to_do_list = ['Buy groceries', 'Pay bills']

@when('the user lists all tasks')
def step_impl(context):
    context.output = context.to_do_list

@then('the output should contain')
def step_impl(context):
    for row in context.table:
        assert row['Task'] in context.output, f'Task "{row["Task"]}" not found in output'

@when('the user marks task "Buy groceries" as completed')
def step_impl(context):
    context.to_do_list[context.to_do_list.index('Buy groceries')] = 'Buy groceries (completed)'

@then('the to-do list should show task "Buy groceries" as completed')
def step_impl(context):
    assert 'Buy groceries (completed)' in context.to_do_list, 'Task "Buy groceries" not marked as completed'

@when('the user clears the to-do list')
def step_impl(context):
    context.to_do_list.clear()


@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.to_do_list) == 0, 'To-do list is not empty'

@when('the user deletes the task "Buy groceries"')
def step_impl(context):
    context.to_do_list.remove('Buy groceries')

@then('the to-do list should not contain "Buy groceries"')
def step_impl(context):
    assert 'Buy groceries' not in context.to_do_list, 'Task "Buy groceries" was not deleted'
