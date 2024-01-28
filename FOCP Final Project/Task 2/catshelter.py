import sys

def process_line(line):
    parts = line.split(",")
    if len(parts) == 3:
        try:
            cat_type, entry_time, exit_time = parts
            return cat_type, int(entry_time), int(exit_time)
        except ValueError:
            return None

def analyze_cat_shelter_log(log_file):
    try:
        with open(log_file, "r") as file:
            cat_visits = 0
            other_cats = 0  
            total_time = 0
            durations = []

            for line in file:
                if line.strip() == "END":
                    break

                data = process_line(line.strip())
                if data:
                    cat_type, entry, exit = data
                    if cat_type == "OURS":
                       # Count the visits by the correct cat
                        cat_visits += 1
                        total_time += exit - entry
                       # Track the duration for OURS cat
                        durations.append(exit - entry)
                    elif cat_type == 'THEIRS':
                        other_cats += 1  # Increment other_cats for THEIRS cat

            hours, minutes = divmod(total_time, 60)
            average_duration = sum(durations) // len(durations) if durations else 0
            longest_visit = max(durations) if durations else 0
            shortest_visit = min(durations) if durations else 0

            # Format and print the results
            print(f"$ ./cat_shelter.py {log_file}")
            print("\n Log File Analysis")
            print("==================")
            print(f"\nCat Visits: {cat_visits}")
            print(f"Other Cat Visits: {other_cats}")  # Include count of other cat visits
            print(f"\nTotal Time in Shelter: {hours} Hours, {minutes} Minutes")
            print(f"\nAverage Visit Length: {average_duration} Minutes")
            print(f"Longest Visit: {longest_visit} Minutes")
            print(f"Shortest Visit: {shortest_visit} Minutes")

    except FileNotFoundError:
        print(f'Cannot open "{log_file}"!')
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing command line argument!")
    else:
        analyze_cat_shelter_log(sys.argv[1])
