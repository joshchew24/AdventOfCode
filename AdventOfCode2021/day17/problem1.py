test_target = (range(20,30 + 1),range(-10,-5 + 1))
input_target = (range(287,309 + 1),range(-76,-48 + 1))

curr_target = test_target

# probe initial = 0,0
# find launch trajectory that allows the probe to end up in the target area
# assume top right corner is best (may not be due to whole numbers)
class probe:
    def __init__(self, vel_x, vel_y):
        self.x = 0
        self.y = 0
        self.x_delta = vel_x
        self.y_delta = vel_y
        self.init_vel = (vel_x, vel_y)
    
    def step(self):
        self.x += self.x_delta
        self.y += self.y_delta
        if self.x_delta != 0:
            self.x_delta -= 1 if self.x_delta > 0 else -1
        self.y_delta -= 1

    def __str__(self):
        return "pos: " + str(self.x) + " " + str(self.y) + " vel: " + " " + str(self.x_delta) + " " + str(self.y_delta)

    def checkHit(self):
        return self.x in curr_target[0] and self.y in curr_target[1]

    # returns direction to reach target area
    def checkXDirection(self):
        if self.x < curr_target[0][0]:
            return 1
        if self.x > curr_target[0][-1]:
            return -1
        return 0
    
    def checkPastX(self):
        return self.x > curr_target[0][-1]
    
    def checkPastY(self):
        return self.y < curr_target[1][-1]


target_point = (curr_target[0][1], curr_target[1][1])
hit = False
x_vel = 0
y_vel = 0
max_height = 0
dec = False
max_probe = None

for x in range(500):
    for y in range(500):
        test_probe = probe(x, y)
        curr_max_height = 0
        curr_hit = False
        while(not test_probe.checkPastY()):
            if test_probe.x_delta == 0 and test_probe.y_delta == 0:
                if test_probe.y > max_height:
                    curr_max_height = test_probe.y
            if test_probe.checkHit():
                curr_hit = True
                # max_height = curr_max_height
                # max_probe = test_probe
            test_probe.step()
        if curr_hit and curr_max_height > max_height:
            max_height = curr_max_height
            max_probe = test_probe

        
print(test_probe)
print(max_height)
print(max_probe.init_vel)

# step
# if y above, continue
# mark hit if hit
# if hit check