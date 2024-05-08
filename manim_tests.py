from manim import *
from manim_physics import *
from manim_data_structures import *
from manim_cad_drawing_utils import *

class StandingWaveExampleScene(Scene):
    def construct(self):
        wave1 = StandingWave(1)
        wave2 = StandingWave(2)
        wave3 = StandingWave(3)
        wave4 = StandingWave(4)
        waves = VGroup(wave1, wave2, wave3, wave4)
        waves.arrange(DOWN).move_to(ORIGIN)
        self.add(waves)
        for wave in waves:
            wave.start_wave()
        self.wait()

class LinearWaveExampleScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(60 * DEGREES, -45 * DEGREES)
        wave = LinearWave()
        self.add(wave)
        wave.start_wave()
        self.wait()
        wave.stop_wave()

class MainScene(Scene):
    def construct(self):
        # Create an array
        arr = MArray([8, 7, 6, 5, 4])
        self.play(Create(arr))

        # Animate array
        self.play(arr.animate.shift(UP * 2.5 + LEFT * 5))

        # Animate array element
        self.play(arr.animate_elem(3).shift(DOWN * 0.5))

        # Animate array element mobjects
        self.play(arr.animate_elem_square(0).set_fill(BLACK), arr.animate_elem_value(0).rotate(PI / 2).set_fill(RED), arr.animate_elem_index(0).rotate(PI / 2))

        # Display array with hex values
        arr2 = MArray([0, 2, 4, 6, 8], index_hex_display=True, index_offset=4)
        self.play(Create(arr2))
        self.play(arr2.animate.shift(DOWN * 2.5 + LEFT * 5))

        # Create customized array
        arr3 = MArray([1, 1, 2], mob_square_args={'color': GRAY_A, 'fill_color': RED_E, 'side_length': 0.5}, mob_value_args={'color': GOLD_A, 'font_size': 28}, mob_index_args={'color': RED_E, 'font_size': 22})
        self.play(Create(arr3))

        # Append element
        self.play(Write(arr2.append_elem(10)))

        # Append customized element
        self.play(Write(arr2.append_elem(12, mob_square_args={'fill_color': BLACK})))

        # Update value of element
        self.play(Write(arr2.update_elem_value(3, 0, mob_value_args={'color': RED})), arr2.animate_elem_square(3).set_fill(WHITE))

        self.wait()
    
class test_dimension(Scene):
    def construct(self):
        mob1 = Round_Corners(Triangle().scale(2),0.3)
        dim1 = Angle_Dimension_Mob(mob1,
                                   0.2,
                                   0.6,
                                   offset=-4,
                                   ext_line_offset=1,
                                   color=RED)
        dim2 = Linear_Dimension(mob1.get_critical_point(RIGHT),
                                mob1.get_critical_point(LEFT),
                                direction=UP,
                                offset=2.5,
                                outside_arrow=True,
                                ext_line_offset=-1,
                                color=RED)
        self.play(Create(mob1))
        self.play(Create(dim1), run_time=3)
        self.play(Create(dim2), run_time=3)
        self.wait(3)
        self.play(Uncreate(mob1), Uncreate(dim2))