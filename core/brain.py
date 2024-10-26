import csv
from datetime import datetime, timedelta
from pathlib import Path
import subprocess
import os
import platform
from typing import Optional, Union

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
        """Create or open a TODO file with a template."""
        self.change_to_project_directory()

        folder = Path('05-todos')
        today_date = datetime.now().strftime('%Y-%m-%d')
        file_name = f"{today_date}.md"
        file_path = folder / file_name

        template_path = Path('configs/templates/todo.md')
        folder.mkdir(parents=True, exist_ok=True)

        if file_path.exists():
            print(f"Opening existing markdown file: {file_path}")
        else:
            if template_path.exists():
                with template_path.open('r') as template_file:
                    template_content = template_file.read()

                # Replace placeholders with today's date
                template_content = template_content.replace('{{CreationDate}}', today_date)
                template_content = template_content.replace('{{ModificationDate}}', today_date)

                with file_path.open('w') as file:
                    file.write(template_content)
                print(f"Markdown file created at {file_path}")
            else:
                print(f"Error: Template file not found: {template_path}")
                print("Please ensure the template file exists at 'configs/templates/todo.md' and try again.")
                return

        self.open_file(file_path)

    def create_new_project(self, project_name):
        """Create a new project file with the given name using a template."""
        self.change_to_project_directory()

        folder = Path('01-projects')
        today_date = datetime.now().strftime('%Y-%m-%d')
        file_name = f"{project_name}.md"
        file_path = folder / file_name

        template_path = Path('configs/templates/project.md')
        folder.mkdir(parents=True, exist_ok=True)

        if file_path.exists():
            print(f"Project file already exists: {file_path}")
        else:
            if template_path.exists():
                with template_path.open('r') as template_file:
                    template_content = template_file.read()

                # Replace placeholders with project name and today's date
                template_content = template_content.replace('{{ProjectName}}', project_name)
                template_content = template_content.replace('{{CreationDate}}', today_date)
                template_content = template_content.replace('{{ModificationDate}}', today_date)

                with file_path.open('w') as file:
                    file.write(template_content)
                print(f"New project file created: {file_path}")
            else:
                print(f"Error: Template file not found: {template_path}")
                print("Please ensure the template file exists at 'configs/templates/project.md' and try again.")
                return

        self.open_file(file_path)

    def list_projects(self):
        """List all project files in the '01-projects' directory."""
        self.change_to_project_directory()

        folder = Path('01-projects')
        if not folder.exists():
            print(f"No '01-projects' directory found.")
            return

        project_files = list(folder.glob('*.md'))
        if project_files:
            print("Project files:")
            for file in project_files:
                print(f" - {file.name}")
        else:
            print("No project files found.")

    def open_project(self, project_name):
        """Open a specific project file."""
        self.change_to_project_directory()

        folder = Path('01-projects')
        file_path = folder / f"{project_name}.md"

        if file_path.exists():
            self.open_file(file_path)
        else:
            print(f"Project file not found: {file_path}")

    def has_changes(self):
        """Check if there are any changes to commit."""
        result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
        return bool(result.stdout.strip())

    def commit_and_push(self, commit_message):
        """Commit and push changes to the git repository."""
        self.change_to_project_directory()
        try:
            if not self.has_changes():
                print("No changes to commit.")
                return

            subprocess.run(['git', 'add', '--all'], check=True)
            subprocess.run(['git', 'commit', '-m', commit_message], check=True)
            subprocess.run(['git', 'push'], check=True)

            print(f"Committed and pushed changes with message: '{commit_message}'")
        except subprocess.CalledProcessError as e:
            print(f"Error during git operation: {e}")
        except PermissionError as e:
            print(f"Permission error during git operation: {e}")

    def sync(self):
        """Sync local changes with the remote repository."""
        self.change_to_project_directory()
        try:
            # Discard local changes in script files
            print("Discarding local changes in script files...")
            subprocess.run(['git', 'restore', '--staged', '*.py'], check=True)
            subprocess.run(['git', 'restore', '*.py'], check=True)

            # Pull the latest changes from the remote repository
            print("Pulling latest changes from the remote repository...")
            subprocess.run(['git', 'pull'], check=True)

            # Check for changes after pulling
            result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
            if result.stdout.strip():
                print("Changes detected:")
                print(result.stdout)
            else:
                print("No changes detected after pull.")

            # Stage any local changes
            print("Staging changes...")
            subprocess.run(['git', 'add', '.'], check=True)

            # Commit changes with an automated message
            commit_message = "Synchronized changes with remote"
            print(f"Committing changes with message: '{commit_message}'")
            result = subprocess.run(['git', 'commit', '-m', commit_message], check=True)

            if result.returncode == 0:
                print("Pushing changes to the remote repository...")
                subprocess.run(['git', 'push'], check=True)
                print("Sync completed successfully.")
            else:
                print("No changes to commit.")

        except subprocess.CalledProcessError as e:
            print(f"Error during git operation: {e}")

    def uninstall(self):
        """Remove all files and configurations created by the brain script."""
        paths_to_remove = [
            Path('/usr/local/bin/brain'),
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

    def export_todos_by_period(self, period: str = 'week', num_periods: int = 1):
        """Export TODO items to a CSV file based on the specified period."""
        self.change_to_project_directory()

        folder = Path('05-todos')
        exports_folder = folder / 'exports'
        exports_folder.mkdir(parents=True, exist_ok=True)

        today = datetime.now()
        start_date = today - (timedelta(weeks=num_periods * 7) if period == 'week' else timedelta(days=num_periods * 30))
        end_date = today

        csv_file_path = exports_folder / f"todos_export_{period}_{num_periods}_{start_date.strftime('%Y-%m-%d')}_{end_date.strftime('%Y-%m-%d')}.csv"
        
        with open(csv_file_path, 'w', newline='') as csvfile:
            fieldnames = ['Item', 'Status']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for todo_file in folder.glob('*.md'):
                file_date = datetime.strptime(todo_file.stem, '%Y-%m-%d')
                if start_date <= file_date <= end_date:
                    with todo_file.open('r') as file:
                        for line in file:
                            if line.startswith('- [ ]') or line.startswith('- [x]'):
                                status = 'Completed' if '[x]' in line else 'Pending'
                                item = line[6:].strip()
                                writer.writerow({'Item': item, 'Status': status})
        
        print(f"TODO items exported to {csv_file_path}")

# Usage of the class remains the same, assuming it is invoked via CLI or another interface.
