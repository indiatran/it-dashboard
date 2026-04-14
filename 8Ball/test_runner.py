import runpy
import builtins
from pathlib import Path

script = Path(__file__).parent / "main.py"
builtins_input = lambda prompt='': next(inputs)

# simulate: ask a question, press Enter to continue (empty -> treated as yes), ask another question, then 'no' to exit
inputs = iter(["Will I get an A?", "", "Is this a test?", "no"])
builtins.input = lambda prompt='': next(inputs)
builtins.input = lambda prompt='': next(inputs)

runpy.run_path(str(script), run_name='__main__')
