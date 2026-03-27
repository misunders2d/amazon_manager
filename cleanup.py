import os
import shutil

sandbox_dir = os.path.abspath(os.path.dirname(__file__))
# Delete the system folders and the symlinked config files
to_delete = [
    ".venv", 
    ".pytest_cache", 
    "__pycache__", 
    "uv.lock", 
    "pyproject.toml",
    "tests/test_dummy.py",
    "tests/test_list_sandbox.py"
]

for target in to_delete:
    path = os.path.join(sandbox_dir, target)
    if os.path.exists(path):
        print(f"Deleting {path}")
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
print("Cleanup complete.")
