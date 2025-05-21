print("nhap van ban (bam 'x' de ket thuc): ")
lines = []
while True:
    line = input()
    if line.lower() == 'x':
        break
    lines.append(line)

print("\nCac dong da chuyen thanh in hoa: ")
for line in lines:
    print(line.upper())

