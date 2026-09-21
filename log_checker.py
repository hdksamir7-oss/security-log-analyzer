failed_attempts = {}

with open("auth.log", "r") as file:
    lines = file.readlines()

for line in lines:
    if "Failed" in line:
        ip = line.strip().split("from ")[-1]

        if ip in failed_attempts:
            failed_attempts[ip] += 1
        else:
            failed_attempts[ip] = 1

print("\n📊 گزارش تلاش‌های ناموفق:")
for ip, count in failed_attempts.items():
    if count >= 2:
        print(f"🚨 IP مشکوک: {ip} — {count} بار تلاش ناموفق")
    else:
        print(f"ℹ️ {ip} — {count} بار تلاش ناموفق")