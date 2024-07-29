import argparse
import os
from pathlib import Path
from core.brain import Brain

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
        else:
            self.move_to_project_directory()

    def move_to_project_directory(self):
        # Change to the project directory
        project_dir = Path(__file__).parent.parent
        os.chdir(project_dir)
        print(f"Moved to project directory: {project_dir}")
