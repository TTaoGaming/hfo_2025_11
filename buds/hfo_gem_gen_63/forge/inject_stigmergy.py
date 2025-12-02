import os
import uuid
from datetime import datetime

# Configuration
TARGET_DIR = "buds/hfo_gem_gen_63"
EXCLUDE_DIRS = ["__pycache__", ".venv", ".git", "node_modules", "drafts"]
EXCLUDE_FILES = ["__init__.py", "requirements.txt", ".gitignore", ".env"]

def generate_header(file_path: str, file_type: str) -> str:
    filename = os.path.basename(file_path)
    holon_id = f"hfo-{uuid.uuid4().hex[:8]}"
    
    # Infer type from path
    h_type = "unknown"
    if "brain" in file_path: h_type = "intent"
    elif "src" in file_path: h_type = "implementation"
    elif "test" in file_path: h_type = "test"
    elif "server" in file_path: h_type = "server"
    elif "grimoire" in file_path: h_type = "spell"
    
    if file_type == "md":
        return f"""---
holon:
  id: {holon_id}
  type: {h_type}
  file: {filename}
  status: active
---

"""
    elif file_type == "py":
        return f'''"""
---
holon:
  id: {holon_id}
  type: {h_type}
  file: {filename}
  status: active
---
"""
'''
    return ""

def inject_headers():
    print(f"💉 Injecting Stigmergy Headers into {TARGET_DIR}...")
    count = 0
    
    for root, dirs, files in os.walk(TARGET_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        for file in files:
            if file in EXCLUDE_FILES: continue
            
            file_path = os.path.join(root, file)
            ext = file.split(".")[-1]
            
            if ext not in ["md", "py"]: continue
            
            # Check if header exists
            with open(file_path, 'r') as f:
                content = f.read()
            
            has_header = False
            if ext == "md" and content.startswith("---"): has_header = True
            if ext == "py" and ("holon:" in content): has_header = True
            
            if not has_header:
                print(f"  -> Injecting into {file}")
                header = generate_header(file_path, ext)
                
                with open(file_path, 'w') as f:
                    f.write(header + content)
                count += 1
                
    print(f"✅ Injected {count} headers.")

if __name__ == "__main__":
    inject_headers()
