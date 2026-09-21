LOG_FILE = "auth.log"
FAILED_THRESHOLD = 2

def parse_log(file_path):
    failed_attempts = {}
    with open(file_path, "r") as file:
        lines = file.readlines()
    for line in lines:
        if "Failed" in line:
            ip = line.strip().split("from ")[-1]
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1
    return failed_attempts

def print_report(failed_attempts):
    print("\n📊 گزارش تلاش‌های ناموفق:")
    for ip, count in failed_attempts.items():
        if count >= FAILED_THRESHOLD:
            print(f"🚨 IP مشکوک: {ip} — {count} بار تلاش ناموفق")
        else:
            print(f"ℹ️ {ip} — {count} بار تلاش ناموفق")

if name == "main":
    attempts = parse_log(LOG_FILE)
    print_report(attempts)
