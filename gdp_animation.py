import numpy as np
from manim import *

class GDPOverTime(Scene):
    def construct(self):
        # Configure for Full HD
        self.camera.frame_width = 16
        self.camera.frame_height = 9
        
        # Title and subtitle with refined positioning
        title = Text("GDP Growth Over Time", font_size=48)
        title.to_edge(UP, buff=0.8)  # Increased buffer for breathing room
        subtitle = Text("Understanding Economic Growth", font_size=32)
        subtitle.next_to(title, DOWN, buff=0.4)  # Slightly larger gap
        title_group = VGroup(title, subtitle)

        self.play(Write(title_group))
        self.wait(1)
        self.play(FadeOut(title_group))

        # Create axes with optimized size and position
        axes = Axes(
            x_range=[1960, 2020, 10],
            y_range=[0, 100, 10],
            axis_config={"include_tip": False},
            x_axis_config={"numbers_to_include": np.arange(1960, 2021, 20)},
            y_axis_config={"numbers_to_include": np.arange(0, 101, 20)},
        )
    
        axes.scale(0.75)  # Slightly smaller to fit annotations better
        axes.center()
        axes.shift(DOWN * 1.0)  # More downward shift to avoid title overlap

        axes_labels = axes.get_axis_labels(x_label="Year", y_label="GDP (Trillion \\$)")

        # Graph title and subtitle with better spacing
        graph_title = Text("Global GDP Growth (1960-2020)", font_size=36)
        graph_title.to_edge(UP, buff=0.8)
        graph_sub = Text("Showing global economic expansion across six decades", font_size=24)
        graph_sub.next_to(graph_title, DOWN, buff=0.4)

        self.play(Create(axes), Write(axes_labels))
        self.play(Write(graph_title), Write(graph_sub))
        self.wait(1)

        # GDP data points (World Bank data in trillion USD)
        years = np.arange(1960, 2021, 5)
        gdp_values = [1.39, 2.16, 2.99, 5.99, 11.33, 12.86, 22.73, 31.08, 33.73, 47.72, 66.58, 75.12, 84.71]

        # Create the GDP curve
        gdp_points = [axes.coords_to_point(years[i], gdp_values[i]) for i in range(len(years))]
        gdp_line = VMobject()
        gdp_line.set_points_smoothly(gdp_points)
        gdp_line.set_color(BLUE)

        self.play(Create(gdp_line), run_time=3)
        self.wait(1)

        # Highlight key periods with improved positioning
        # Post-WWII Boom
        boom_period = Rectangle(
            width=axes.x_axis.get_length() * 0.2,
            height=axes.y_axis.get_length() * 0.2,
            color=GREEN,
        ).move_to(axes.coords_to_point(1965, 7))

        boom_text = Text("Post-WWII Economic Boom", font_size=24, color=GREEN)
        boom_text.next_to(boom_period, UP, buff=0.3)  # Increased buffer
        boom_sub = Text("Steady growth following postwar reconstruction", font_size=20)
        boom_sub.to_edge(DOWN, buff=0.8)  # Higher up to avoid overlap

        self.play(Create(boom_period), Write(boom_text), Write(boom_sub))
        self.wait(1.5)
        self.play(FadeOut(boom_sub))

        # Oil Crisis
        oil_period = Rectangle(
            width=axes.x_axis.get_length() * 0.15,
            height=axes.y_axis.get_length() * 0.15,
            color=RED,
        ).move_to(axes.coords_to_point(1975, 11))

        oil_text = Text("Oil Crisis Slowdown", font_size=24, color=RED)
        oil_text.next_to(oil_period, UP, buff=0.3)
        oil_sub = Text("Economic impact of the 1970s energy crisis", font_size=20)
        oil_sub.to_edge(DOWN, buff=0.8)

        self.play(Create(oil_period), Write(oil_text), Write(oil_sub))
        self.wait(1.5)
        self.play(FadeOut(oil_sub))

        # Tech Boom
        tech_period = Rectangle(
            width=axes.x_axis.get_length() * 0.15,
            height=axes.y_axis.get_length() * 0.15,
            color=YELLOW,
        ).move_to(axes.coords_to_point(1995, 36))

        tech_text = Text("Tech Boom", font_size=24, color=YELLOW)
        tech_text.next_to(tech_period, UP, buff=0.3)
        tech_sub = Text("Rapid growth driven by computing and internet", font_size=20)
        tech_sub.to_edge(DOWN, buff=0.8)

        self.play(Create(tech_period), Write(tech_text), Write(tech_sub))
        self.wait(1.5)
        self.play(FadeOut(tech_sub))

        # Financial Crisis
        crisis_period = Rectangle(
            width=axes.x_axis.get_length() * 0.1,
            height=axes.y_axis.get_length() * 0.1,
            color=RED,
        ).move_to(axes.coords_to_point(2008, 65))

        crisis_text = Text("Financial Crisis", font_size=24, color=RED)
        crisis_text.next_to(crisis_period, UP, buff=0.3)
        crisis_sub = Text("Global downturn after housing collapse", font_size=20)
        crisis_sub.to_edge(DOWN, buff=0.8)

        self.play(Create(crisis_period), Write(crisis_text), Write(crisis_sub))
        self.wait(1.5)

        # Clean up
        cleanup_group = VGroup(
            boom_period, boom_text, oil_period, oil_text,
            tech_period, tech_text, crisis_period, crisis_text, crisis_sub
        )
        self.play(FadeOut(cleanup_group))
        self.wait(1)

        # GDP Components Breakdown with refined positioning
        self.play(FadeOut(graph_title), FadeOut(graph_sub))
        
        gdp_formula = MathTex("GDP = C + I + G + (X - M)")
        gdp_formula.scale(1.2)
        gdp_formula.move_to(UP * 3)  # Precise positioning

        formula_title = Text("The GDP Formula", font_size=36)
        formula_title.next_to(gdp_formula, UP, buff=0.5)
        formula_sub = Text("Components of Gross Domestic Product", font_size=24)
        formula_sub.next_to(gdp_formula, DOWN, buff=0.5)

        self.play(Write(formula_title), Write(gdp_formula), Write(formula_sub))
        self.wait(1)

        component_texts = [
            "C = Consumer Spending",
            "I = Business Investment",
            "G = Government Spending",
            "X = Exports",
            "M = Imports",
        ]

        components = VGroup(*[Text(text, font_size=28) for text in component_texts])
        components.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        components.next_to(formula_sub, DOWN, buff=0.7)

        for component in components:
            self.play(Write(component))
            self.wait(0.5)

        self.wait(1)
        self.play(FadeOut(components), FadeOut(gdp_formula), FadeOut(formula_title), FadeOut(formula_sub))

        # Pie chart with optimized positioning
        pie_title = Text("Typical GDP Composition", font_size=36)
        pie_title.to_edge(UP, buff=0.8)
        pie_sub = Text("Average distribution in developed economies", font_size=24)
        pie_sub.next_to(pie_title, DOWN, buff=0.4)

        self.play(Write(pie_title), Write(pie_sub))

        pie_values = [60, 20, 15, 5]  # C, I, G, Net Exports
        pie_colors = [BLUE, GREEN, YELLOW, RED]
        pie_labels = [
            "Consumer\nSpending\n60%",
            "Business\nInvestment\n20%",
            "Government\nSpending\n15%",
            "Net Exports\n5%",
        ]

        sectors = VGroup()
        labels = VGroup()
        total = sum(pie_values)
        start_angle = 0

        for value, color, label_text in zip(pie_values, pie_colors, pie_labels):
            angle = value * 2 * PI / total
            sector = Sector(
                radius=2.8,  # Slightly larger for clarity
                angle=angle,
                start_angle=start_angle,
                color=color,
                fill_opacity=0.8,
            )
            sectors.add(sector)

            mid_angle = start_angle + angle / 2
            label_pos = np.array([
                4.0 * np.cos(mid_angle),  # Farther from center
                4.0 * np.sin(mid_angle),
                0
            ])
            label = Text(label_text, font_size=24)
            label.move_to(label_pos)
            labels.add(label)

            start_angle += angle

        pie = VGroup(sectors, labels)
        pie.center()
        pie.shift(DOWN * 0.5)  # Adjusted to avoid title overlap

        self.play(Create(sectors), run_time=2)
        for label in labels:
            self.play(Write(label))

        self.wait(2)

        # Final message with refined positioning
        self.play(
            FadeOut(pie), FadeOut(pie_title), FadeOut(pie_sub), FadeOut(axes),
            FadeOut(axes_labels), FadeOut(gdp_line)
        )
        
        final_title = Text("Factors Affecting GDP Growth", font_size=40)
        final_title.to_edge(UP, buff=0.8)
        factors_sub = Text("Key determinants of economic trends", font_size=28)
        factors_sub.next_to(final_title, DOWN, buff=0.4)

        self.play(Write(final_title), Write(factors_sub))

        factors = [
            "Technology & Innovation",
            "Education & Human Capital",
            "Natural Resources",
            "Political Stability",
            "Trade Relations",
            "Infrastructure",
        ]

        factor_texts = VGroup(*[Text(factor, font_size=32) for factor in factors])
        factor_texts.arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        factor_texts.next_to(factors_sub, DOWN, buff=0.8)
        factor_texts.center()

        for factor in factor_texts:
            self.play(Write(factor))
            self.wait(0.5)

        self.wait(2)

        # Conclusion with optimized placement
        conclusion = Text(
            "Understanding GDP measures economic prosperity",
            font_size=32,
        )
        conclusion.next_to(factor_texts, DOWN, buff=1.2)

        self.play(Write(conclusion))
        self.wait(3)

        self.play(FadeOut(VGroup(final_title, factors_sub, factor_texts, conclusion)))

        # Final credits
        credits = Text("Created with Manim", font_size=36)
        credits_sub = Text("© 2025 - Full HD Animation", font_size=24)
        credits_sub.next_to(credits, DOWN, buff=0.4)
        credits_group = VGroup(credits, credits_sub)
        credits_group.center()
        
        self.play(Write(credits_group))
        self.wait(2)
        self.play(FadeOut(credits_group))
        self.wait(1)