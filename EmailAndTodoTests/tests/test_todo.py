from pytest import mark


@mark.parametrize("task",[
    "Go to gym",
    "Clean the counter",
    "Give julie medicine"
])
def test_if_add_task_adds_correctly(todo_list, task):
    #this test if add_task adds to the list properly with valid string
    todo_task_added = todo_list.add_task(task)
    assert todo_task_added == "Task was added"


@mark.parametrize("task",[
    1235,
    10.5,
    ""
])
def test_if_add_task_returns_error_with_invalid_input(todo_list,task):
    # this test if add_task doesn`t add to the list properly with empty string or different instances
    task_error = todo_list.add_task(task)
    assert task_error == "task is invalid"


def test_if_get_task_list_returns_true_tasks(todo_list):
    # this tests if get_task_list returns a string with all the tasks
    tasks = todo_list.get_tasks_list()
    expected = "1: Go to gym\n2: Clean the counter\n3: Give julie medicine\n"
    assert tasks == expected


@mark.parametrize("task",[
    "Go to gym",
    "Clean the counter",
    "Give julie medicine"
])
def test_if_task_is_deleted_properly(todo_list,task):
    #this tests if a task is deleted from the list properly
    task_deleted = todo_list.delete_task(task)
    expected = "Task was deleted"
    assert task_deleted == expected


@mark.parametrize("task",[
    "Water the plants",
    "",
    1234
])
def test_if_delete_task_returns_error_with_invalid_input(todo_list, task):
    # this tests if a task is not deleted because the test sends a non-existing task or different instances
    task_del_error = todo_list.delete_task(task)
    expected = "Task wasn't found or is not valid"
    assert task_del_error == expected


def test_if_get_task_list_returns_empty(todo_list):
    # this tests if get_task_list returns empty string because there are no tasks
    tasks = todo_list.get_tasks_list()
    expected = ""
    assert tasks == expected









