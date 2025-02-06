from djitellopy import Tello

drone = Tello()

drone.connect()
drone.takeoff()

drone.move_left(100)
drone.rotate_counter_clockwise(90)
drone.move_forward(100)

drone.land()