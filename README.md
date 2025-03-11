# YouTube Video Repository

This repository contains code for creating educational videos using Manim, a mathematical animation engine. The videos visualize complex concepts through animations and are designed to be uploaded to YouTube.

## Overview

Manim is a powerful animation engine for explanatory math videos, created by Grant Sanderson (3Blue1Brown). This repository uses Manim to create videos that visualize various concepts in an engaging and educational way.

## Installation

### Prerequisites

Before installing Manim, you need to install several system dependencies:

#### Debian/Ubuntu

```bash
# Install pkg-config (required for finding libraries)
sudo apt-get install pkg-config

# Install CMake (build system)
sudo apt-get install cmake

# Install Cairo and its development files
sudo apt-get install libcairo2-dev

# Install other required dependencies for Manim
sudo apt-get install python3-dev libpango1.0-dev ffmpeg texlive texlive-latex-extra texlive-fonts-extra texlive-latex-recommended texlive-science
```

You can also install these dependencies individually:

```bash
sudo apt update
sudo apt install ffmpeg
sudo apt install libcairo2-dev
sudo apt install libpango1.0-dev
sudo apt install texlive texlive-latex-extra texlive-fonts-extra texlive-latex-recommended texlive-science
```

### Installing Manim

After installing the dependencies, you can install Manim using pip:

```bash
pip install manim
```

## Running the Animations

To render an animation, use the `manim` command followed by the script file and the scene class name:

```bash
manim -pql gdp_animation.py GDPOverTime
```

### Command Options:

- `-p`: Preview the animation once it's done
- `-l`: Use low quality (faster rendering for testing)
- `-m`: Use medium quality
- `-h`: Use high quality (slower, but better for final videos)
- `-ql`: Combine quality and preview flags (low quality with preview)
- `-qm`: Medium quality with preview
- `-qh`: High quality with preview

## Project Structure

```
youtube-video/
├── animations/
│   ├── gdp_animation.py
│   ├── physics_concept.py
│   └── math_visualization.py
├── assets/
│   ├── images/
│   └── data/
├── rendered/
│   ├── videos/
│   └── thumbnails/
└── utils/
    └── helpers.py
```

## Example Scene

Here's a simple example of a Manim scene:

```python
from manim import *

class GDPOverTime(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 100, 10],
            axis_config={"include_tip": False}
        )
        
        # Add labels
        x_label = axes.get_x_axis_label(r"\text{Year}")
        y_label = axes.get_y_axis_label(r"\text{GDP (Trillion \$)}")
        
        # Create graph
        graph = axes.plot(lambda x: x**2, color=BLUE)
        
        # Create dots for specific points
        dots = VGroup()
        for x in range(11):
            dot = Dot(axes.c2p(x, x**2), color=YELLOW)
            dots.add(dot)
        
        # Animation sequence
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait()
        self.play(Create(graph), run_time=2)
        self.wait()
        self.play(Create(dots), run_time=1)
        self.wait(2)
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-animation`)
3. Commit your changes (`git commit -m 'Add amazing animation'`)
4. Push to the branch (`git push origin feature/amazing-animation`)
5. Open a Pull Request

## Resources

- [Manim Documentation](https://docs.manim.community/)
- [3Blue1Brown](https://www.3blue1brown.com/) - For inspiration
- [Manim Community](https://www.manim.community/)

## License

This project is licensed under the MIT License - see the LICENSE file for details.