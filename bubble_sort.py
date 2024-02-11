from pyglet.window import Window
from pyglet.app import run
from pyglet.shapes import Rectangle
from pyglet.graphics import Batch
from pyglet import clock
import random

class BubbleSortVisualizer(Window):
    def __init__(self):
        super(BubbleSortVisualizer, self).__init__(2000, 750, "Bubble Sort Visualization - Step by Step")
        self.batch = Batch()
        self.x = list(range(1, 100))
        random.shuffle(self.x)  # Shuffle the list
        self.bars = []
        self.create_rectangles()

        self.current_i = 0
        self.current_j = 0
        self.sorted = False

    def create_rectangles(self):
        for e, i in enumerate(self.x):
            self.bars.append(Rectangle(50 + e * 20, 100, 4, i * 10, batch=self.batch, color=(255, 255, 255)))

    def reset_sort(self):
        self.x = list(range(1, 200))
        random.shuffle(self.x)
        self.bars = []
        self.create_rectangles()
        self.current_i = 0
        self.current_j = 0
        self.sorted = False

    def on_update(self, deltatime):
        if not self.sorted:
            n = len(self.x)
            if self.current_i < n - 1:
                if self.current_j < n - 1 - self.current_i:
                    if self.x[self.current_j] > self.x[self.current_j + 1]:
                        # Swap heights in the list
                        self.x[self.current_j], self.x[self.current_j + 1] = self.x[self.current_j + 1], self.x[self.current_j]

                        # Move rectangles to new positions with a smooth transition
                        destination_height = self.bars[self.current_j].height
                        source_height = self.bars[self.current_j + 1].height
                        self.bars[self.current_j].height = source_height
                        self.bars[self.current_j + 1].height = destination_height

                        # Change color during the swap
                        self.bars[self.current_j].color = (255, 0, 0)  # Red
                        self.bars[self.current_j + 1].color = (255, 0, 0)  # Red

                    # Reset color for all bars
                    for bar in self.bars:
                        bar.color = (255, 255, 255)

                    self.current_j += 1
                else:
                    self.current_i += 1
                    self.current_j = 0
            else:
                self.sorted = True

    def on_draw(self):
        self.clear()
        self.batch.draw()

visualizer = BubbleSortVisualizer()
clock.schedule_interval(visualizer.on_update, 0.0001)  # Adjust the interval for smoother animation
run()
