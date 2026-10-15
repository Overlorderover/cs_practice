from logstats import count_levels, top_errors, format_report

with open("events.log", encoding="utf-8") as log:
    counts = count_levels(log)
    log.seek(0)
    errors = top_errors(log, n=3)

broken_count = counts["BROKEN"]
error_count = counts["ERROR"]
total_parsed = counts["DEBUG"] + counts["INFO"] + counts["WARNING"] + counts["ERROR"]

report = format_report(counts, errors)
with open("report.txt", mode="w", encoding="utf-8") as out_file:
    out_file.write(report)