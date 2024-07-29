import argparse
import os
from pathlib import Path
from core.brain import Brain
from core.constants import VERSION

class CommandLineInterface:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="A Python command-line utility named Brain")
        self.setup_arguments()
        self.args = self.parser.parse_args()

    def setup_arguments(self):
        self.parser.add_argument('-v', '--version', action='version', version=f"Brain version: {VERSION}")
        subparsers = self.parser.add_subparsers(dest='command', help='Available commands')

        # Subparser for 'new' command
        new_parser = subparsers.add_parser('new', help='Create new files')
        new_subparsers = new_parser.add_subparsers(dest='new_type', help='Type of file to create')

        # Subparser for 'new todo'
        new_todo_parser = new_subparsers.add_parser('todo', help='Create a new TODO file or open the existing one')

        # Subparser for 'new project'
        new_project_parser = new_subparsers.add_parser('project', help='Create a new project file')
        new_project_parser.add_argument('name', help='Name of the project')

        # Subparser for 'todo' command
        subparsers.add_parser('todo', help='Open the most recent TODO file')

    def run(self, brain):
        args = self.parser.parse_args()
        if args.command == 'new':
            if args.new_type == 'todo':
                brain.create_or_open_todo()
            elif args.new_type == 'project':
                if not args.name:
                    print("Usage: brain new project <project-name>")
                else:
                    brain.create_new_project(args.name)
        elif args.command == 'todo':
            brain.create_or_open_todo()
        else:
            self.parser.print_help()
    def move_to_project_directory(self):
        # Change to the project directory
        project_dir = Path(__file__).parent.parent
        os.chdir(project_dir)
        print(f"Moved to project directory: {project_dir}")
