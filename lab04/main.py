import sys
from stats import average_by_city, read_valid, warmest_city, parse_record

def main():
    lines = sys.stdin.read().splitlines()
    total_parsed_lines = 0
    skipped_errors_count = 0
    for line in lines:
        cleaned = line.strip()
        if not cleaned:
            continue
        try:
            parse_record(cleaned)
            total_parsed_lines += 1
        except ValueError:
            skipped_errors_count += 1
    valid_records = read_valid(lines)
    best_city = warmest_city(valid_records)
    if best_city:
        averages = average_by_city(valid_records)
        warmest_temp = averages[best_city]
    else:
        warmest_temp = 0.0
    print(total_parsed_lines)
    print(skipped_errors_count)
    print(f"{warmest_temp:.1f}")

if __name__ == "__main__":
    main()