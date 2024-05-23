from pytest import fixture
from allClasses.Todo_ver_01 import ToDO


@fixture(scope="session")
def todo_list():
    todo = ToDO()
    return todo



