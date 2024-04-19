from datetime import date

def main():
  habits = []

  while True:
    print("Habit Tracker")
    print("1. Add Habit")
    print("2. Mark Habit Complete")
    print("3. View Habits")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      name = input("Enter habit name: ")
      description = input("Enter description (optional): ")
      reminder_frequency = input("Enter reminder frequency (e.g., daily, weekly): ").lower()  # Convert to lowercase
      habits.append(Habit(name, description, reminder_frequency))

    elif choice == '2':
      if not habits:
        print("No habits added yet!")
        continue
      for i, habit in enumerate(habits):
        print(f"{i+1}. {habit.name}")
      habit_index = int(input("Enter habit number to mark complete: ")) - 1
      habits[habit_index].mark_completed(date.today())
      print(f"{habits[habit_index].name} marked complete!")

    elif choice == '3':
      if not habits:
        print("No habits added yet!")
        continue
      for i, habit in enumerate(habits):
        print(f"{i+1}. {habit.name} ({habit.get_completion_streak()} day streak)")

    elif choice == '4':
      print("Exiting...")
      break

    else:
      print("Invalid choice!")

if __name__ == "__main__":
  main()
