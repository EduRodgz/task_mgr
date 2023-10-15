import requests
from app.database import task


BACKEND_URL = "http://127.0.0.1:5000/tasks"
#Mini challenge 1, create script allows interactively update task via ID.


def get_task_by_id(ID):
    single_task = task.select_by_id(ID)
    out = {
        "task": single_task,
        "ok": True
    }
    return out 

def update_task(ID, update_summary, update_description):
    update_task = {
        "ID": ID,
        "update_summary": update_summary,
        "update_description": update_description
    }
    response = requests.put(BACKEND_URL, json=update_task)
    if response.status_code == 204:
        print("Update successfull.")
    else:
        print("Update unsuccessfull, try again.")




if __name__ == "__main__":
    print("To update fill out prompts:")
    ID = input("Enter ID:")
    update_summary = input("Update task summary:")
    update_description = input("Update task description:")
    update_task(ID, update_summary, update_description)