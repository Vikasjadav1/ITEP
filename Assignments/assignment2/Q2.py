quantity=int(input("enter quantity"))

if quantity>1000:
    cost=100*quantity
    discount=cost*0.10
    actual_cost=cost-discount
    print(f"total_cost {actual_cost}")
else:
    cost=100*quantity
    print(f"total_cost {cost}")