#!/usr/bin/env python3

import argparse
import subprocess
from pathlib import Path
from datetime import datetime
import platform
from git import Repo

class Brain:
    def __init__(self, version):
        self.version = version

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

    def commit_and_push(self, file_name):
        try:
            repo = Repo('.')
            if repo.is_dirty():
                repo.git.add(A=True)
                commit_message = f"Added todo: {file_name}"
                repo.index.commit(commit_message)
                origin = repo.remote(name='origin')
                origin.push()
                print(f"Committed and pushed changes with message: '{commit_message}'")
            else:
                print("No changes to commit.")
        except Exception as e:
            print(f"Error committing changes: {e}")

    def sync(self):
        try:
            repo = Repo('.')
            print("Pulling latest changes from remote...")
            repo.git.pull()
            print("Pull complete. Now committing and pushing local changes...")
            # Commit and push changes
            self.commit_and_push("todo files")
        except Exception as e:
            print(f"Error during sync: {e}")

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

    def run(self, brain):
        if self.args.version:
            brain.print_version()
        elif self.args.command == 'todo':
            brain.create_or_open_todo()
        elif self.args.command == 'sync':
            brain.sync()

def main():
    brain = Brain(version="1.0.0")
    cli = CommandLineInterface()
    cli.run(brain)

if __name__ == "__main__":
    main()
