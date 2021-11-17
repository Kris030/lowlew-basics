from manim import VMobject, Animation, AnimationGroup
from typing import Callable, Iterable

def animate_from_center(objs: Iterable[VMobject], animation: Callable[VMobject, Animation], lag_ratio: float = .1) -> AnimationGroup:
	LC = len(objs)
	return \
		AnimationGroup(
			AnimationGroup(
				*[
					animation(o)
						for o in objs[LC // 2 - 1::-1]
				],
				lag_ratio=lag_ratio
			),
			AnimationGroup(
				*[
					animation(o)
						for o in objs[LC // 2:LC]
				],
				lag_ratio=lag_ratio
			)
		) if LC % 2 == 0 else \
		AnimationGroup(
			animation(objs[LC // 2]),
			AnimationGroup(
				AnimationGroup(
					*[
						animation(o)
							for o in objs[LC // 2 - 1::-1]
					],
					lag_ratio=lag_ratio
				),
				AnimationGroup(
					*[
						animation(o)
							for o in objs[LC // 2 + 1:LC]
					],
					lag_ratio=lag_ratio
				)
			),
			lag_ratio=lag_ratio
		)

class FuncAfterAnimation(Animation):
	def __init__(self, func: Callable=None, **kwargs):
		super().__init__(None, **kwargs)
		self.finish = func
	def begin(self) -> None:
			pass
	def clean_up_from_scene(self, scene: "Scene") -> None:
			pass
	def update_mobjects(self, dt: float) -> None:
			pass
	def interpolate(self, alpha: float) -> None:
			pass
