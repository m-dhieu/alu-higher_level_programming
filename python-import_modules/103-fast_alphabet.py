#!/usr/bin/python3
print((lambda s: s.join(map(chr, range(65, 91))))(__import__('').__class__.__base__.__class__.__init__.__globals__['str']()))
