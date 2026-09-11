lower_base=128
upper_base=92
heigth=40
width=4
initail_area=0.5*((lower_base+upper_base)*heigth)

walkaway_area=heigth*width

reamaning_area=initail_area-walkaway_area

print(f"reamaning area: {reamaning_area}")