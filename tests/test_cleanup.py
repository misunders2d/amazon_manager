import os
import shutil

def test_cleanup():
    sandbox_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    for target in [".venv", ".pytest_cache"]:
        path = os.path.join(sandbox_dir, target)
        if os.path.exists(path):
            print(f"Deleting {path}")
            shutil.rmtree(path)
    assert True
