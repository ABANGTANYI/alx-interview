#!/usr/bin/python3
import sys
import re

def output(log):
    print(f"File size: {log['file_size']}")
    for code in sorted(log['code_frequency']):
        if log['code_frequency'][code]:
            print(f"{code}: {log['code_frequency'][code]}")

def parse_log_line(line, log):
    pattern = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')
    match = pattern.match(line)
    if match:
        code = match.group(3)
        file_size = int(match.group(4))

        log['file_size'] += file_size

        if code.isdigit() and int(code) in [200, 301, 400, 401, 403, 404, 405, 500]:
            log['code_frequency'][code] += 1

def main():
    log = {
        'file_size': 0,
        'code_frequency': {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parse_log_line(line, log)
            line_count += 1

            if line_count % 10 == 0:
                output(log)
    except KeyboardInterrupt:
        output(log)

if __name__ == "__main__":
    main()
