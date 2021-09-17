# Features
user can add a new task to kanban

user can see todo list in chronological order

user can move a todo item to WIP

user can see WIP list in chronological order

user can move a WIP item to Done

user can see Done list in chronological order

# For cli
## create a item to todo list
$ kanban new “I want to drink water”

## move item with id 1 to wip list
$ kanban move 1 to wip

## move item with id 1 to done list
$ kanban move 1 to done

## display all items in todo list
$ kanban todo

## display all items in wip list
$ kanban wip

## display all items in done list
$ kanban done