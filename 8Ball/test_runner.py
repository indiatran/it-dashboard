import runpy
import builtins
from pathlib import Path

script = Path(__file__).parent / "main.py"
# simulate two questions then exit
inputs = iter(["Will I pass?", "yes", "Is this working?", "no"])
builtins.input = lambda prompt='': next(inputs)

runpy.run_path(str(script), run_name='__main__')
