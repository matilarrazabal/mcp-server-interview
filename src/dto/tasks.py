def taskRequest(name: str, desc: str):
    payload = {
        "name": name,
        "description": desc
    }
    return payload

def startATaskRequest():
    payload = {
        "status": "InProgress"
    }
    return payload

def completeATaskRequest():
    payload = {
        "status": "Completed"
    }
    return payload

def updateTaskNameRequest(name: str):
    payload = {
        "name": name
    }
    return payload

def updateTaskDescriptionRequest(desc: str):
    payload = {
        "description": desc 
    }
    return payload