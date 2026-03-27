import os
import shutil

sandbox_dir = os.path.abspath(os.path.dirname(__file__))
for target in [".venv", ".pytest_cache", "__pycache__"]:
    path = os.path.join(sandbox_dir, target)
    if os.path.exists(path):
        print(f"Deleting {path}")
        shutil.rmtree(path)
print("Cleanup complete.")
