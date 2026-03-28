import os
import shutil

sandbox = os.path.abspath("./data/sandbox")
print(f"Wiping sandbox at {sandbox}...")
if os.path.exists(sandbox):
    for entry in os.listdir(sandbox):
        path = os.path.join(sandbox, entry)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)
print("Done.")
