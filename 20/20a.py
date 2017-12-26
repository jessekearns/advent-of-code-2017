class Point:
    def __init__(self, pX, pY, pZ, vX, vY, vZ, aX, aY, aZ):
        self.pX = pX
        self.pY = pY
        self.pZ = pZ
        self.vX = vX
        self.vY = vY
        self.vZ = vZ
        self.aX = aX
        self.aY = aY
        self.aZ = aZ
    
    def increment(self):
        self.vX += self.aX
        self.vY += self.aY
        self.vZ += self.aZ
        self.pX += self.vX
        self.pY += self.vY
        self.pZ += self.vZ

    def mandist(self):
        return (abs(self.pX) + abs(self.pY) + abs(self.pZ))

inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\20\\input20.txt"
with open(inputfile) as f:
    lines = f.readlines()

points = []
for line in lines:
    # strip out the fluff characters
    cleanline = line.replace('<', '').replace('>', '').replace(' ', '').replace('p', '').replace('v', '').replace('a', '').replace('=', '')
    nums = cleanline.split(',')
    newPoint = Point(int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3]), int(nums[4]), int(nums[5]), int(nums[6]), int(nums[7]), int(nums[8]))
    points.append(newPoint)

for i in range(100000):
    for point in points:
        point.increment()

bestIndex = 0
bestDistance = points[0].mandist()
for pIndex in range(len(points)):
    point = points[pIndex]
    dist = point.mandist()
    if dist < bestDistance:
        bestDistance = dist
        bestIndex = pIndex

bestPoint = points[bestIndex]
# Of course it's going to be the one with vector <0, 0, 0>.....
print("Closest point to zero is index {0} with distance {4} and acceleration vector <{1}, {2}, {3}>".format(bestIndex, bestPoint.aX, bestPoint.aY, bestPoint.aZ, bestDistance))