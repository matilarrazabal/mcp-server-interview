# mcp-server-interview
Model Context Protocol server for croonchloop interview

## Usage
The following steps were how the server was tested.

First a client like claude desktop should be installed.
Then open a terminal in the mcp-server-interview folder and execute:

Add MCP to your project dependencies:
>uv add "mcp[cli]"

Then install the mcp server in claude:
>uv run mcp install src/main.py

## Structure 

```text
MCP-SERVER-INTERVIEW/
├── requirements.txt
├── .gitignore
├── config/
│   ├── conf.yml
|   ├── loader.py
│   └── __init__.py
├── src/
|   ├── dto/
|   │   ├── lists.py
|   │   └── tasks.py
|   ├── service/
|   |   ├── __init__.py
|   │   ├── todoList.py
|   │   └── tasks.py
│   └── main.py
├── README.md
└── requirements.txt
```

## Interacting with the server.
Examples of propts given to claude desktop to test and interact with the server.
The prompts were given in spanish like the example of the challenge instructions.

Create a new todo list.
>Crea una lista llamada 'Nombre de lista"

Create a task for a specific list.
>Crea la tarea llamada 'tarea1' con descripcion 'desc' en la lista llamda 'Nombre de lista'

Start a task (change the task's status to 'InProgress')
>Comenzar la tarea 'tarea1' de la lista 'Nombre de lista'

Complete a task (change the task's status to 'Completed')
>Terminar la tarea 'tarea1' de la lista 'Nombre de lista'

Delete a task 
>Eliminar la tarea 'tarea1' de la lista 'Nombre de lista'

## Next steps
*Tasks:* Right now it's not avilable to change name and description for a giving task. 

## Areas for improvement
*Test:* Even though the server was manually tested, testing the service layer will ensure correctness in futures changes.

*App Configuration:* After having dependency-related errors, the app configuration module was left out, and the todo list service url was hardcoded in the main script. However, keeping all configuration values in one place make te deployment and usage easier.

*Project structure:* Structuring a project in layers helps to assign responsabilities and group similar functions and classes. For this kind of project, it's not common to find a architecture design to follow.
