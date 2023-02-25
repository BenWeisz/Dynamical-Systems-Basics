import pysketcher as ps
from pysketcher.backend.matplotlib import MatplotlibBackend

ceiling = ps.Wall(
    [ps.Point(1, 3.75), ps.Point(5, 3.75)],
    0.1,
)

spring1 = ps.Spring(ps.Point(3, 3), 0.75, 0.2, 0.1, 10)
mass1 = ps.Rectangle(ps.Point(2.8, 2.6), 0.4, 0.4)
mass1.style.fill_color = ps.Style.Color.ORANGE
mass1_text = ps.Text("m1", ps.Point(3, 2.75))

line1_top = ps.Line(ps.Point(3.45, 3.4), ps.Point(3.55, 3.4))
line1_center = ps.Line(ps.Point(3.5, 3.4), ps.Point(3.5, 2.8))
line1_bottom = ps.Line(ps.Point(3.45, 2.8), ps.Point(3.55, 2.8))

zero_text1 = ps.Text("0", ps.Point(3.65, 3.38))
position_text1 = ps.Text("x1(t)", ps.Point(3.67, 2.78))

spring2 = ps.Spring(ps.Point(3, 1.85), 0.75, 0.2, 0.1, 10)
mass2 = ps.Rectangle(ps.Point(2.8, 1.45), 0.4, 0.4)
mass2.style.fill_color = ps.Style.Color.ORANGE
mass2_text = ps.Text("m2", ps.Point(3, 1.6))

line2_top = ps.Line(ps.Point(3.45, 2.25), ps.Point(3.55, 2.25))
line2_center = ps.Line(ps.Point(3.5, 2.25), ps.Point(3.5, 1.65))
line2_bottom = ps.Line(ps.Point(3.45, 1.65), ps.Point(3.55, 1.65))

zero_text2 = ps.Text("0", ps.Point(3.65, 2.23))
position_text2 = ps.Text("x2(t)", ps.Point(3.67, 1.63))

fig = ps.Figure(0, 6, 0, 4, backend=MatplotlibBackend)
fig.add(ceiling)
fig.add(spring1)
fig.add(mass1)
fig.add(mass1_text)

fig.add(line1_top)
fig.add(line1_center)
fig.add(line1_bottom)
fig.add(zero_text1)
fig.add(position_text1)

fig.add(spring2)
fig.add(mass2)
fig.add(mass2_text)

fig.add(line2_top)
fig.add(line2_center)
fig.add(line2_bottom)
fig.add(zero_text2)
fig.add(position_text2)

fig.save("double-mass-spring.png")