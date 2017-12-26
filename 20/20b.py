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
        self.collided = False
    
    def increment(self):
        if self.collided == False:
            self.vX += self.aX
            self.vY += self.aY
            self.vZ += self.aZ
            self.pX += self.vX
            self.pY += self.vY
            self.pZ += self.vZ

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

for i in range(5000):
    occupied = {}
    for pIndex in range(len(points)):
        point = points[pIndex]
        point.increment()
        if (point.collided == False):
            pos = (point.pX, point.pY, point.pZ)
            if pos in occupied:
                point.collided = True
                points[occupied[pos]].collided = True
            else:
                occupied[pos] = pIndex

survivors = 0
for point in points:
    if point.collided == False:
        survivors += 1

print("Out of {0} total particles, {1} survived without colliding".format(len(points), survivors))