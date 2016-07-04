#!/usr/bin/env xonsh
# fix for Xonsh's `vox` - virtual environment manger tool
# to properly generate virtual environments using virtualenv 
# with python2 or any other python executable
import os

def _venv(args, stdin=None):
    """
    venv <env-name> <python>
    Activate with `vox activate <env-name>`
    """
    name, version = args
    venv_path = os.path.join(os.path.expanduser('~/.virtualenvs'), name)
    print('Creating a virtualenv "{}" with "{}"'.format(name, version))
    virtualenv @(venv_path) -p @(version)

aliases['venv'] = _venv
