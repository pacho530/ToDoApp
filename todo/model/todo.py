class Todo:

    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed = True

        return True

    def add_tag(self, tag: str):
        self.tag: str = tag

        if self.tag not in self.tags:
            self.tags.append(tag)

            return

    def __str__(self)-> str:

        return f"{self.code_id} - {self.title}"


class TodoBook:

    def __init__(self):

        self.todos: dict[int, Todo] ={}


    def add_todo(self, title: str, description: str)-> int:

        code_id = len(self.todos) +1
        new_todo = Todo(code_id, title, description)
        self.todos[code_id] = new_todo

        return code_id

    def pending_todos(self):
        pass
