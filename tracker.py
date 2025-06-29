moods = []
FILENAME = "mood_log.txt"

def add_mood():
    mood_category = input("How are you feeling today?").strip().capitalize()
    mood_description = input("Why?").strip().capitalize()
    mood_count = input("Rate your productivity (1-10):").strip().capitalize()

    if not mood_category:
        print("Mood can't be empty")
        return
    if not mood_count.isdigit():
        print("Count should be a number")
        return
    entry = f"{mood_category} - {mood_description} - {mood_count}"
    moods.append(entry)

    with open(FILENAME, "a") as file:
        file.write(entry + "\n")

    print("mood added")

def view_mood():
    if not moods:
        print("No moods recorded yet")
    else:
        print("Moods tracked today!")
        for item in moods:
            print("*", item)

def show_productivity():
    
    scores  = []

    for entry in moods:
        parts = entry.split("-")

        if len(parts) !=3:
            continue

        raw_score = parts[2].strip()

        try: 
            score = float(raw_score)
            scores.append(score)
        except ValueError:
            print(f"Skipping invalid score: {raw_score}")
            continue

    if scores:
        total = sum(scores)
        avg = total/len(scores)

        print(f"\n Total Productivity Score: {total:.2f}")
        print(f"\n Average Productivity Score: {avg:.2f}")
    else:
        print("No valid productivity score found.") 
        
def load_moods():
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                moods.append(line.strip())
    except FileNotFoundError:
        print("No previous mood log found.")

def main_menu():
    load_moods()
    print("Welcome to mood tracker")
    
    while True:
        command = input("What would you like to do? (add/view/summary/exit)").strip().lower()

        if command == "add":
            add_mood()
        elif command == "view":
            view_mood()

        elif command == "summary":
            show_productivity()

        elif command == "exit":
            print("Goodbye!")
            return
        else:
            print("Invalid option")

main_menu()