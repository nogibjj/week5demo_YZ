#!/usr/bin/env python3
import click
from collections import Counter
import re

#@click.command()
#@click.argument('file_name', type=click.File('r'))
#@click.argument('lines', default=-1, type=int)
#def head(file_name, lines):

 #   counter = 0

 #   for line in file_name:

 #       print(line.strip())
  #      counter += 1

  #      if counter == lines: 
  #          break


@click.command()
@click.argument("file", type=click.Path(exists=True))
def count_word(file):
    """Counts word frequencies in given file
    or standard input."""
    words = re.findall(r'\w+', open(file=file, encoding="ISO-8859-1").read().lower())
    print(Counter(words).most_common(10))


if __name__ == '__main__':
    count_word()