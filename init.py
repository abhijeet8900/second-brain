#!/usr/bin/env python3

from core.brain import Brain
from core.cli import CommandLineInterface
from core.constants import VERSION
import argparse
import sys


def main():
    brain = Brain(version=VERSION)
    cli = CommandLineInterface()
    cli.run(brain)

if __name__ == "__main__":
    main()
