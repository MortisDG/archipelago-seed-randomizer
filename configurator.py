import tkinter as tk
from tkinter import messagebox
import yaml
import os

# Load/Save 
def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def save_yaml(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, sort_keys=False)

# Easy settings
def apply_easy_settings(data):
    easy_settings = data["Jak and Daxter The Precursor Legacy"]

    easy_settings["filler_power_cells_replaced_with_traps"] = {
        0: 0,
        "random": 0,
        "random-low": 0,
        "random-high": 0,
        5: 100  
    }

    easy_settings["trap_effect_duration"] = {
        10: 100,  
        "random": 0,
        "random-low": 0,
        "random-high": 0
    }

    easy_settings["trap_weights"] = {
        "Camera Trap": 0,
        "Darkness Trap": 1,
        "Despair Trap": 0,
        "Earthquake Trap": 1,
        "Ecoless Trap": 1,
        "Gravity Trap": 0,
        "Health Trap": 0,
        "Ledge Trap": 0,
        "Mirror Trap": 0,
        "Pacifism Trap": 1,
        "Slippery Trap": 1,
        "Teleport Trap": 0,
        "Trip Trap": 1,
        "Zoomer Trap": 0
    }


# Generate YAML
def generate_yaml():
    player_name = name_entry.get().strip()

    if not player_name:
        messagebox.showerror("Input Error", "Please enter a name.")
        return

    # Load template
    template_path = "base_template.yaml"
    if not os.path.exists(template_path):
        messagebox.showerror("File Error", f"Template file not found:\n{template_path}")
        return

    data = load_yaml(template_path)

    # Apply settings
    data["name"] = player_name
    data["description"] = "Easy Difficulty"
    apply_easy_settings(data)

    # Output path
    output_path = f"{player_name}_easy_seed.yaml"
    save_yaml(data, output_path)

    messagebox.showinfo("Success", f"YAML generated:\n{output_path}")


# Main GUI
root = tk.Tk()
root.title("Archipelago Seed Generator - Easy Mode")

tk.Label(root, text="Enter Your Name:").pack(pady=(10, 0))
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

tk.Button(root, text="Generate Easy Seed", command=generate_yaml).pack(pady=10)

root.mainloop()