sleep_hours = []
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for i in range(7):
    sleep_input = int(input(f"Enter No of Hours You slept for {week_days[i]} - :"))
    sleep_hours.append(sleep_input)

print(f"Average hours slept - {sum(sleep_hours) // len(sleep_hours)}")