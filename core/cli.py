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
        todo_parser = subparsers.add_parser('todo', help='Manage TODO items')
        todo_subparsers = todo_parser.add_subparsers(dest='todo_action', help='TODO actions')

        # Subparser for 'todo open'
        todo_open_parser = todo_subparsers.add_parser('open', help='Open the most recent TODO file')

        # Subparser for 'todo export' command
        todo_export_parser = todo_subparsers.add_parser('export', help='Export TODO items to a CSV file')
        export_subparsers = todo_export_parser.add_subparsers(dest='export_type', help='Export type')

        export_month_parser = export_subparsers.add_parser('month', help='Export TODO items from the last x months')
        export_month_parser.add_argument('months', type=int, nargs='?', default=1, help='Number of months to export (default: 1 month)')

        export_week_parser = export_subparsers.add_parser('week', help='Export TODO items from the last x weeks')
        export_week_parser.add_argument('weeks', type=int, nargs='?', default=1, help='Number of weeks to export (default: 1 week)')

        # Subparser for 'sync' command
        subparsers.add_parser('sync', help='Sync local changes with the remote repository')

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
            if args.todo_action == 'open':
                brain.create_or_open_todo()
            elif args.todo_action == 'export':
                if args.export_type == 'month':
                    # Use default value of 1 month if not provided
                    brain.export_todos_by_period('month', args.months)
                elif args.export_type == 'week':
                    # Use default value of 1 week if not provided
                    brain.export_todos_by_period('week', args.weeks)
        elif args.command == 'sync':
            brain.sync()
        else:
            self.parser.print_help()

    def move_to_project_directory(self):
        # Change to the project directory
        project_dir = Path(__file__).parent.parent
        os.chdir(project_dir)
        print(f"Moved to project directory: {project_dir}")
