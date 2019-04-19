#!/usr/bin/python

print '''
Element["" "" "" "" 61.0000mm 13.3000mm 0.0000 0.0000 0 100 ""]
(
'''
for i in xrange(45):
	y = i*1.0
	print '''
	Pad[0.4000mm {0:f}mm 0.5000mm {0:f}mm 0.8000mm 0.4000mm 1.0000mm "" "{1:d}" "square"]
	Pad[0.7000mm {0:f}mm 2.1000mm {0:f}mm 0.4000mm 0.4000mm 0.6000mm "" "{1:d}" "square,edge2"]'''.format(y, i+1)

print '''
)
'''
