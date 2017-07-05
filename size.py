#!/usr/bin/env python3
import sys
import os
import shutil
import tempfile

import click


@click.command()
@click.argument('input', required=False, type=click.File('r'))
@click.argument('output', required=False, type=click.File('w'))
@click.option('-tmp', 'tmp', help='pipe to tmp file', is_flag=True)
def cli(input, output, tmp):
    """Simple, pipeable tool for indenting text"""
    rows, columns = shutil.get_terminal_size()
    sys.stdout.write('rows:{}\ncols:{}\n'.format(rows, columns))
    # for line in source:
    #     text = format_.format(line.strip())
    #     if output:
    #         output.write(text)
    #     else:
    #         sys.stdout.write(text)

if __name__ == "__main__":
    cli()
