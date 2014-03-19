#!/usr/bin/env python
# main program for group 4
from terrain  import terrain_class
from bike_factory import bike_factory_class
from animate import animate_class
from physics import physics_class

terrain = terrain_class(rand=5)

for i in xrange(5):
    factory = bike_factory_class(5)

#go simulation
    for new_bike in factory:
    
        physics = physics_class(new_bike,terrain)
        animate  = animate_class(new_bike,terrain)

<<<<<<< HEAD
        for time in xrange(30000):
=======
        for time in xrange(100000):
>>>>>>> c7cdafb77a3927ab99a73b08fdbdfb4bf1d433ab
	    physics.step()
	    if not time%10:
		animate.draw()
		pass
	    if physics.stuck():
		break
	animate.close()
	
# get some data from physics and story the bike result
	rr = physics.get_result()
	print "result = ", rr
        new_bike.result = rr

    factory.make_new_generation()		#make some improovements genetics

