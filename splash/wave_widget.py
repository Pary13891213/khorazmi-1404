from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics import Color, Line
import math, random

class WaveWidget(FloatLayout): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.neon = Image(
            source="images/Light1.png",
            size_hint=(None, None),
            size=(380, 380),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.add_widget(self.neon)

        self.time = 0
        self.layers = []
        for i in range(5):
            self.layers.append({
                "n1": random.randint(1, 3),
                "n2": random.randint(2, 5),
                "n3": random.randint(4, 7),

                "amp1": random.uniform(12, 20),
                "amp2": random.uniform(8, 14),
                "amp3": random.uniform(5, 10),

                "w1": random.uniform(0.1, 0.7),
                "w2": random.uniform(0.7, 1.5),
                "w3": random.uniform(1.5, 2.2),
                "color": (1, 1, 1, 0.45 + i * 0.1),
            })

        Clock.schedule_interval(self.animate, 1 / 60)

    def animate(self, dt):
        self.time += dt
        self.canvas.before.clear()

        cx = self.center_x
        cy = self.center_y
        base_radius = min(self.width, self.height) * 0.4
        N = 720
        t = self.time

        with self.canvas.before:
            for layer in self.layers:
                Color(*layer["color"])
                points = []
                n1, n2, n3 = layer["n1"], layer["n2"], layer["n3"]
                a1, a2, a3 = layer["amp1"], layer["amp2"], layer["amp3"]
                w1, w2, w3 = layer["w1"], layer["w2"], layer["w3"]

                for i in range(N + 1):
                    theta = 2 * math.pi * (i / N)
                    r = base_radius \
                        + math.sin(n1 * theta + w1 * t) * a1 \
                        + math.sin(n2 * theta + w2 * t) * a2 \
                        + math.sin(n3 * theta + w3 * t) * a3
                    x = cx + r * math.cos(theta)
                    y = cy + r * math.sin(theta)
                    points.extend([x, y])

                points[-2:] = points[:2]
                Line(points=points, width=1)
