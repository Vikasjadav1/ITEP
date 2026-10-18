price=int(input("enter price"))

if price<50000:
    road_tax=price*0.05
    print(f"road tax : {road_tax}")
elif price>50000 and price<=100000:
    road_tax=price*0.10
    print(f"road tax : {road_tax}")
else:
    road_tax=price*0.10
    print(f"road tax : {road_tax}")
