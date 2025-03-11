import numpy as np
from manim import *


class GDPOverTime(Scene):
    def construct(self):
        # Title
        title = Text("GDP Growth Over Time", font_size=40)
        subtitle = Text("Understanding Economic Growth", font_size=30)
        subtitle.next_to(title, DOWN)
        title_group = VGroup(title, subtitle)

        self.play(Write(title_group))
        self.wait(1)
        self.play(FadeOut(title_group))

        # Create axes
        axes = Axes(
            x_range=[1960, 2020, 10],
            y_range=[0, 25, 5],
            axis_config={"include_tip": False},
            x_axis_config={"numbers_to_include": np.arange(1960, 2021, 20)},
            y_axis_config={"numbers_to_include": np.arange(0, 26, 5)},
        )

        axes_labels = axes.get_axis_labels(x_label="Year", y_label="GDP (Trillion \\$)")

        # Add title to the graph
        graph_title = Text("Global GDP Growth (1960-2020)", font_size=30)
        graph_title.to_edge(UP)

        self.play(Create(axes), Write(axes_labels), Write(graph_title))
        self.wait(1)

        # GDP data points (simplified for visualization)
        # Source: World Bank data, simplified for animation purposes
        years = np.arange(1960, 2021, 5)
        gdp_values = [
            1.4,
            2.2,
            3.4,
            6.4,
            11.3,
            18.3,
            31.5,
            33.6,
            47.4,
            65.6,
            84.9,
            96.1,
            97.8,
        ]  # Added 2020 value

        # Create the GDP curve
        gdp_points = [
            axes.coords_to_point(years[i], gdp_values[i]) for i in range(len(years))
        ]
        gdp_line = VMobject()
        gdp_line.set_points_smoothly(gdp_points)
        gdp_line.set_color(BLUE)

        # Animate the drawing of the curve
        self.play(Create(gdp_line), run_time=3)
        self.wait(1)

        # Highlight key periods with explanations

        # Post-WWII Boom
        boom_period = Rectangle(
            width=axes.x_axis.get_length() * 0.2,
            height=axes.y_axis.get_length() * 0.2,
            color=GREEN,
        ).move_to(axes.coords_to_point(1965, 2.5))

        boom_text = Text("Post-WWII Economic Boom", font_size=20, color=GREEN)
        boom_text.next_to(boom_period, UP)

        self.play(Create(boom_period), Write(boom_text))
        self.wait(1.5)

        # Oil Crisis
        oil_period = Rectangle(
            width=axes.x_axis.get_length() * 0.15,
            height=axes.y_axis.get_length() * 0.15,
            color=RED,
        ).move_to(axes.coords_to_point(1975, 6))

        oil_text = Text("Oil Crisis Slowdown", font_size=20, color=RED)
        oil_text.next_to(oil_period, UP)

        self.play(Create(oil_period), Write(oil_text))
        self.wait(1.5)

        # Tech Boom
        tech_period = Rectangle(
            width=axes.x_axis.get_length() * 0.15,
            height=axes.y_axis.get_length() * 0.15,
            color=YELLOW,
        ).move_to(axes.coords_to_point(1995, 35))

        tech_text = Text("Tech Boom", font_size=20, color=YELLOW)
        tech_text.next_to(tech_period, UP)

        self.play(Create(tech_period), Write(tech_text))
        self.wait(1.5)

        # Financial Crisis
        crisis_period = Rectangle(
            width=axes.x_axis.get_length() * 0.1,
            height=axes.y_axis.get_length() * 0.1,
            color=RED,
        ).move_to(axes.coords_to_point(2008, 65))

        crisis_text = Text("Financial Crisis", font_size=20, color=RED)
        crisis_text.next_to(crisis_period, UP)

        self.play(Create(crisis_period), Write(crisis_text))
        self.wait(1.5)

        # Clean up and prepare for the next segment
        cleanup_group = VGroup(
            boom_period,
            boom_text,
            oil_period,
            oil_text,
            tech_period,
            tech_text,
            crisis_period,
            crisis_text,
        )
        self.play(FadeOut(cleanup_group))
        self.wait(1)

        # GDP Components Breakdown
        gdp_formula = MathTex("GDP = C + I + G + (X - M)")
        gdp_formula.to_edge(UP, buff=0.5)

        self.play(FadeOut(graph_title), Write(gdp_formula))
        self.wait(1)

        component_texts = [
            "C = Consumer Spending",
            "I = Business Investment",
            "G = Government Spending",
            "X = Exports",
            "M = Imports",
        ]

        components = VGroup(*[Text(text, font_size=24) for text in component_texts])
        components.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        components.next_to(gdp_formula, DOWN, buff=0.5)

        for component in components:
            self.play(Write(component))
            self.wait(0.5)

        self.wait(1)

        # Transition to pie chart
        self.play(FadeOut(components), FadeOut(gdp_formula))

        # Create a pie chart showing typical GDP components
        pie_title = Text("Typical GDP Composition", font_size=30)
        pie_title.to_edge(UP)

        self.play(Write(pie_title))

        # Values are approximate percentages for visualization
        pie_values = [60, 20, 15, 5]  # C, I, G, Net Exports
        pie_colors = [BLUE, GREEN, YELLOW, RED]
        pie_labels = [
            "Consumer\nSpending\n60%",
            "Business\nInvestment\n20%",
            "Government\nSpending\n15%",
            "Net Exports\n5%",
        ]

        pie = VGroup()
        total = sum(pie_values)
        start_angle = 0

        # Create pie sectors
        sectors = VGroup()
        labels = VGroup()

        for i, (value, color, label_text) in enumerate(
            zip(pie_values, pie_colors, pie_labels)
        ):
            angle = value * 2 * PI / total
            sector = Sector(
                radius=2,
                angle=angle,
                start_angle=start_angle,
                color=color,
                fill_opacity=0.8,
            )
            sectors.add(sector)

            # Position labels
            mid_angle = start_angle + angle / 2
            label_pos = sector.get_center() * 1.5
            label = Text(label_text, font_size=20)
            label.move_to(label_pos)
            labels.add(label)

            start_angle += angle

        pie = VGroup(sectors, labels)
        pie.next_to(pie_title, DOWN, buff=0.5)

        self.play(Create(sectors), run_time=2)
        for label in labels:
            self.play(Write(label))

        self.wait(2)

        # Final message
        final_title = Text("Factors Affecting GDP Growth", font_size=36)
        final_title.to_edge(UP)

        self.play(
            FadeOut(pie),
            FadeOut(pie_title),
            FadeOut(axes),
            FadeOut(axes_labels),
            FadeOut(gdp_line),
            Write(final_title),
        )

        factors = [
            "Technology & Innovation",
            "Education & Human Capital",
            "Natural Resources",
            "Political Stability",
            "Trade Relations",
            "Infrastructure",
        ]

        factor_texts = VGroup(*[Text(factor, font_size=30) for factor in factors])
        factor_texts.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        factor_texts.next_to(final_title, DOWN, buff=0.5)

        for factor in factor_texts:
            self.play(Write(factor))
            self.wait(0.5)

        self.wait(2)

        # Conclusion
        conclusion = Text(
            "Understanding GDP helps us measure economic growth and prosperity",
            font_size=24,
        )
        conclusion.next_to(factor_texts, DOWN, buff=0.8)

        self.play(Write(conclusion))
        self.wait(3)

        self.play(FadeOut(VGroup(final_title, factor_texts, conclusion)))

        # Final credits
        credits = Text("Created with Manim", font_size=30)
        self.play(Write(credits))
        self.wait(2)
        self.play(FadeOut(credits))
        self.wait(1)
