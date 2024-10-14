len1 = 366
len2 = 32

with open("out.txt", "w") as f:
    for i in range(len1 + len2 - 1):
        f.write(f"{max(0, i - len2 + 1)} : {min(len1, i + 1)}\n")
        for j in range(max(0, i - len2 + 1), min(len1, i + 1)):
            f.write(f"   {j} {i - j}\n")
