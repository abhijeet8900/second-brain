from pathlib import Path
import subprocess
import os
import platform
from datetime import datetime

class Brain:
    def __init__(self, version):
        self.version = version
        self.project_dir = self.find_project_directory()
        self.ensure_git_in_path()

    def ensure_git_in_path(self):
        """Ensure Git is in the PATH environment variable."""
        if platform.system() == "Darwin":  # macOS
            git_path = subprocess.run(['which', 'git'], capture_output=True, text=True).stdout.strip()
            if not git_path:
                raise EnvironmentError("Git not found. Please install Git.")
            os.environ['PATH'] += os.pathsep + os.path.dirname(git_path)

    def find_project_directory(self):
        """Find and return the root directory of the project."""
        current_file = Path(__file__).resolve()
        return current_file.parent.parent

    def change_to_project_directory(self):
        """Change the current working directory to the project root directory."""
        os.chdir(self.project_dir)
        print(f"Changed directory to project root: {self.project_dir}")

    def print_version(self):
        print(f"Brain version: {self.version}")

    def open_file(self, file_path):
        """Open a file using the default application based on the OS."""
        try:
            if platform.system() == "Darwin":  # macOS
                subprocess.run(['open', file_path])
            elif platform.system() == "Linux":
                subprocess.run(['xdg-open', file_path])
            elif platform.system() == "Windows":
                subprocess.run(['start', file_path], shell=True)
            else:
                print("Unsupported operating system for opening files.")
        except Exception as e:
            print(f"Error opening file: {e}")

    def create_or_open_todo(self):
        # Change to the project directory
        self.change_to_project_directory()

        # Define the folder and file name
        folder = Path('05-todos')
        today_date = datetime.now().strftime('%Y-%m-%d')
        file_name = f"{today_date}.md"
        file_path = folder / file_name

        # Define the template file path
        template_path = Path('configs/todo-template.md')

        # Create the folder if it does not exist
        folder.mkdir(parents=True, exist_ok=True)

        # Create or open the markdown file with the template
        if file_path.exists():
            print(f"Opening existing markdown file: {file_path}")
        else:
            if template_path.exists():
                with template_path.open('r') as template_file:
                    template_content = template_file.read()
                
                # Replace placeholders with today's date
                template_content = template_content.replace('created: YYYY-MM-DD', f'created: {today_date}')
                template_content = template_content.replace('modified: YYYY-MM-DD', f'modified: {today_date}')
            else:
                print(f"Template file not found: {template_path}")
                template_content = f"""---
created: {today_date}
modified: {today_date}
---
"""

            with file_path.open('w') as file:
                file.write(template_content)
            print(f"Markdown file created at {file_path}")

        # Open the file
        self.open_file(file_path)

    def has_changes(self):
        """Check if there are any changes to commit."""
        result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
        return bool(result.stdout.strip())

    def commit_and_push(self, commit_message):
        self.change_to_project_directory()  # Ensure we're in the project directory
        try:
            # Check for changes before staging
            if not self.has_changes():
                print("No changes to commit.")
                return

            # Stage all changes
            subprocess.run(['git', 'add', '--all'], check=True)

            # Commit changes
            subprocess.run(['git', 'commit', '-m', commit_message], check=True)

            # Push changes
            subprocess.run(['git', 'push'], check=True)

            print(f"Committed and pushed changes with message: '{commit_message}'")
        except subprocess.CalledProcessError as e:
            print(f"Error during git operation: {e}")
        except PermissionError as e:
            print(f"Permission error during git operation: {e}")

    def sync(self):
        self.change_to_project_directory()  # Ensure we're in the project directory
        try:
            # Discard local changes in Python script files
            print("Discarding local changes in script files...")
            subprocess.run(['git', 'restore', '--staged', '*.py'], check=True)
            subprocess.run(['git', 'restore', '*.py'], check=True)

            # Pull the latest changes from the remote repository
            print("Pulling latest changes from the remote repository...")
            subprocess.run(['git', 'pull'], check=True)

            # Log changes in non-script files after pull
            print("Logging changes in non-script files...")
            result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
            changes = result.stdout.strip().split('\n')
            for change in changes:
                if change and not change.startswith('M *.py'):
                    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {change}")

            # Stage any local changes
            print("Staging changes...")
            subprocess.run(['git', 'add', '.'], check=True)

            # Commit changes with an automated message
            commit_message = "Synchronized changes with remote"
            print(f"Committing changes with message: '{commit_message}'")
            subprocess.run(['git', 'commit', '-m', commit_message], check=True)

            # Push changes to the remote repository
            print("Pushing changes to the remote repository...")
            subprocess.run(['git', 'push'], check=True)

            print("Sync completed successfully.")

        except subprocess.CalledProcessError as e:
            print(f"Error during git operation: {e}")

    def uninstall(self):
        """Remove all files and configurations created by the brain script."""
        # Define paths to be removed
        paths_to_remove = [
            Path('/usr/local/bin/brain'),  # Example symlink path
            Path('05-todos'),
            Path('configs/todo-template.md')
        ]

        for path in paths_to_remove:
            try:
                if path.is_symlink() or path.is_file():
                    path.unlink()
                    print(f"Removed file: {path}")
                elif path.is_dir():
                    for sub_path in path.rglob('*'):
                        if sub_path.is_file():
                            sub_path.unlink()
                            print(f"Removed file: {sub_path}")
                    path.rmdir()
                    print(f"Removed directory: {path}")
            except Exception as e:
                print(f"Error removing {path}: {e}")
            except PermissionError as e:
                print(f"Permission error removing {path}: {e}")

        print("Uninstallation complete.")
