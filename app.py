import json
import os
import streamlit as st

FILENAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=2)

st.title("Francis' Task Manager 🧠")

if "tasks" not in st.session_state:
    st.session_state.tasks = load_tasks()

tasks = st.session_state.tasks

# Add task
new_task = st.text_input("Add a new task")

if st.button("Add Task"):
    if new_task.strip():
        tasks.append({"task": new_task.strip(), "done": False})
        save_tasks(tasks)
        st.rerun()

st.divider()

# Show tasks
for i, task in enumerate(tasks):
    col1, col2, col3 = st.columns([0.1, 0.7, 0.2])

    done = col1.checkbox("", value=task["done"], key=f"done_{i}")
    if done != task["done"]:
        task["done"] = done
        save_tasks(tasks)

    col2.write(("✅ " if task["done"] else "❌ ") + task["task"])

    if col3.button("Delete", key=f"delete_{i}"):
        tasks.pop(i)
        save_tasks(tasks)
        st.rerun()