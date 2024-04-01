import sys

def format_time(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    return f"{hours} Hours, {minutes} Minutes"

def analyze_cat_shelter(filename):
    cat_visits = 0
    intruding_cats = 0
    total_time = 0
    longest_visit = 0
    shortest_visit = float('inf')
    with open(filename, 'r') as file:
        for line in file:
            if line.strip() == "END":
                break
            parts = line.strip().split(',')
            if len(parts) != 3:
                print(f"Issue parsing line: {line}")
                continue
            activity = parts[0]
            start_time = int(parts[1])
            end_time = int(parts[2])
            duration = end_time - start_time
            if activity == "OURS":
                cat_visits += 1
                total_time += duration
                if duration > longest_visit:
                    longest_visit = duration
                if duration < shortest_visit:
                    shortest_visit = duration
            elif activity == "THEIRS":
                intruding_cats += 1
            else:
                print(f"Warning: Unknown activity '{activity}' detected.")

    average_visit_length = total_time / cat_visits if cat_visits > 0 else 0
    print("Log File Analysis")
    print("==================")
    print(f"Cat Visits: {cat_visits}")
    print(f"Other Cats: {intruding_cats}")
    print(f"Total Time in House: {format_time(total_time)}")
    print(f"Average Visit Length: {format_time(average_visit_length)}")
    print(f"Longest Visit: {format_time(longest_visit)}")
    print(f"Shortest Visit: {format_time(shortest_visit)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing command line argument!")
        print("Usage: python cat_shelter.py <filename>")
    else:
        filename = sys.argv[1]
        try:
            analyze_cat_shelter(filename)
        except FileNotFoundError:
            print(f'Cannot open "{filename}"!')



