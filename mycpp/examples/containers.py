#!/usr/bin/python
"""
container_types.py
"""
from __future__ import print_function

import os
from runtime import log

from typing import List, Tuple


def IntDemo():
  # type: () -> None
  intlist = []  # type: List[int]
               # NOTE: this annotation is required, or MyPy has a partial type.
               # I thoguht it would be able to infer it from expressions below.

  intlist.append(1)
  intlist.append(2)
  intlist.append(3)
  log("len(intlist) = %d", len(intlist))
  for i in intlist:
    log("i = %d", i)

  strlist = []  # type: List[str]

  strlist.append('a')
  strlist.append('b')
  log("len(strlist) = %d", len(strlist))
  for s in strlist:
    log("s = %s", s)

  #strlist.pop()
  #strlist.pop()
  x = strlist.pop()
  log("len(strlist) = %d", len(strlist))
  # seg fault
  #log("x = %s", x)


def TupleDemo():
  # type: () -> None

  t2 = (3, 'hello')  # type: Tuple[int, str]

  # Destructuring
  myint, mystr = t2
  log('myint = %d', myint)
  log('mystr = %s', mystr)

  # Does this ever happen?  Or do we always use destructring?
  #log('t2[0] = %d', t2[0])
  #log('t2[1] = %s', t2[1])


def run_tests():
  # type: () -> None

  IntDemo()
  log('')
  TupleDemo()


def run_benchmarks():
  # type: () -> None
  n = 1000000
  i = 0
  intlist = []  # type: List[int]
  strlist = []  # type: List[str]
  while i < n:
    intlist.append(i)
    strlist.append("foo")
    i += 1

  log('Appended %d items to 2 lists', n)


if __name__ == '__main__':
  if os.getenv('BENCHMARK'):
    log('Benchmarking...')
    run_benchmarks()
  else:
    run_tests()
