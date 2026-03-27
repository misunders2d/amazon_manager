import os

def test_list_sandbox():
    sandbox_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    print(f"\nListing sandbox contents: {sandbox_dir}")
    for root, dirs, files in os.walk(sandbox_dir):
        if ".venv" in root:
            continue
        rel = os.path.relpath(root, sandbox_dir)
        print(f"[{rel}] {len(files)} files, {len(dirs)} dirs")
    assert True
