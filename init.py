#!/usr/bin/env python3

from core.cli import CommandLineInterface
from core.brain import Brain
from core.constants import VERSION

def main():
    brain = Brain(version=VERSION)
    cli = CommandLineInterface()
    cli.run(brain)

if __name__ == "__main__":
    main()