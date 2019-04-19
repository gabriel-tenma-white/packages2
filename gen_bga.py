#!/usr/bin/python

W = 26
H = 26
pitch = 1.0
ballDiameter = 0.53
solderMaskDiameter = 0.63
clearance = 0.15

#colList = [0,1,2,6,7,8]
colList = None

ox = -pitch/2.
oy = -pitch/2.

if colList == None:
	colList = range(W)

rowNames = [x for x in 'ABCDEFGHJKLMNPRTUVWY']
rowNamesDoubleDigit = []
for x in rowNames:
	for y in rowNames:
		rowNamesDoubleDigit.append(x+y)
rowNames += rowNamesDoubleDigit


print 'Element["" "" "" "" 155.6000mm 164.5000mm 0.0000 0.0000 0 100 ""]'
print '('

for row in xrange(H):
	y = row*pitch + oy
	rowName = rowNames[row]
	for col in colList:
		x = col*pitch + ox
		name = rowName + str(col + 1)
		print 'Pad[%.04fmm %.04fmm %.04fmm %.04fmm %.04fmm %.04fmm %.04fmm "" "%s" ""]' % (
					x,y,x,y,ballDiameter,clearance*2,solderMaskDiameter,name)
print ')'
