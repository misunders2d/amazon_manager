import os
import shutil

def clean():
    sandbox_dir = "/code/data/sandbox"
    print(f"Cleaning sandbox: {sandbox_dir}")
    for filename in os.listdir(sandbox_dir):
        if filename == "cleaner.py":
            continue
        file_path = os.path.join(sandbox_dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            print(f"Deleted {filename}")
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

if __name__ == "__main__":
    clean()

clean() # Run on import
