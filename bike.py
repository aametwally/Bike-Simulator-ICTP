import math
import random
import json

class bike_class(object):
    """
    The main purpose of this class is to generate a bike with many specifications like (Coordinates, Radius, Mass, Velocity, Acceleration, ....)
    """
    
    def __init__(self):
	from copy import deepcopy
	self._construction = [[6., 6.], [10., 6.], [10., 10.], [6., 10.]]
	self._position = deepcopy(self._construction)

	self._radius = [1., 1., 0., 0.]
	self._mass = [10., 10., 30., 30.]
	self._angle = [0. for i in xrange (4)]
	self._velocity = [[0. for i in xrange (2)] for i in xrange(4)]
	self._ang_velocity = [0. for i in xrange (4)]
	self._acceleration = [[0. for i in xrange (2)] for i in xrange(4)]
	self._ang_acceleration = [0. for i in xrange (4)]#[ang_a1,ang_a2,ang_a3,ang_a4]
	self._spring_const = [[0. for i in xrange (4)] for i in xrange(4)]
	self._spring_length = [[0. for i in xrange (4)] for i in xrange(4)]
	self._result=0
	for i in xrange (4):
	    for j in xrange(4):
		self.spring_const[i][j] = 10000.
		dx=self.position[j][0]-self.position[i][0]
		dy=self.position[j][1]-self.position[i][1]
		dr = math.sqrt(dx*dx + dy*dy)
		self._spring_length[i][j]=dr
		
    def randomize(self,size = 10., offset = 3.):
	"""This function produces random Bicycles. It has two arguments:
	
	Size = number of generated bikes
	
	offset = the displacement from the origin
	"""
	for i in xrange (2):
	    self._radius[i] = 0.5+2.5*random.random()
	for i in xrange (4):
	    for j in xrange(2):
		self._construction[i][j] = size*random.random()+offset
		self._spring_const[i][j] = (9.9*random.random()+0.1)*self._spring_const[i][j]
	self.check()
	return

    def check(self):
	"""
	This function calculate the spring_length
	"""
	from copy import deepcopy
	self._position = deepcopy(self._construction)
	for i in xrange (4):
	    for j in xrange(4):
		dx=self.position[j][0]-self.position[i][0]
		dy=self.position[j][1]-self.position[i][1]
		dr = math.sqrt(dx*dx + dy*dy)
		self._spring_length[i][j]=dr
	return

	
    @property
    def construction(self):
	"""
	This function get the value of the construction
	"""
	return self._construction

    @property
    def position(self):
	"""
	This function get the value of the bicycle coordinate
	"""
	return self._position
    
    @property
    def velocity(self):
	"""
	This function get the value of the velocity
	"""
	return self._velocity
	
    @property
    def acceleration(self):
	"""
	This function get the value of the acceleration
	"""
	return self._acceleration

    @property
    def angle(self):
	"""
	This function get the value of the angle of the wheels
	"""
	return self._angle
	
    @property
    def ang_velocity(self):
	"""
	This function get the value of the angular veleocity
	"""
	return self._ang_velocity

    @property
    def ang_acceleration(self):
	"""
	This function get the value of the angular acceleration
	"""
	return self._ang_acceleration	
    
    @property
    def radius(self):
	"""
	This function get the value of the raduis of the wheels
	"""
	return self._radius
	
    @property
    def mass(self):
	"""
	This function get the value of the mass at the four points 
	"""
	return self._mass
	
    @property
    def spring_const(self):
	"""
	This function get the value of the spring constants
	"""
	return self._spring_const
	
    @property
    def spring_length(self):
	"""
	This function get the value of the spring length
	"""
	return self._spring_length
	
    @property
    def result(self):
	"""
	This function get the value of the distance that each bike has moved 
	"""
	return self._result

	

    @construction.setter
    def construction(self, construction):
	self._construction = construction

    @position.setter
    def position(self, position):
	self._position = position
 
    @velocity.setter
    def velocity(self, velocity):
	self._velocity = velocity
	
    @acceleration.setter
    def acceleration(self, acceleration):
	self._acceleration = acceleration
 
    @angle.setter
    def angle(self, angle):
	self._angle = angle
	
    @ang_velocity.setter
    def ang_velocity(self, ang_velocity):
	self._ang_velocity = ang_velocity

    @ang_acceleration.setter
    def ang_acceleration(self, ang_acceleration):
	self._ang_acceleration = ang_acceleration	
    
    @radius.setter
    def radius(self, radius):
	self._radius = radius
	
    @mass.setter
    def mass(self, mass):
	self._mass = mass
	
    @spring_const.setter
    def spring_const(self, spring_const):
	self._spring_const = spring_const
	
    @spring_length.setter
    def spring_length(self, spring_length):
	self._spring_length = spring_length
	
    @result.setter
    def result(self, result):
	self._result=result
    
    def save_json(self, path):
	"""
	This function save bike objects into json files
	"""
	a = {
	    "position" : self._position,
	    "radius" : self._radius,
	    "mass"   : self._mass,
	    "result" : self._result,
	    "spring_const" : self._spring_const,
	    "spring_length" : self._spring_length,  
	    }
	x=json.dumps(a, sort_keys=True, indent=4)
	with open(path, 'wb') as fp:
	    fp.write(x)

	    
    def load_json(self, path):
	"""
	This function load json files into a dictionary 
	"""
	with open(path, 'rb') as fp:
	    y = json.load(fp)
	    return y
 
 
if __name__=="__main__":
    H=bike_class()
    H.randomize()
    x=H.save_json("data.json")
    data=H.load_json("data.json")
    #print data["position"]
    #print data["radius"]
    #print data["mass"]
    #print data["result"]
    #print data["spring_const"]
    #print data["spring_length"]