output = ""

for i in range(int(input("Enter the number you want factorialleded\n")), 1, -1):
    output += f"{i}\\times"
output += "1"

print(f"\n{output}\n")