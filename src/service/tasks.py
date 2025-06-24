import httpx
from dto.tasks import completeATaskRequest, startATaskRequest, taskRequest
from service.todoList import TodoList


class Tasks:
    def __init__(self, tasksUrl: str, tdlSrv: TodoList):
        self.tasksUrl = tasksUrl
        self.tdlSrv = tdlSrv

    async def createTask(self, name: str, desc: str,list:str) -> str:
        listId: int = await self.tdlSrv.getListId(list)
        async with httpx.AsyncClient() as client:
            payload = taskRequest(name, desc)
            response = await client.post(f"{self.tasksUrl}/{listId}", json=payload)
            return response.text

    async def getTasks(self, name: str):
        list = await self.tdlSrv.getList(name)
        return list["tasks"]

    async def getTask(self, name: str, list: str):
        tsks = await self.getTasks(list)
        matched_tsk = [tsk for tsk in tsks if tsk["name"] == name]
        if not matched_tsk:
            return "No se encontro una tarea con ese nombre" 
        return  matched_tsk[0]
        
    async def startTask(self, name: str,list:str):
        payload = startATaskRequest()
        response = await self.updateTask(name,list,payload)
        return response  

    async def completeTask(self, name: str,list:str):
        payload = completeATaskRequest()
        response = await self.updateTask(name,list,payload)
        return response     
        
    async def updateTask(self, name: str,list:str, payload: any):
        list = await self.tdlSrv.getList(list)
        listId = list["id"]
        tasks = list["tasks"]  
        matched_tsk = [tsk for tsk in tasks if tsk["name"] == name]
        tskId = matched_tsk[0]["id"]
        async with httpx.AsyncClient() as client:
            response = await client.patch(f"{self.tasksUrl}/{listId}/{tskId}", json=payload)
            return response.text 
    
    async def deleteTask(self, name: str,list:str):
        list = await self.tdlSrv.getList(list)
        listId = list["id"]
        tasks = list["tasks"]        
        matched_tsk = [tsk for tsk in tasks if tsk["name"] == name]
        tskId = matched_tsk[0]["id"]
        async with httpx.AsyncClient() as client:
            response = await client.delete(f"{self.tasksUrl}/{listId}/{tskId}")
            return response.text 
