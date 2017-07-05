#!/usr/bin/env python3
import click
import sys

"""Simple cli app for retrieving specific bar of a poem  """

@click.command()
@click.argument('start', required=False, default=0)
@click.argument('end', required=False, default=-1)
@click.option('--input', type=click.File('r'))
@click.option('--output', type=click.File('w'))
@click.option('--split', default='\n\n')
def cli(start, end, input, output, split):
    """Simple, pipeable tool for centering text"""
    source = input.read() if input else sys.stdin.read()
    bars = source.split(split)
    try:
        result = split.join(bars[start: end])
    except IndexError:
        click.echo(f'out of range, total bars: {len(bars)}')
        return
    if output:
        output.write(f'{result}\n')
    else:
        sys.stdout.write(f'{result}\n')

if __name__ == "__main__":
    cli()
