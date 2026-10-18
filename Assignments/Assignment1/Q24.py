wall_length=20*100
wall_heigth=2*100
wall_thickness=0.75*100

brick_length=25
brick_width=10
brick_thickness=7.5

wall_volume=wall_length*wall_heigth*wall_thickness
brick_volume=brick_length*brick_width*brick_thickness

number_of_bricks=wall_volume/brick_volume

total_cost=((number_of_bricks)/1000)*900

print(f"total cost : {total_cost}")