# Second Brain

Second Brain is a Python command-line utility designed to assist with managing personal knowledge, projects, and TODO lists. It integrates with Git for version control and provides an easy-to-use interface for creating and managing various documents.

## Features

- TODO Management: Create, open, and export TODO files.

- Project Management: Create and manage project files.

- Git Integration: Sync changes with a remote Git repository, commit, and push changes.

- Cross-Platform Support: Compatible with Unix-based systems (Linux, macOS) and Windows.

## Requirements

- Python 3.6 or higher
- Git

## Installation

1. Clone the Repository:

    `
    git clone https://github.com/abhijeet8900/second-brain
    cd second-brain
    `

2. Setup the Environment:

    Run the setup.py script to configure your environment:

    `python setup.py`

    This script will:
        Add a shebang line to the main script (init.py).
        Make the script executable on Unix systems.
        Create a symbolic link or a batch file to run the script easily.

## Command-Line Interface (CLI)

The CLI provides various commands to interact with the Brain application

`brain -v` : Print out current version.

`brain new todo` : Creates new markdown todo file with todays date.

`brain new project <project-name>` : Creates new markdown project document file.

`brain todo open` : Opens recent todo file.

`brain todo export week <x>` : Exports todo's for x number of week from today

`brain todo export month <x>` : Exports todo's for x number of months from today

`brain sync` : Sync up with git repo

`brain help` : List out available commands
