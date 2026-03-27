import os

def test_readme_ends_with_dot():
    # Find the README.md file relative to the project root
    readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
    if not os.path.exists(readme_path):
         # Handle case where test is run inside sandbox vs live
         readme_path = os.path.join(os.path.dirname(__file__), "..", "..", "README.md")
    
    with open(readme_path, "r") as f:
        content = f.read().strip()
    assert content.endswith(".")
