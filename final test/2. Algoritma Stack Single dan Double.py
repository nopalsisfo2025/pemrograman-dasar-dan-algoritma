
size = 10
stack = [None] * size
top1 = -1
top2 = size

# Push ke stack 1
top1 += 1
stack[top1] = 100

# Push ke stack 2
top2 -= 1
stack[top2] = 200

print("Double Stack:", stack)
