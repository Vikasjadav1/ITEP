# # for i in range(1,4):
# #     for j in range(1,4):
# #         print(i, j)


# # for i in range(5):
# #     for j in range(5):
# #         print("*", end=" ")
# #     print("")

# # for i in range(5):
# #     print("* "*5)


# # for i in range(5):
# #     for j in range(5,i,-1):
# #         print("*", end=" ")
# #     print("")


# for i in range(5,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print("")


# # for i in range(5):
# #     for j in range(i+1):
# #         print("*", end=" ")
# #     print("")


# # for i in range(5):
# #     for j in range(5):
# #         if j>=5-i:
# #             print(" ", end=" ")
# #         else:
# #             print("*", end=" ")
# #     print("")

# for i in range(1,6):
#     for k in range(5-i):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     print("")


# for i in range(1, 6 , 1):
#     for j in range(1,6, 1): 
#         if j<6-i:
#             print(" ", end=" ")
#         else:
#             print("*", end=" ")
#     print("")


# for i in range(1,10):
#     for j in range(1,10):
#         if i==5 or j==5:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()




for i in range(1,10):
    for j in range(1,10):
        if i==5 or j==5 or (i==1 and j>5) or (j==1 and i>5) or (i==9 and j>5) or (j==9 and i<5):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()