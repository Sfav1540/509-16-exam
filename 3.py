width = float(input())
length = float(input())
depth = float(input())

volume = width * length * depth

time_in_seconds = volume * 15

time_in_minutes = time_in_seconds / 60

print(f"ต้องใช้เวลาในการเติมน้ำ {time_in_minutes:.2f} นาที.")
