from datetime import datetime

HISTORY_FILE = "history.txt"

def save_record(expression, result):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record = f"{timestamp} | {expression} = {result}\n"
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(record)

def load_history():

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

def show_history():
    records = load_history()
    if not records:
        print("История пока пуста!")
    else:
        print("\n--- История вычислений ---")
        for line in records:
            print(line, end="")
        print()

def clear_history():
 
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        f.write("")
    print("История очищена.")