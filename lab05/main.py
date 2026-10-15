from logstats import count_levels, top_errors, format_report

path = input()
with open(path, encoding="utf-8") as log:
    counts = count_levels(log)
    log.seek(0)
    errors = top_errors(log, n=3)

broken_count = counts.get("BROKEN", 0)
error_count = counts.get("ERROR", 0)


total_parsed = counts.get("DEBUG", 0) +counts.get("INFO", 0) +counts.get("WARNING", 0) +counts.get("ERROR", 0)
print(total_parsed)
print(error_count)
print(broken_count)

report = format_report(counts, errors)
with open("report.txt", mode="w", encoding="utf-8") as out_file:
    out_file.write(report)