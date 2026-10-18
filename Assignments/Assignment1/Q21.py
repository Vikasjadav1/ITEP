length=15
breadth=8
heigth=5

brick_volume=length*breadth*heigth

wall_length=15*100
wall_breadth=10*100
wall_heigth=8*100

wall_volume=wall_length*wall_breadth*wall_heigth

bricks=wall_volume/brick_volume

print(f"number of bricks : {bricks}")