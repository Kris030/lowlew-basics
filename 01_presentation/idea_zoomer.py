import random
from math import ceil
from manim import *

from manim_editor import PresentationSectionType

random.seed(123)

def zoom_into(obj: Mobject):
	def zoomer(s: Scene):
		os = s.get_top_level_mobjects()
		s.play(
			*[FadeOut(o) for o in os if o is not obj],
			obj.animate
				.move_to(ORIGIN)
				.scale(200)
				.set_opacity(0)
		)
	return zoomer

def fade_prev(s: Scene):
	os = s.get_top_level_mobjects()
	if len(os):
		s.play(*[FadeOut(o) for o in os])

def my_scene(ps: Scene, s: Scene, t: str, obj: Mobject, ptype: PresentationSectionType=PresentationSectionType.NORMAL):
	s.next_section(type(s).__name__, type=ptype)
	x = Text(t).shift(UP * 3)
	s.play(
		Transform(obj, x) if obj is not None else Write(x),
		*[FadeOut(o) for o in ps.get_top_level_mobjects() if o is not obj] if ps else []
	)

class Intro(Scene):
	def construct(self) -> None:
		self.next_section('Intro', type=PresentationSectionType.NORMAL)

		t2 = Text('the boi')
		t2.shift(UP)
		self.play(t2.animate.shift(DOWN * 2).scale(.75))

		t1 = Text('Hogy a rákba működik is a szmitó?', color=YELLOW)
		self.play(Write(t1))
		self.play(FadeOut(t1), FadeOut(t2))

