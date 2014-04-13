#!/usr/bin/python
import sys
def valueToIeee1541String(val):
	if val < 0:
		return "neg!"
	if val == 1:
		return "%d Byte" % (val)
	if val < 1024:
		return "%d Bytes" % (val)
	for i in ('', 'KiB', 'MiB', 'GiB', 'TiB', 'EiB', 'PiB', 'YiB', 'ZiB'):
		if (val < 1024.0) or (i == 'ZiB'):
			return "%.3f %s" % (val, i)
		val /= 1024.0
print valueToIeee1541String(float(sys.argv[1]))

