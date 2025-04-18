import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import yaml
import os
import random

# Load/Save 
def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def save_yaml(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, sort_keys=False)

def generate_random_trap_weights(min_weight=3, max_weight=10):
    trap_names = [
        "Camera Trap",
        "Darkness Trap",
        "Despair Trap",
        "Earthquake Trap",
        "Ecoless Trap",
        "Gravity Trap",
        "Health Trap",
        "Ledge Trap",
        "Mirror Trap",
        "Pacifism Trap",
        "Slippery Trap",
        "Teleport Trap",
        "Trip Trap",
        "Zoomer Trap",
    ]
    
    return {
        trap: random.randint(min_weight, max_weight)
        for trap in trap_names
    }

def generate_settings(name, difficulty):
    base = load_yaml("base_template.yaml")
    game_settings = base["Jak and Daxter The Precursor Legacy"]

    base["name"] = name
    base["description"] = f"{difficulty} difficulty Archipelago seed"
    
    if difficulty == "Easy":
        random_filler_size = random.randint(1, 5)
        random_trap_duration = random.randint(5, 10)
        
        game_settings["filler_power_cells_replaced_with_traps"] = {random_filler_size: 50}
        game_settings["trap_effect_duration"] = {random_trap_duration: 50}
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
        random_filler_size = random.randint(5, 10)
        random_trap_duration = random.randint(5, 15)
        
        game_settings["enable_move_randomizer"] = {"true": 50, "false": 0}
        game_settings["filler_power_cells_replaced_with_traps"] = {random_filler_size: 50}
        game_settings["trap_effect_duration"] = {random_trap_duration: 50}
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
        random_filler_size = random.randint(5, 15)
        random_orb_filler_size = random.randint(1, 5)
        random_trap_duration = random.randint(10, 30)
        valid_bundle_sizes = [1, 2, 4, 5, 8, 10, 16, 20, 25, 40, 50]
        random_orbsanity_size = random.choice(valid_bundle_sizes)
        
        game_settings["enable_move_randomizer"] = {"true": 50, "false": 0}
        game_settings["enable_orbsanity"] = {"per_level": 0, "off": 0, "global": 50}
        game_settings["global_orbsanity_bundle_size"] = {random_orbsanity_size: 50}
        game_settings["filler_power_cells_replaced_with_traps"] = {random_filler_size: 50}
        game_settings["filler_orb_bundles_replaced_with_traps"] = {random_orb_filler_size: 50}
        game_settings["trap_effect_duration"] = {random_trap_duration: 50}
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
        random_filler_size = random.randint(15, 35)
        random_orb_filler_size = random.randint(5, 10)
        random_trap_duration = random.randint(25, 60)
        valid_bundle_sizes = [16, 20, 25, 40, 50, 80, 100]
        random_orbsanity_size = random.choice(valid_bundle_sizes)
        random_canyon_cell_count = random.randint(20, 25)        
        
        game_settings["enable_move_randomizer"] = {"true": 50, "false": 0}
        game_settings["enable_orbsanity"] = {"per_level": 0, "off": 0, "global": 50}
        game_settings["global_orbsanity_bundle_size"] = {random_orbsanity_size: 50}
        game_settings["filler_power_cells_replaced_with_traps"] = {random_filler_size: 50}
        game_settings["filler_orb_bundles_replaced_with_traps"] = {random_orb_filler_size: 50}
        game_settings["trap_effect_duration"] = {random_trap_duration: 50}
        game_settings["fire_canyon_cell_count"] = {random_canyon_cell_count: 50}
        game_settings["trap_weights"] = generate_random_trap_weights()
        
    elif difficulty == "No Logic":
        random_filler_size = random.randint(15, 50)
        random_orb_filler_size = random.randint(5, 20)
        random_trap_duration = random.randint(25, 60)
        valid_bundle_sizes = [16, 20, 25, 40, 50, 80, 100, 125, 200, 250]
        random_orbsanity_size = random.choice(valid_bundle_sizes)
        random_canyon_cell_count = random.randint(20, 25)
        random_mountainpass_cell_count = random.randint(45, 50)
        random_lava_tube_cell_count = random.randint(72, 80)
        random_citizen_orb_trade_amount = random.randint(90, 130)
        random_oracle_orb_trade_amount = random.randint(120, 150)
        random_punch_for_klaww = random.choices(
                                                ["true", "false"],           
                                                weights=[0, 50],            
                                                k=1                          
                                                )[0]  
        
        game_settings["enable_move_randomizer"] = {"true": 50, "false": 0}
        game_settings["enable_orbsanity"] = {"per_level": 0, "off": 0, "global": 50}
        game_settings["global_orbsanity_bundle_size"] = {random_orbsanity_size: 50}
        game_settings["filler_power_cells_replaced_with_traps"] = {random_filler_size: 50}
        game_settings["filler_orb_bundles_replaced_with_traps"] = {random_orb_filler_size: 50}
        game_settings["trap_effect_duration"] = {random_trap_duration: 50}
        game_settings["fire_canyon_cell_count"] = {random_canyon_cell_count: 50}
        game_settings["mountain_pass_cell_count"] = {random_mountainpass_cell_count: 50}
        game_settings["lava_tube_cell_count"] = {random_lava_tube_cell_count: 50}
        game_settings["citizen_orb_trade_amount"] = {random_citizen_orb_trade_amount: 50}
        game_settings["oracle_orb_trade_amount"] = {random_oracle_orb_trade_amount: 50}
        game_settings["require_punch_for_klaww"] = {random_punch_for_klaww: 50}
        game_settings["trap_weights"] = generate_random_trap_weights()
        game_settings["accessibility"] = {"full": 0, "minimal": 50}
        game_settings["progression_balancing"] = {
            "random": 0,
            "random-low": 0,
            "random-high": 0,
            "disabled": 50, 
            "normal": 0,
            "extreme": 0  
        }
        
    return base

def generate_yaml():
    player_name = name_entry.get().strip()  
    difficulty = difficulty_var.get()  

    if not player_name:
        messagebox.showerror("Input Error", "Please enter a name.")
        return

    if difficulty not in ["Easy", "Medium", "Hard", "Extreme", "No Logic"]:
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
root.geometry("350x250") 
root.config(bg="#2E3B4E")  

title_label = tk.Label(root, text="Enter Your Username:", bg="#2E3B4E", fg="#FFFFFF")
title_label.pack(pady=(20, 5))

name_entry = tk.Entry(root, width=30, bg="#F0F0F0", relief="solid", bd=2)
name_entry.pack(pady=5)

difficulty_label = tk.Label(root, text="Select Difficulty:", bg="#2E3B4E", fg="#FFFFFF")
difficulty_label.pack(pady=(15, 5))

difficulty_var = tk.StringVar(root)
difficulty_var.set("Easy")  
difficulty_dropdown = ttk.OptionMenu(root, difficulty_var, "Easy", "Medium", "Hard", "Extreme", "No Logic")
difficulty_dropdown.config(width=20)
difficulty_dropdown.pack(pady=5)

generate_button = tk.Button(root, text="Generate Seed", command=generate_yaml, bg="#4CAF50", fg="white", relief="solid", bd=2, padx=20, pady=10)
generate_button.pack(pady=(20, 10))

root.mainloop()