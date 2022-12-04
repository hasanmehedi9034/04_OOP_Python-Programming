data={1:[2,3,4,5],2:[1,3,4,5],3:[1,2,4,5],4:[1,2,3,5],5:[1,2,3,4]}

ans = {k:[j for j in range(1, 6) if k is not j] for k in range(1, 6)}

print(ans)
print(data)

# print(data == ans)
# for i in range(1, 6):
#     print([j for j in range(1, 6) if i is not j])

# for i in range(1, 6):
#     print([i for i in range(5)])

