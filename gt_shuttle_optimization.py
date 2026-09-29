import random
import pandas as pd
import matplotlib.pyplot as plt

# Simulation settings
SIMULATION_TIME = 180  # minutes
STUDENTS_PER_MIN = 2   # average arrivals per minute

# Test different shuttle frequencies (minutes)
frequencies = [5, 10, 15, 20]

results = []

for frequency in frequencies:
    waiting_students = []
    total_wait_time = 0
    students_served = 0
    max_queue = 0

    for minute in range(SIMULATION_TIME):

        # Simulate student arrivals
        arrivals = random.randint(0, STUDENTS_PER_MIN * 2)

        for _ in range(arrivals):
            waiting_students.append(minute)

        # Shuttle arrives
        if minute % frequency == 0:
            shuttle_capacity = 30

            boarded = min(len(waiting_students), shuttle_capacity)

            for _ in range(boarded):
                arrival_time = waiting_students.pop(0)
                total_wait_time += minute - arrival_time
                students_served += 1

        max_queue = max(max_queue, len(waiting_students))

    avg_wait = (
        total_wait_time / students_served
        if students_served > 0
        else 0
    )

    results.append(
        {
            "Shuttle Frequency (min)": frequency,
            "Average Wait Time": round(avg_wait, 2),
            "Max Queue Length": max_queue,
            "Students Served": students_served,
        }
    )

# Results table
df = pd.DataFrame(results)

print("\nGeorgia Tech Shuttle Optimization Results\n")
print(df)

# Visualization
plt.figure(figsize=(8, 5))
plt.plot(
    df["Shuttle Frequency (min)"],
    df["Average Wait Time"],
    marker="o",
)
plt.title("Impact of Shuttle Frequency on Student Wait Time")
plt.xlabel("Shuttle Frequency (Minutes)")
plt.ylabel("Average Wait Time (Minutes)")
plt.grid(True)
plt.tight_layout()

plt.savefig("shuttle_wait_times.png")
plt.show()
