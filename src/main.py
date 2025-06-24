import httpx
from mcp.server.fastmcp import FastMCP
from service.tasks import Tasks
from service.todoList import TodoList

# Create an MCP server
mcp = FastMCP("Demo")
todoListBaseUrl = "http://localhost:3000/api/todolists"
tasksBaseUrl = "http://localhost:3000/api/tasks"
tdlSrv = TodoList(todoListBaseUrl)
taskSrv = Tasks(tasksBaseUrl, tdlSrv)

# Add an addition tool
@mcp.tool()
async def create_list(name: str) -> str:
    """Crear lista ‘Prueba’"""
    list: any = ""
    try:
        list = await tdlSrv.createList(name)
    except ValueError as e:
        return f"Ocurrió algo inesperado: {e}"   
    return list

@mcp.tool()
async def update_list_name(oldName: str, newName: str) -> str:
    """Cambiar, actualizar o update el nombre de la lista ‘OldName’ a o por 'NewName'"""
    list: any = ""
    try:
        list = await tdlSrv.updateListName(oldName, newName)
    except ValueError as e:
        return f"Ocurrió algo inesperado: {e}"   
    return list

@mcp.tool()
async def get_list(name: str) -> str:
    """Obter, ver la lista con nombre ‘Prueba’"""
    tdl: any = ""
    try:
        tdl = await tdlSrv.getList(name)
    except ValueError as e:
        return f"Ocurrió algo inesperado: {e}"
    return f"Su lista es {tdl}!"

@mcp.tool()
async def create_task( name: str, desc: str,list:str) -> str:
    """Crear task o tarea ‘Prueba’ con descripcion 'desc' en la lista 'nombre de lista'"""
    tsk = await taskSrv.createTask(name, desc, list)
    return tsk

@mcp.tool()
async def start_a_task( name: str ,list:str) -> str:
    """Comenzar, empezar o start una tarea / task con nombre 'name' en la lista llamada 'listname'"""
    tsk = await taskSrv.startTask(name, list)
    return tsk
       
@mcp.tool()
async def complete_a_task( name: str ,list:str) -> str:
    """Complete, terminate o finalizar una tarea / task con nombre 'name' en la lista llamada 'listname'"""
    tsk = await taskSrv.completeTask(name, list)
    return tsk

@mcp.tool()
async def delete_a_task(name: str, list: str) -> str:
    """Eliminar, remover o quitar una tarea / task con nombre 'name' de la lista llamada 'listname'"""
    tsk = await taskSrv.deleteTask(name, list)
    return tsk
       
# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="stdio")