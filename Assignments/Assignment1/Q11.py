base_ratio=8
heigth_ratio=5

area=320

x_sqaure=area/(0.5*base_ratio*heigth_ratio)
x=x_sqaure**0.5

base=base_ratio*x
heigth=heigth_ratio*x

print(f"base is: {base}")
print(f"heigth is: {heigth}")

