# Python Git Workflow Practice

## 🎯 Project Goal
Master Git basic workflow (status, add, commit) with Python project

## 🐍 Python Features
- Object-oriented Git workflow simulation
- Commit history management
- Project version control demonstration

## 📁 Project Structure
project/
├── src/
│ └── git_simulator.py # Main Python module
├── examples/
│ └── demo.py # Usage examples
├── tests/ # Unit tests
├── requirements.txt # Dependencies
└── README.md

## 🚀 Quick Start
```bash
python src/git_simulator.py

3. **Коммит изменений:**
   - **Commit message**: `"docs: create comprehensive Python project documentation"`
   - ✅ **Commit directly to the `main` branch**
   - **Нажмите "Commit changes"**

### 🐍 Шаг 2.3: ВТОРОЙ КОММИТ - добавление основного Python модуля

1. **Создайте новую папку:** Нажмите "Add file" → "Create new file"
   - Введите имя: `src/` - GitHub автоматически создаст папку

2. **Теперь создайте файл в папке src:** Введите имя `src/git_simulator.py`

3. **Содержимое файла:**
```python
"""
Git Workflow Simulator - Python Implementation
Simulates basic Git commands: status, add, commit
"""

class GitSimulator:
    def __init__(self, project_name):
        self.project_name = project_name
        self.staged_files = []
        self.commits_history = []
        self.working_directory = {}
        
    def status(self):
        """Simulates git status - shows current state"""
        print(f"\n📊 Project: {self.project_name}")
        print(f"📍 Current branch: main")
        
        # Show staged files
        if self.staged_files:
            print("\n✅ Staged changes (ready to commit):")
            for file in self.staged_files:
                print(f"   A {file}")
        else:
            print("\n❌ No staged changes")
            
        # Show unstaged changes
        if self.working_directory:
            print("\n📝 Unstaged changes:")
            for file, content in self.working_directory.items():
                print(f"   M {file}")
        else:
            print("\n📝 No uncommitted changes")
            
        return {
            'staged': self.staged_files.copy(),
            'unstaged': list(self.working_directory.keys())
        }
    
    def add(self, filename, content=None):
        """Simulates git add - stages files for commit"""
        if content:
            self.working_directory[filename] = content
            
        if filename in self.working_directory:
            self.staged_files.append(filename)
            print(f"✅ Added to staging: {filename}")
        else:
            print(f"❌ File not found in working directory: {filename}")
            
        return self.staged_files
    
    def commit(self, message):
        """Simulates git commit - saves staged changes"""
        if not self.staged_files:
            print("❌ Nothing to commit. Use 'add' first.")
            return None
            
        commit_data = {
            'id': len(self.commits_history) + 1,
            'message': message,
            'files': self.staged_files.copy(),
            'timestamp': self._get_current_time(),
            'hash': self._generate_hash()
        }
        
        self.commits_history.append(commit_data)
        
        # Clear staged files after commit
        committed_files = self.staged_files.copy()
        self.staged_files.clear()
        
        print(f"💾 Committed [{commit_data['hash'][:8]}]: {message}")
        print(f"   📁 Files: {', '.join(committed_files)}")
        
        return commit_data
    
    def log(self):
        """Shows commit history"""
        print(f"\n📜 Commit History for '{self.project_name}':")
        if not self.commits_history:
            print("   No commits yet")
            return
            
        for commit in self.commits_history:
            print(f"   🎯 {commit['id']:2d} [{commit['hash'][:8]}] {commit['message']}")
            print(f"      📅 {commit['timestamp']}")
            print(f"      📁 Files: {', '.join(commit['files'])}")
    
    def _get_current_time(self):
        """Helper method to get current time"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def _generate_hash(self):
        """Helper method to generate fake commit hash"""
        import hashlib
        import random
        random_str = str(random.random()) + str(len(self.commits_history))
        return hashlib.sha1(random_str.encode()).hexdigest()


def demonstrate_git_workflow():
    """Demonstrates the complete Git workflow"""
    print("🚀 Starting Git Workflow Simulation with Python")
    print("=" * 50)
    
    # Initialize Git simulator
    repo = GitSimulator("MyPythonProject")
    
    # Step 1: Check initial status
    print("\n1. Checking initial status:")
    repo.status()
    
    # Step 2: Create some files and add them
    print("\n2. Creating files and adding to staging:")
    repo.add("main.py", "print('Hello World')")
    repo.add("utils.py", "def helper(): pass")
    repo.add("README.md", "# My Project")
    
    # Step 3: Check status after adding
    print("\n3. Status after adding files:")
    repo.status()
    
    # Step 4: Make first commit
    print("\n4. Making first commit:")
    repo.commit("feat: add initial project structure")
    
    # Step 5: Create more changes and commit
    print("\n5. Adding more features:")
    repo.add("requirements.txt", "python>=3.8")
    repo.commit("build: add project dependencies")
    
    # Step 6: Show final history
    print("\n6. Final commit history:")
    repo.log()


if __name__ == "__main__":
    demonstrate_git_workflow()
