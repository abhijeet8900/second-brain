#!/usr/bin/env python3

import argparse
import subprocess
import os
from pathlib import Path
from datetime import datetime
import platform

class Brain:
    def __init__(self, version):
        self.version = version
        self.ensure_git_in_path()

    def ensure_git_in_path(self):
        """Ensure Git is in the PATH environment variable."""
        if platform.system() == "Darwin":  # macOS
            git_path = subprocess.run(['which', 'git'], capture_output=True, text=True).stdout.strip()
            if not git_path:
                raise EnvironmentError("Git not found. Please install Git.")
            os.environ['PATH'] += os.pathsep + os.path.dirname(git_path)

    def print_version(self):
        print(f"Brain version: {self.version}")

    def open_file(self, file_path):
        """Open a file using the default application based on the OS."""
        if platform.system() == "Darwin":  # macOS
            subprocess.run(['open', file_path])
        elif platform.system() == "Linux":
            subprocess.run(['xdg-open', file_path])
        elif platform.system() == "Windows":
            subprocess.run(['start', file_path], shell=True)
        else:
            print("Unsupported operating system for opening files.")

    def create_or_open_todo(self):
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

    def commit_and_push(self, commit_message):
        try:
            # Stage all changes
            subprocess.run(['git', 'add', '--all'], check=True)

            # Commit changes
            subprocess.run(['git', 'commit', '-m', commit_message], check=True)

            # Push changes
            subprocess.run(['git', 'push'], check=True)

            print(f"Committed and pushed changes with message: '{commit_message}'")
        except subprocess.CalledProcessError as e:
            print(f"Error during git operation: {e}")

    def sync(self):
        try:
            # Pull latest changes from remote
            print("Pulling latest changes from remote...")
            subprocess.run(['git', 'pull'], check=True)
            print("Pull complete. Now staging changes...")

            # Stage all changes
            subprocess.run(['git', 'add', '--all'], check=True)
            print("Changes staged. Now committing and pushing...")

            # Commit and push changes
            self.commit_and_push("Synchronized changes with remote")
        except subprocess.CalledProcessError as e:
            print(f"Error during sync: {e}")

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

        print("Uninstallation complete.")

class CommandLineInterface:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="A Python command-line utility named Brain")
        self.setup_arguments()
        self.args = self.parser.parse_args()

    def setup_arguments(self):
        self.parser.add_argument("-v", "--version", action="store_true", help="Show the version number and exit")
        subparsers = self.parser.add_subparsers(dest='command')
        
        # Create subparser for `--todo`
        todo_parser = subparsers.add_parser('todo', help='Manage todos')
        
        # Create subparser for `sync`
        sync_parser = subparsers.add_parser('sync', help='Sync with git repository')

        # Create subparser for `uninstall`
        uninstall_parser = subparsers.add_parser('uninstall', help='Uninstall Brain and revert changes')

    def run(self, brain):
        if self.args.version:
            brain.print_version()
        elif self.args.command == 'todo':
            brain.create_or_open_todo()
        elif self.args.command == 'sync':
            brain.sync()
        elif self.args.command == 'uninstall':
            brain.uninstall()

def main():
    brain = Brain(version="1.0.0")
    cli = CommandLineInterface()
    cli.run(brain)

if __name__ == "__main__":
    main()
