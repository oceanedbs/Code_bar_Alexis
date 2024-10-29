import pandas as pd

queue_data = pd.read_csv('/home/dubois/Documents/Autre/Code_bar_Alexis/3_crous/queue.txt', header=None, sep=' ')
queue_data.columns = ["Time", "Arrivals"]
queue_data = queue_data["Arrivals"].tolist()

menu_items = pd.read_csv('/home/dubois/Documents/Autre/Code_bar_Alexis/3_crous/nourriture.csv', header=None, sep=',')
print(menu_items)   
menu_items.columns = ["Plat", "Type", "Bonheur", "Tps_min", "Tps_max"]
menu_items = menu_items.values.tolist()
print(menu_items)

service_rate = 10  # People served per minute

# Step 1: Calculate queue length over time
queue_lengths, current_queue = [], 0
for arrivals in queue_data:
    current_queue += arrivals
    if current_queue <= service_rate:
        queue_lengths.append(0)
        current_queue = 0
    else:
        queue_lengths.append(current_queue - service_rate)
        current_queue -= service_rate

# Step 2: Calculate wait times and find optimal arrival minute
wait_times = [max(0, (q_len - 1) // 10) for q_len in queue_lengths]
optimal_arrival_minute = wait_times.index(min(wait_times))
optimal_wait_time = wait_times[optimal_arrival_minute]

# Step 3: Select highest happiness meal items available at optimal arrival time
available_items = {"Entree": [], "Plat": [], "Dessert": []}
for name, category, happiness, start, end in menu_items:
    if start <= optimal_arrival_minute <= end:
        available_items[category].append((name, happiness))

selected_meal, total_happiness = {}, 0
for category, items in available_items.items():
    if items:
        best_item = max(items, key=lambda x: x[1])
        selected_meal[category] = best_item[0]
        total_happiness += best_item[1]

# Output results
arrival_time = "11:30"  # 0 minutes from start time
print(f"Optimal arrival time: {arrival_time}")
print(f"Wait time in queue: {optimal_wait_time} minutes")
print(f"Selected meal: {selected_meal}")
print(f"Total happiness: {total_happiness - optimal_wait_time * 2} points")
