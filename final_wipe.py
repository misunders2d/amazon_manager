import os
import shutil

for root, dirs, files in os.walk(".", topdown=False):
    for d in dirs:
        if d == "__pycache__":
            shutil.rmtree(os.path.join(root, d))
    for f in files:
        if f == "final_wipe.py":
            continue
        rel = os.path.relpath(os.path.join(root, f), ".")
        if rel not in {"pyproject.toml", "CHANGELOG.md", ".gitignore", "app/app_utils/config.py", "app/sub_agents/coordinator_agent.py"}:
            os.unlink(os.path.join(root, f))
print("Final wipe done")
