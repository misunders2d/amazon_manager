import os
import sys
import app
import app.app_utils.config

def test_diag():
    print(f"\nCWD: {os.getcwd()}")
    print(f"sys.path: {sys.path}")
    print(f"app.__file__: {app.__file__}")
    print(f"app.app_utils.config.__file__: {app.app_utils.config.__file__}")
    
    print("\nContent of app/app_utils/config.py (from disk):")
    with open(app.app_utils.config.__file__, 'r') as f:
        print(f.read())
        
    print("\nALLOWED_CONFIG_KEYS in memory:")
    print(app.app_utils.config.ALLOWED_CONFIG_KEYS)
    
    assert False
