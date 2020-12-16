import json
import os

# List of commands supported by the system
supported_commands = ['build', 'place', 'move', 'turn', 'tilt', 'undo', 'redo', 'store', 'clone', 'give']

# List of the movement direction supported
supported_directions = ['up', 'down', 'left', 'right', 'forward', 'back']

# Required dictionaries for command interpretation
with open(f'{os.path.dirname(os.path.abspath(__file__))}/directions.json') as directions_file:
    directions_dict = json.load(directions_file)

with open(f'{os.path.dirname(os.path.abspath(__file__))}/materials.json') as materials_file:
    materials_dict = json.load(materials_file)