class Parts(Scene):

	def mem_get_table(self, i: int) -> Table:
		return self.ta[i // 8]

	def mem_get_cell(self, i: int) -> Polygon:
		return self.mem_get_table(i).get_cell((1, 2 + i % 8))

	def mem_move_p(self, i: int) -> None:
		c = self.mem_get_cell(i)
		return self.p.copy().move_to(c.get_center() + UP * c.height / 1.5)

	def mem_move_ph(self, i: int) -> None:
		c = self.mem_get_cell(i)
		return self.ph.copy().move_to(c.get_center() + DOWN * self.ch / 2)

	def mem_table(self, t: int) -> Table:

		labels = ['Cím'] + [f'{x + t * 8:02x}' for x in range(8)]

		values = ['Érték']
		for x in range(8):
			values.append(f'{self.mem[t * 8 + x]:02x}')

		o2 = Table([labels, values], include_outer_lines=True)
		o2.set_row_colors(YELLOW, GRAY)
		o2.shift((t - .25) * 2.5 * DOWN)
		o2.scale(.65)
		return o2
	
	def mem_simulate(self) -> None:
		j = 1
		for i in range(9):
			self.play(Transform(self.p, self.mem_move_p(j)), Transform(self.ph, self.mem_move_ph(j)))
			if self.mem[j] % 2:
				j += 1
			else:
				j += 3
			j %= len(self.mem)

	def construct(self) -> None:
		my_scene(None, self, 'Részei', None, ptype=PresentationSectionType.SKIP)
		
		bbs = Square()
		bbt = Text('?')

		bb = VGroup(bbs, bbt)
		self.bb = bb

		RAMs = Square()
		RAMt = Text('RAM').scale(.9)
		RAM = VGroup(RAMs, RAMt).set_color(GREEN).scale(.75)

		self.play(Create(RAMs), Write(RAMt))
		self.play(RAM.animate.next_to(bb, LEFT * 2))
		RAMw = [
			Line(start=RAM.get_right(), end=bb.get_left()).shift(UP / 3),
			Line(start=bb.get_left(), end=RAM.get_right()).shift(DOWN / 3),
		]

		CPUs = Square()
		CPUr = Text('CPU').scale(.9)

		CPU = VGroup(CPUs, CPUr).set_color(RED).scale(.75)

		self.play(Create(CPUs), Write(CPUr))
		self.play(CPU.animate.next_to(bb, RIGHT * 2))
		CPUw = [
			Line(start=CPU.get_left(), end=bb.get_right()).shift(UP / 3),
			Line(start=bb.get_right(), end=CPU.get_left()).shift(DOWN / 3),
		]

		IOs = Square()
		IOr = Text('IO').scale(.9)

		IO = VGroup(IOs, IOr).set_color(BLUE).scale(.75)

		self.play(Create(IOs), Write(IOr))
		self.play(IO.animate.next_to(bb, DOWN * 2))
		IOw = [
			Line(start=IO.get_top(), end=bb.get_bottom()).shift(LEFT / 3),
			Line(start=bb.get_bottom(), end=IO.get_top()).shift(RIGHT / 3),
		]

		RAM.add(*RAMw)
		CPU.add(*CPUw)
		IO.add(*IOw)

		wires = RAMw + IOw + CPUw

		self.play(FadeIn(bbs), Write(bbt),
			*[Create(w) for w in wires],
			*[w.animate.set_color(YELLOW) for w in wires]
		)

		self.next_section('PartsLoop', type=PresentationSectionType.LOOP)

		dotAnims = [
			Dot(point=w.get_start(), color=YELLOW)
				.animate(rate_func=linear).move_to(w.get_end())
					for ws in wires for w in ws
		]
		dots = VGroup(*[d.mobject for d in dotAnims])
		
		parts = VGroup(bb, RAM, CPU, IO)
		
		self.play(*[FadeIn(d) for d in dots], run_time=.3)
		self.play(*dotAnims, run_time=.3)
		self.play(*[FadeOut(d) for d in dots], run_time=.3)

#class IO(Scene):
#	def construct(self):
		my_scene(self, self, 'IO', IO)

		drs = 5
		dcs = 24
		rbs = 12

		bios_text = Text('BIOS', color=YELLOW)
		self.play(Write(bios_text))

		self.next_section('After BIOS explanation', type=PresentationSectionType.NORMAL)

		rdb = VGroup(*[
			Dot(fill_opacity=0,
				color=YELLOW if dcs * i + j < rbs else WHITE)
				.shift(RIGHT * j / 2 + DOWN * i / 2)
					for i in range(drs)
						for j in range(-dcs // 2, dcs // 2)
		]).shift(DOWN)
		self.play(rdb.animate(lag_ratio=.2).set_opacity(1), run_time=1.5)

		self.play(
			Transform(
				VGroup(bios_text, *rdb[:rbs * 2]),
				VGroup(*[
					rdb[i].copy().move_to(LEFT * rbs / 4 + i * RIGHT / 4)
							for i in range(rbs * 2)
				])
			)
		)

		self.play(*[FadeOut(b) for b in rdb[rbs * 2:]])

		self.play(Transform(VGroup(*self.get_top_level_mobjects()), parts))
		
#class MEMORY(Scene):
#	def construct(self):
		# --------------------- MEMORY SCENE ---------------------
		self.wait(1)
		my_scene(self, self, 'Memória', RAM, ptype=PresentationSectionType.LOOP)
		
		tc = 2

		self.mem = [random.randrange(0, 255) for x in range(tc * 8)]

		t1, t2 = self.ta = [self.mem_table(i) for i in range(tc)]
		ts = VGroup(*self.ta)

		self.play(Create(ts, run_time=2))
		
		self.p = Triangle(color=RED, fill_color=RED, fill_opacity=1)
		self.p.rotate(PI)
		self.p.scale(.25)
		
		c = t1.get_cell((1, 2))
		self.p.move_to(c.get_center() + UP * c.height / 1.5)

		c = t1.get_cell((1, 2))

		hls = t1.get_vertical_lines()
		self.cw = hls[1].get_start()[1] - hls[2].get_start()[1] #c.width * .9
		self.ch = len(hls[0])
		self.ph = Rectangle(width=self.cw, height=self.ch * 2,
						color=BLACK, fill_color=RED, fill_opacity=.3)
		self.ph.z_index -= 1
		
		self.ph.move_to(c.get_center() + DOWN * self.ch / 2)

		self.play(FadeIn(self.ph))

		self.mem_simulate()
		

		
		self.play(Transform(VGroup(*self.get_top_level_mobjects()), parts))

# class CPU(Scene):
# 	def construct(self):
		self.wait(1)
		my_scene(self, self, 'CPU', CPU)
		self.remove(bbt)

		# cpt = Table(
		# 	[
		# 		[
		# 			'', 'R', 'X', 'H', 'L'
		# 		],
		# 		[
		# 			'A', 'RAX', 'AX', 'AH', 'AL'
		# 		],
		# 		[
		# 			'B', 'RBX', 'BX', 'BH', 'BL'
		# 		]
		# 	], include_outer_lines=True
		# )
		# self.play(Create(cpt))
		
		self.play(Transform(VGroup(*self.get_top_level_mobjects()), parts))
		self.play(*[FadeOut(o) for o in self.get_top_level_mobjects()])


class Outro(Scene):
	def construct(self) -> None:
		my_scene(None, self, 'Outro', None)
		
