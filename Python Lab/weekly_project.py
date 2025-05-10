#Inintial checklist task

tasks = ["Workout", "Cooking", "Study", "Attend Team Meeting"]

# Completed checklist tasks
completed=["Workout","Cooking","Attend Team Meeting"]
completed_tasks=[task for task in tasks if task in completed]
incompleted_tasks=[task for task in tasks if task not in completed]
print("Completed Tasks: ")
for task in completed_tasks:
    print(f"- {task}")

print("\nIncomplete Tasks:")
for task in incompleted_tasks:
    print(f"- {task}")