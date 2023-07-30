import matplotlib.pyplot as plt
# Define the car class
class Car:
    def __init__(self):
        self.position = 0

    def drive(self, speed):
        self.position += speed
# Create a car instance
car = Car()

# Simulate the car driving
positions = []
speeds = [2, 3, 4, 5]  # Sample speeds

for speed in speeds:
    car.drive(speed)
    positions.append(car.position)
# Plot the car's positions
plt.plot(positions)
plt.xlabel("Time")
plt.ylabel("Position")
plt.title("Self-Driving Car Simulation")
plt.show()
