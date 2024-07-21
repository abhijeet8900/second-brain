#!/usr/bin/env python3

import os
import sys
import stat
from pathlib import Path
import platform

def make_executable(path):
    """Make a file executable."""
    st = os.stat(path)
    os.chmod(path, st.st_mode | stat.S_IEXEC)

def create_symlink(src, dest):
    """Create a symbolic link."""
    try:
        os.symlink(src, dest)
        print(f"Created symlink {dest} -> {src}")
    except FileExistsError:
        print(f"Symlink {dest} already exists. Skipping.")
    except PermissionError:
        print(f"Permission denied while creating symlink {dest}. Try running as administrator or using sudo.")

def create_batch_file(batch_file, script_file):
    """Create a batch file to run the brain script."""
    with open(batch_file, 'w') as file:
        file.write(f'@echo off\n')
        file.write(f'python {script_file} %*\n')

def setup_unix(brain_init_path):
    # Ensure the script has the shebang line
    with brain_init_path.open('r') as file:
        first_line = file.readline().strip()
    if not first_line.startswith('#!'):
        print("Adding shebang line to the script.")
        shebang = '#!/usr/bin/env python3\n'
        with brain_init_path.open('r+') as file:
            content = file.read()
            file.seek(0, 0)
            file.write(shebang + content)

    # Make the script executable
    make_executable(brain_init_path)

    # Create a symbolic link in /usr/local/bin
    symlink_path = Path('/usr/local/bin/brain')
    create_symlink(brain_init_path, symlink_path)

def setup_windows(brain_init_path):
    # Ensure the script has the shebang line
    with brain_init_path.open('r') as file:
        first_line = file.readline().strip()
    if not first_line.startswith('#!'):
        print("Adding shebang line to the script.")
        shebang = '#!/usr/bin/env python3\n'
        with brain_init_path.open('r+') as file:
            content = file.read()
            file.seek(0, 0)
            file.write(shebang + content)

    # Create the batch file in the project directory
    batch_file_path = brain_init_path.parent / 'brain.bat'
    create_batch_file(batch_file_path, brain_init_path)

    print("Setup completed successfully.")
    print(f"Add {batch_file_path} to your PATH to run 'brain -v' from anywhere.")

def main():
    # Define the brain init path
    project_folder = Path(__file__).parent
    brain_init_path = project_folder / 'init.py'

    # Check if the brain init script exists
    if not brain_init_path.exists():
        print(f"Brain init script {brain_init_path} does not exist.")
        sys.exit(1)

    # Detect the operating system and run the appropriate setup
    if platform.system() == "Windows":
        setup_windows(brain_init_path)
    else:
        setup_unix(brain_init_path)

if __name__ == "__main__":
    main()
