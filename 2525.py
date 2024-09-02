hour, minute = map(int, input().split())
cookTime = int(input())

cookTimeHour = int(cookTime / 60)
cookTimeMinute = cookTime % 60

endTimeHour = cookTimeHour + hour
endTimeMinute = cookTimeMinute + minute

if endTimeMinute >= 60:
    endTimeMinute -= 60
    endTimeHour += 1

if endTimeHour >= 24:
    endTimeHour -= 24

print(f"{endTimeHour} {endTimeMinute}")