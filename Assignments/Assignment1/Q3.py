tiles_length=13
tiles_breadth=7

rectangle_length=520
rectangle_breadth=140

Tile_area=tiles_length*tiles_breadth
rectangle_area=rectangle_length*rectangle_breadth

tiles_needed=rectangle_area/Tile_area

print(f"tiles needed to cover the rectangular region : {tiles_needed}")
