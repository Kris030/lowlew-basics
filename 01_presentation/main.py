from manim_editor import PresentationSectionType as PST
from random import random, randrange, seed as rand_seed
from animutils import *
from math import ceil
from manim import *

class Presentation(Scene):
	def construct(self) -> None:
		rand_seed(123)

		self.next_section('Intro', type=PST.NORMAL)

		auth = Text('the boi')
		self.play(auth.animate.shift(DOWN).scale(.75))

		title = Text('Hogyan is működik a szmitó?', color=YELLOW)
		self.play(Write(title))
		self.next_section('Hold intro screen', type=PST.SKIP)
		self.play(FadeOut(title), FadeOut(auth))

		self.next_section('Parts', type=PST.SKIP)
		
		BB_S = Square()
		BB_T = Text('?')
		BB = VGroup(BB_S, BB_T)

		RAM_S = Square()
		RAM_T = Text('RAM').scale(.9)
		RAM = VGroup(RAM_S, RAM_T).set_color(GREEN).scale(.75)

		self.play(Create(RAM_S), Write(RAM_T))
		self.play(RAM.animate.next_to(BB, LEFT * 2))
		RAM_W = [
			Line(start=RAM.get_right(), end=BB.get_left()).shift(UP / 3),
			Line(start=BB.get_left(), end=RAM.get_right()).shift(DOWN / 3),
		]

		CPU_S = Square()
		CPU_T = Text('CPU').scale(.9)
		CPU = VGroup(CPU_S, CPU_T).set_color(RED).scale(.75)

		self.play(Create(CPU_S), Write(CPU_T))
		self.play(CPU.animate.next_to(BB, RIGHT * 2))
		CPU_W = [
			Line(start=CPU.get_left(), end=BB.get_right()).shift(UP / 3),
			Line(start=BB.get_right(), end=CPU.get_left()).shift(DOWN / 3),
		]

		IO_S = Square()
		IO_T = Text('IO').scale(.9)
		IO = VGroup(IO_S, IO_T).set_color(BLUE).scale(.75)

		self.play(Create(IO_S), Write(IO_T))
		self.play(IO.animate.next_to(BB, DOWN * 2))
		IO_W = [
			Line(start=IO.get_top(), end=BB.get_bottom()).shift(LEFT / 3),
			Line(start=BB.get_bottom(), end=IO.get_top()).shift(RIGHT / 3),
		]

		RAM.add(*RAM_W)
		CPU.add(*CPU_W)
		IO.add(*IO_W)

		WIRES = RAM_W + IO_W + CPU_W

		self.play(FadeIn(BB_S), Write(BB_T),
			*[Create(w) for w in WIRES],
			*[w.animate.set_color(YELLOW) for w in WIRES]
		)

		self.next_section('PartsLoop', type=PST.LOOP)

		dotAnims = [
			Dot(point=w.get_start(), color=YELLOW)
				.animate(rate_func=linear).move_to(w.get_end())
					for ws in WIRES for w in ws
		]
		dots = VGroup(*[d.mobject for d in dotAnims])
		
		parts = VGroup(BB, RAM, CPU, IO)
		
		self.play(*[FadeIn(d) for d in dots], play_time=.3)
		self.play(*dotAnims, play_time=.3)
		self.play(*[FadeOut(d) for d in dots], play_time=.3)

		self.next_section('IO', type=PST.NORMAL)

		DRS = 5
		DCS = 24 // 2
		RBS = 16

		LZY = 0
		rdb = VGroup(*[
			Dot(color=YELLOW if i * DCS * 2 + j + DCS < RBS else WHITE)
				.shift(RIGHT * j / 2 + DOWN * i / 2)
					for i in range(DRS)
						for j in range(-DCS, DCS) 
		]).shift(DOWN)
		self.play(ReplacementTransform(parts, rdb) or 1.5)

		bios_text = Text('BIOS', color=YELLOW)
		self.play(Write(bios_text))

		self.next_section('After BIOS explanation', type=PST.NORMAL)

		dds = rdb[:RBS]
		rdb.remove(*dds)
		dds = VGroup(*dds)

		tot = VGroup(*[
			dds[i].copy()
			.move_to(ORIGIN + LEFT * RBS / 4 + i * RIGHT / 2)
				for i in range(RBS)
		])
		self.play(
			Transform(dds, tot),
			Transform(bios_text, tot)
		)
		self.remove(bios_text)
		self.play(FadeOut(rdb))

		TMW = 8
		TMH = 2
		texts = [
			[
				Text(f'{randrange(0, 255):02x}', color=GRAY, fill_opacity=0)
					for j in range(TMW)
			] for i in range(TMH)
		]

		tscale = .65
		tmem = MobjectTable(texts,
			col_labels=[
				Text(f'{i:02x}', color=YELLOW)
					for i in range(TMW)
			],
			row_labels=[
				Text(f'{j * TMW:02x}', color=YELLOW)
					for j in range(TMH)
			]
		)
		tmem.scale(tscale)

		self.play(Transform(
			VGroup(*dds),
			VGroup(*[
				val.copy().set_opacity(1)
					for row in texts for val in row
			])
		))

		self.play(FadeIn(tmem))

		def get_cell_highlighted(col: int, row: int, fill=WHITE) -> BackgroundRectangle:
			return tmem.get_highlighted_cell(
				(col, row), color=fill
			).scale(.75 if tscale == .65 else .6).set_z_index(-1)

		def get_pos(index: int) -> (int, int):
			return (index // TMW + 2,
					index % TMW + 2)
		
		def get_curr_pos() -> (int, int):
			return get_pos(self.pc)

		def get_curr_cell_highlighted() -> BackgroundRectangle:
			return get_cell_highlighted(*get_curr_pos())
		
		def get_curr_cell() -> Polygon:
			return tmem.get_cell(get_curr_pos())

		def movp(by: int):
			self.pco = self.pc
			self.pc += by

		def jmp(by=0):
			if by != 0:
				movp(by)
			oldrow, oldcol = oldpos = get_pos(self.pco)
			newrow, newcol = newpos = get_curr_pos()
			return AnimationGroup(
				Transform(hl, get_curr_cell_highlighted()),

				tmem.get_entries((oldrow, 1))
					.animate.set_color(YELLOW),
				tmem.get_entries((1, oldcol))
					.animate.set_color(YELLOW),

				tmem.get_entries((newrow, 1))
					.animate.set_color(WHITE),
				tmem.get_entries((1, newcol))
					.animate.set_color(WHITE),

				dds[self.pco].animate.set_color(GRAY),
				dds[self.pc].animate.set_color(GRAY_E)
			)
		
		self.pc = 0
		self.pco = 0
		hl = get_cell_highlighted(2, 2, fill=BLACK)
		tmem.add_to_back(hl)
		
		self.play(jmp())

		dfr = dds[2]
		DFRT = '9f'
		self.next_section('Step 1 - Change', PST.NORMAL)
		self.play(
			jmp(1),
			Transform(
				dfr,
				Text(DFRT, color=GRAY)
					.scale(tscale)
					.move_to(dfr)
			)
		)
		
		self.next_section('Step 2 - Check', PST.NORMAL)
		
		self.play(Indicate(dfr, color=BLUE_E))
		self.play(jmp(4))

		self.next_section('Introduce Registers', PST.NORMAL)
		self.play(*[
			o.animate.shift(DOWN * 2)
				for o in self.get_top_level_mobjects()
		])

		REGC = 3

		regvals = {
			chr(c) : [
				[ Text(chr(c), color=RED) ],
				[ Text('00', color=GRAY) ]
			] for c in range(b'A'[0], b'A'[0] + REGC)
		}
		registers = {
			chr(b'A'[0] + i) :
			MobjectTable(regvals[chr(b'A'[0] + i)], include_outer_lines=True)
				.move_to((REGC / 2 * LEFT + (i + .5) * RIGHT) * 3 + UP * 1.5)
					for i in range(REGC)
		}
		self.play(
			animate_from_center(
				[*registers.values()],
				lambda r: r.create(element_animation=Write)
			)
		)

		self.next_section('Step 3 - Store in Register', type=PST.NORMAL)

		regeo = registers['A'].get_entries((1, 2))
		regen = Text(DFRT, color=GRAY).move_to(regeo)
		dfrc = dfr.copy()
		self.play(
			jmp(1),
			Transform(dfrc, regen),
			Transform(regeo, regen)
		)
		self.remove(dfrc)
		regeo.set(text=DFRT)

		self.next_section('Stack', type=PST.NORMAL)

		tcmlp = VGroup(tmem, dds)

		self.play(
			tcmlp.animate
				.scale(tscale := .75)
				.to_edge(edge=DR),
			VGroup(*registers.values())
				.animate
				.next_to(
					tcmlp.copy()
						.scale(.75)
						.to_edge(edge=DR),
					UP
				)
				.to_edge(edge=RIGHT)
		)

		_stack = tcmlp.copy()

		STMW = 1
		STMH = 8
		sexts = [
			Text('00', color=GRAY)
				for i in range(STMH)
		]

		STSCALE = .65
		stack: MobjectTable = MobjectTable(
			[*map(lambda t: [t], sexts)],
			col_labels=[ Text('00', color=YELLOW) ],
			row_labels=[
				Text(f'{0x100 - j:02x}', color=YELLOW)
					for j in range(STMH, 0, -1)
			]
		).scale(STSCALE).to_edge(edge=LEFT)

		self.play(ReplacementTransform(_stack, stack))
		
		def movsp(by: int):
			self.spo = self.sp
			self.sp -= by

		def jmsp(by=0):
			if by != 0:
				movsp(by)

			return AnimationGroup(
				Transform(shigh,
					stack.get_highlighted_cell((self.sp + 2, 2), color=WHITE)
						.scale(.75)
						.set_z_index(-1)
				),

				stack.get_entries((self.spo + 2, 1))
					.animate.set_color(YELLOW),

				stack.get_entries((self.sp + 2, 1))
					.animate.set_color(WHITE),

				sexts[self.spo].animate.set_color(GRAY),
				sexts[self.sp].animate.set_color(GRAY_E)
			)
		
		self.sp = STMH - 1
		self.spo = self.sp
		shigh = stack.get_highlighted_cell((self.sp + 2, 2), color=BLACK)
		shigh.scale(.75).set_z_index(-1)

		self.play(jmsp())

		self.next_section('Stack Demonstation', type=PST.NORMAL)

		call_stack = []
		
		def stack_push(reg:str=None, val:Any=None):
			sto = sexts[self.sp]

			rege = registers[reg].get_entries((2, 1)).copy() if reg else None

			stn = Text(rege.text if reg else str(val), color=GRAY_E)
			stn.scale(STSCALE).move_to(sto)

			if reg:
				self.remove(sto)
				self.play(
					Transform(rege, stn),
					Transform(sto, stn)
				)
				sto.set(text=rege.text)
				self.remove(rege)
			else:
				self.play(Transform(sto, stn))
			
			self.play(jmsp(1))

		def stack_pop(reg: str=None):
			stack_entry = sexts[self.sp + 1]
			new_stack_entry = Text('00', color=GRAY)
			new_stack_entry.move_to(stack_entry).scale(STSCALE)

			if reg:
				regval = registers[reg].get_entries((2, 1))
				new_regval = Text(stack_entry.text, color=GRAY)
				new_regval.move_to(regval)
				self.play(
					Transform(stack_entry, new_stack_entry),
					Transform(stack_entry.copy(), new_regval),
					Transform(regval, new_regval)
				)
			else:
				self.play(Transform(stack_entry, new_stack_entry))
			
			self.play(jmsp(-1))

		def call(index: int):
			call_stack.append(self.pc)
			stack_push(val=f'{self.pc:02x}'),
			self.play(jmp(index - self.pc))

		def ret():
			_adr = call_stack.pop() + 1
			stack_pop()
			self.play(jmp(_adr - self.pc))

		self.next_section('Push eax', type=PST.NORMAL)
		stack_push(reg='A')
		self.next_section('Call function', type=PST.NORMAL)
		call(TMH * TMW - 4)

		adds = registers['A'].get_entries((1, 2))
		tto = Text('b6', color=GRAY).move_to(adds)

		self.next_section('Modify eax in function', type=PST.NORMAL)
		self.play(jmp(1), Transform(adds, tto))
		adds.set(text='b6')
		self.remove(tto)
		
		self.next_section('Return from func', type=PST.NORMAL)
		self.play(jmp(1))
		ret()

		self.next_section('Pop eax', type=PST.NORMAL)
		stack_pop('A')

		self.next_section('Word sizes', type=PST.NORMAL)
		self.play(*map(FadeOut, self.get_top_level_mobjects()))

		POW = 5
		LC = 2 ** POW
		lines = VGroup(*[
			Line(color=YELLOW if i < 8 else GRAY)
				.rotate(PI / 2)
				.scale(2.5)
				.shift((LC * LEFT / 2 + i * RIGHT) / (POW - 2) + DOWN)
					for i in range(LC)
		])
		word_size = Text('8', color=RED).shift(UP * 3)
		self.play(
			Write(word_size),
			animate_from_center(lines, Create)
		)
		
		self.next_section('Increase Word size', type=PST.NORMAL)

		for p in range(3, POW + 1):
			self.play(
				*[
					l.animate.set_color(YELLOW)
						for l in lines[:2 ** p]
				],
				Transform(
					word_size,
					Text(str(2 ** p), color=RED).move_to(word_size)
				)
			)
			self.wait(1)

		self.next_section('Outro', type=PST.SKIP)
		sus = SVGMobject('amogus_oversimplified.svg', color=RED, fill_color=BLACK)
		self.play(
			ReplacementTransform(lines, sus),
			FadeOut(word_size)
		)
		
		self.next_section('Amogus buffer', PST.COMPLETE_LOOP)

		self.play(Rotating(sus, run_time=3, rate_func=rate_functions.ease_in_out_sine))
		self.wait(.3)

		self.next_section('End', PST.NORMAL)

		self.play(FadeOut(sus))

