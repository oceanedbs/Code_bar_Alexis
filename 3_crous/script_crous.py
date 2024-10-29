import matplotlib.pyplot as plt
import pandas as pd



# Open the queue.txt and nourriture.txt files
queue_data = pd.read_csv('/home/dubois/Documents/Autre/Code_bar_Alexis/3_crous/queue.txt', sep=' ', header=None)
queue_data.columns = ["Time", "Arrivals"]

nourriture_data = pd.read_csv('/home/dubois/Documents/Autre/Code_bar_Alexis/3_crous/nourriture.txt', sep=' ', header=None)
nourriture_data.columns = ["Plat", "Type", "Bonheur", "Tps_min", "Tps_max"]
# Process each line in the queue_data
queue = 0
queue_evolution = []
hapiness_evolution = []
meal_evolution = []
waiting_time = 0
for i, q in queue_data.iterrows():
    # Perform your desired operations on each line
    queue += int(q['Arrivals'])
    queue -= 10
    if queue < 0 :
        queue = 0
    print(queue)
    queue_evolution.append(queue)   
    waiting_time = queue // 10 
    if queue % 10 != 0:
        waiting_time += 1
    print(waiting_time)
    hapiness_level = 0
    optimal_meal = []
    for m in ["Entree", "Plat", "Dessert"]:
        p = nourriture_data[(nourriture_data["Type"] == m) & (i+waiting_time >= nourriture_data["Tps_min"]) & (i+waiting_time <= nourriture_data["Tps_max"])] 
        p = p[p["Bonheur"] == p["Bonheur"].max()]
        print(p)
        if not p.empty:
            hapiness_level += p["Bonheur"].values[0]        
            optimal_meal.append(p["Plat"].values[0])
        print("hapiness_level")
        print(hapiness_level)
        hapiness_level -= waiting_time*2
    hapiness_evolution.append(hapiness_level)
    meal_evolution.append(optimal_meal)
plt.plot(hapiness_evolution, label="hapiness")    
plt.plot(queue_evolution, label="queue")
plt.legend
plt.show()

print("hapiness level")
print(max(hapiness_evolution))

print("time")
print(hapiness_evolution.index(max(hapiness_evolution)))

print(meal_evolution[hapiness_evolution.index(max(hapiness_evolution))])