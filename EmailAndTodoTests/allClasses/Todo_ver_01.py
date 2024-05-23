


class ToDO:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: str):
        if not task or not isinstance(task,str):
            return "task is invalid"
        else:
            self.tasks.append(task)
            return "Task was added"

    def delete_task(self,del_task: str):
        try:
            self.tasks.remove(del_task)
            return "Task was deleted"
        except ValueError:
            return "Task wasn't found or is not valid"

    def get_tasks_list(self):
        tasks_list = ""
        for i, task in enumerate(self.tasks):
            tasks_list += f"{i+1}: {task}\n"
        return tasks_list


