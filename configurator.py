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


def generate_settings(name, difficulty):
    base = load_yaml("base_template.yaml")
    game_settings = base["Jak and Daxter The Precursor Legacy"]

    base["name"] = name
    base["description"] = f"{difficulty} difficulty Archipelago seed"
    
    if difficulty == "Easy":
        game_settings["filler_power_cells_replaced_with_traps"] = {5: 50}
        game_settings["trap_effect_duration"] = {10: 50}
        game_settings["trap_weights"] = {
            "Camera Trap": 1,
            "Darkness Trap": 1,
            "Despair Trap": 1,
            "Earthquake Trap": 1,
            "Ecoless Trap": 1,
            "Gravity Trap": 1,
            "Health Trap": 1,
            "Ledge Trap": 1,
            "Mirror Trap": 1,
            "Pacifism Trap": 1,
            "Slippery Trap": 1,
            "Teleport Trap": 1,
            "Trip Trap": 1,
            "Zoomer Trap": 1,
        }
        
    elif difficulty == "Medium":
        game_settings["enable_move_randomizer"] = {"true": 50, "false": 0}
        game_settings["filler_power_cells_replaced_with_traps"] = {10: 50}
        game_settings["trap_effect_duration"] = {20: 50}
        game_settings["trap_weights"] = {
            "Camera Trap": 1,
            "Darkness Trap": 1,
            "Despair Trap": 1,
            "Earthquake Trap": 0,
            "Ecoless Trap": 1,
            "Gravity Trap": 1,
            "Health Trap": 1,
            "Ledge Trap": 1,
            "Mirror Trap": 1,
            "Pacifism Trap": 1,
            "Slippery Trap": 1,
            "Teleport Trap": 1,
            "Trip Trap": 1,
            "Zoomer Trap": 1,
        }
        game_settings["start_inventory"] = {
            "Double Jump": 1  
        }
        
    elif difficulty == "Hard":
        game_settings["enable_move_randomizer"] = {"true": 50, "false": 0}
        game_settings["enable_orbsanity"] = {"per_level": 0, "off": 0, "global": 50}
        game_settings["global_orbsanity_bundle_size:"] = {25: 50}
        game_settings["filler_power_cells_replaced_with_traps"] = {15: 50}
        game_settings["filler_orb_bundles_replaced_with_traps"] = {5: 50}
        game_settings["trap_effect_duration"] = {30: 50}
        game_settings["trap_weights"] = {
            "Camera Trap": 3,
            "Darkness Trap": 1,
            "Despair Trap": 1,
            "Earthquake Trap": 0,
            "Ecoless Trap": 2,
            "Gravity Trap": 3,
            "Health Trap": 1,
            "Ledge Trap": 4,
            "Mirror Trap": 1,
            "Pacifism Trap": 1,
            "Slippery Trap": 1,
            "Teleport Trap": 1,
            "Trip Trap": 2,
            "Zoomer Trap": 1,
        }
        
    elif difficulty == "Extreme":
        game_settings["enable_move_randomizer"] = {"true": 50, "false": 0}
        game_settings["enable_orbsanity"] = {"per_level": 0, "off": 0, "global": 50}
        game_settings["global_orbsanity_bundle_size:"] = {16: 50}
        game_settings["filler_power_cells_replaced_with_traps"] = {35: 50}
        game_settings["filler_orb_bundles_replaced_with_traps"] = {12: 50}
        game_settings["trap_effect_duration"] = {45: 50}
        game_settings["fire_canyon_cell_count"] = {22: 50}
        game_settings["trap_weights"] = {
            "Camera Trap": 8,
            "Darkness Trap": 7,
            "Despair Trap": 6,
            "Earthquake Trap": 0,
            "Ecoless Trap": 2,
            "Gravity Trap": 5,
            "Health Trap": 4,
            "Ledge Trap": 7,
            "Mirror Trap": 6,
            "Pacifism Trap": 3,
            "Slippery Trap": 5,
            "Teleport Trap": 8,
            "Trip Trap": 4,
            "Zoomer Trap": 4,
        }
        
    return base

def generate_yaml():
    player_name = name_entry.get().strip()  
    difficulty = difficulty_var.get()  

    if not player_name:
        messagebox.showerror("Input Error", "Please enter a name.")
        return

    if difficulty not in ["Easy", "Medium", "Hard", "Extreme"]:
        messagebox.showerror("Input Error", "Please select a valid difficulty.")
        return

    # Generate settings based on difficulty
    data = generate_settings(player_name, difficulty)

    # Output path
    output_path = f"{player_name}_{difficulty.lower()}_seed.yaml"
    save_yaml(data, output_path)

    messagebox.showinfo("Success", f"YAML generated:\n{output_path}")

# Main GUI
root = tk.Tk()
root.title("ArchipelaGOAL Seed Generator")

tk.Label(root, text="Enter Your Name:").pack(pady=(10, 0))
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# Dropdown for difficulties
tk.Label(root, text="Select Difficulty:").pack(pady=(10, 0))
difficulty_var = tk.StringVar(root)
difficulty_var.set("Easy")  # Default value

difficulty_dropdown = tk.OptionMenu(root, difficulty_var, "Easy", "Medium", "Hard", "Extreme")
difficulty_dropdown.pack(pady=5)

tk.Button(root, text="Generate Seed", command=generate_yaml).pack(pady=10)

root.mainloop()