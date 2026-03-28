import os
import shutil

sandbox = os.path.abspath(".")
for item in os.listdir(sandbox):
    if item == "app":
        # Keep the app folder but empty it
        path = os.path.join(sandbox, item)
        for sub in os.listdir(path):
            if sub != "wipe_sandbox_clean.py":
                subpath = os.path.join(path, sub)
                if os.path.isdir(subpath):
                    shutil.rmtree(subpath, ignore_errors=True)
                else:
                    os.unlink(subpath)
    elif item != "wipe_sandbox_clean.py":
        path = os.path.join(sandbox, item)
        if os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)
        else:
            os.unlink(path)
print("Sandbox wiped clean.")
