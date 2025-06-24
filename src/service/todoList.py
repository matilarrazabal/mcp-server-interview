import httpx

from dto.lists import todoListRequest

class TodoList:
    def __init__(self, tdlUrl: str):
        self.tdlUrl = tdlUrl

    async def getList(self, name: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.tdlUrl}")
            resp = response.json()
            matched_tdl = [tdl for tdl in resp if tdl["name"] == name]
            if not matched_tdl:
                raise ValueError("No se encontro una lista con ese nombre")
            return  matched_tdl[0]
     
    async def createList(self, name: str):  
        try:
            tdl = await self.getList(name)
        except ValueError as e:
            async with httpx.AsyncClient() as client:           
                payload = todoListRequest(name)
                response = await client.post(f"{self.tdlUrl}", json=payload)
                return response.text
        return ValueError(f"Ya existe una lista llamada {name}")

    async def updateListName(self, oldName: str, newName: str):  
        tdl: any = {}
        try:
            tdl = await self.getList(oldName)
        except ValueError as e:
            return ValueError("No se encontro una lista con ese nombre")
        try:
            await self.getList(newName)
        except ValueError as e:
            async with httpx.AsyncClient() as client:           
                payload = todoListRequest(newName)
                tdlId = tdl["id"]
                response = await client.patch(f"{self.tdlUrl}/{tdlId}", json=payload)
                return response.text
        return ValueError(f"Ya existe una lista llamada {newName}")

    
    async def getListId(self, name: str):
        tdl = await self.getList(name)
        id = tdl["id"]
        if not id:
            return 0
        return id 
    