import os
import json

# ---------------------------
# CONFIGURATION
# ---------------------------
USERNAME = os.getlogin()  # automatically detect Windows username  !!!
COM_PORT = "COM3"         # change if needed !!!
# ESP32 project folder
ESP32_PROJECT = r"C:\projects1\ESP_32D_YONA" #chngge if diffrant!!!




# Path to mpremote.exe
MPREMOTE_PATH = f"C:/Users/{USERNAME}/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0/LocalCache/local-packages/Python311/Scripts/mpremote.exe"





# ---------------------------
# CREATE TASKS.JSON FOR ESP32 UPLOAD
# ---------------------------
tasks_json = {
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Upload & Run on ESP32",
            "type": "shell",
            "command": "cmd",
            "args": [
                "/c",
                f"\"{MPREMOTE_PATH}\" connect {COM_PORT} fs cp \"${{file}}\" :main.py && "
                f"\"{MPREMOTE_PATH}\" connect {COM_PORT} reset && "
                f"\"{MPREMOTE_PATH}\" connect {COM_PORT} repl"
            ],
            "presentation": {
                "reveal": "always",
                "panel": "shared",
                "clear": True
            },
            "problemMatcher": []
        }
    ]
}

# Ensure .vscode folder exists
os.makedirs(f"{ESP32_PROJECT}/.vscode", exist_ok=True)

# Save tasks.json in ESP32 project
TASKS_PATH = f"{ESP32_PROJECT}/.vscode/tasks.json"
with open(TASKS_PATH, "w") as f:
    json.dump(tasks_json, f, indent=2)

print(f"tasks.json generated at {TASKS_PATH} for user '{USERNAME}' and COM port '{COM_PORT}'")
print("Now you can run the 'Upload & Run on ESP32' task in VS Code.")
