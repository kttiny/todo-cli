```python
import json
import os
import sys

FILE = "tasks.json"


def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add(text):
    tasks = load()
    tasks.append({"text": text, "done": False})
    save(tasks)
    print(f"Добавлено: {text}")


def list_tasks():
    tasks = load()
    if not tasks:
        print("Список пуст.")
        return
    for i, t in enumerate(tasks, 1):
        mark = "✓" if t["done"] else "✗"
        print(f"{i}. [{mark}] {t['text']}")


def done(idx):
    tasks = load()
    if 0 < idx <= len(tasks):
        tasks[idx - 1]["done"] = True
        save(tasks)
        print("Отмечено как выполненное.")
    else:
        print("Неверный номер.")


def delete(idx):
    tasks = load()
    if 0 < idx <= len(tasks):
        removed = tasks.pop(idx - 1)
        save(tasks)
        print(f"Удалено: {removed['text']}")
    else:
        print("Неверный номер.")


def main():
    if len(sys.argv) < 2:
        print("Использование: python todo.py [add|list|done|delete] [аргумент]")
        return
    cmd = sys.argv[1]
    if cmd == "add" and len(sys.argv) > 2:
        add(" ".join(sys.argv[2:]))
    elif cmd == "list":
        list_tasks()
    elif cmd == "done" and len(sys.argv) > 2:
        done(int(sys.argv[2]))
    elif cmd == "delete" and len(sys.argv) > 2:
        delete(int(sys.argv[2]))
    else:
        print("Неизвестная команда.")


if __name__ == "__main__":
    main()