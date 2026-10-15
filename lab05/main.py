from logstats import count_levels, top_errors, format_report

path = input()
with open(path, encoding="utf-8") as log:
    counts = count_levels(log)
    log.seek(0)
    errors = top_errors(log, n=3)

broken_count = counts["BROKEN"]
error_count = counts["ERROR"]
total_parsed = counts["DEBUG"] + counts["INFO"] + counts["WARNING"] + counts["ERROR"] +counts["BROKEN"]

print(total_parsed)
print(error_count)
print(broken_count)

report = format_report(counts, errors)
with open("report.txt", mode="w", encoding="utf-8") as out_file:
    out_file.write(report)