import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import imageio, os

class Drone:
    def __init__(self, position, load_capacity=0.5, acceleration=1.0, climb_rate=1.0, weight=1.0, size=1.0, battery_life=60.0):
        self.position = np.array(position)
        self.velocity = np.array([0.0, 0.0, 0.0])
        self.load_capacity = load_capacity
        self.acceleration = acceleration
        self.climb_rate = climb_rate
        self.weight = weight
        self.size = size
        self.battery_life = battery_life
        self.load = 0.0
        self.destroyed = False

    def destroy(self):
        self.destroyed = True 
        # change z coordinate to 0, others stay the same
        self.position[2] = 0.0
        

    def update_position(self):
        self.position += self.velocity

    def adjust_velocity(self, target_position):
        direction = target_position - self.position
        direction /= np.linalg.norm(direction)  # Normalize the direction.
        self.velocity = self.acceleration * direction

    def set_load(self, load):
        if load > self.load_capacity:
            raise ValueError("Load exceeds load capacity.")
        self.load = load
        self.battery_life -= load / self.load_capacity  # Decrease battery life based on load.


class Swarm:
    def __init__(self, num_drones):
        self.swarm = [Drone(5*np.random.rand(3)) for _ in range(num_drones)]
        self.filenames = []

    def set_formation(self, formation_type, **kwargs):
        if formation_type == 'linear':
            height = kwargs.get('height', 30.0)
            x_coord = kwargs.get('x_coord', 30.0)
            length = kwargs.get('length', 20.0)
            self.target_positions = [np.array([x_coord, height, i * length / len(self.swarm)]) for i in range(len(self.swarm))]
        elif formation_type == 'circular':
            height = kwargs.get('height', 30.0)
            radius = kwargs.get('radius', 10.0)
            center_xz = kwargs.get('center_xz', np.array([10.0, 10.0]))  # Now just x and z coordinates.
            angles = np.linspace(0, 2*np.pi, len(self.swarm), endpoint=False)
            self.target_positions = [np.array([center_xz[0] + radius * np.cos(angle), height, center_xz[1] + radius * np.sin(angle)]) for angle in angles]
        else:
            raise ValueError(f"Unknown formation type: {formation_type}")
 
    def update(self, frame):
        if frame == 100:
            self.set_formation('linear', height=30.0, x_coord=30.0, length=20.0)
        for drone, target_position in zip(self.swarm, self.target_positions):
            if not drone.destroyed:  # Only update drones that are not destroyed.
                drone.adjust_velocity(target_position)
        for drone in self.swarm:
            if not drone.destroyed:  # Only update drones that are not destroyed.
                drone.update_position()

    def plot(self, frame):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for i, drone in enumerate(self.swarm):
            ax.scatter(*drone.position)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_xlim([0, 50])
        ax.set_ylim([0, 50])
        ax.set_zlim([0, 50])
        
        filename = f'frame_{frame}.png'
        plt.savefig(filename)
        self.filenames.append(filename)

        plt.close(fig)

    def animate(self):
        with imageio.get_writer('drone_animation.gif' , duration=3, loop=0) as writer:
            for filename in self.filenames:
                image = imageio.imread(filename)
                writer.append_data(image)

        for filename in self.filenames:
            os.remove(filename)
    
    def print_drone_state(self):
        for i, drone in enumerate(self.swarm):
            print(f"Drone {i}:")
            print(f"Position: {drone.position}")
            #print(f"Velocity: {drone.velocity}")
            print(f"Load: {drone.load}")
            print(f"Battery life: {drone.battery_life}")
            print()


sim = Swarm(30)
sim.set_formation('circular', height=30.0, radius=20.0, center_xz=np.array([30.0, 30.0]))


# Run the simulation for 150 frames.
for frame in range(200):
    sim.update(frame)
    if frame % 5 == 0:
        sim.plot(frame)
    if frame==100:
        # destroy drone 1 to 5
        for i in range(5):
            sim.swarm[i].destroy()

        sim.set_formation('linear', height=30.0, x_coord=30.0, length=20.0)
        sim.print_drone_state()

sim.print_drone_state()

# Create an animation from the simulation.
sim.animate()
