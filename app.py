import os
import platform
import shutil


def check_system_health():
    print(f"=== System Health Monitor ===")
    print(f"OS Platform: {platform.system()} {platform.release()}")

    # Check Disk Space
    total, used, free = shutil.disk_usage("/")
    free_gb = free // (2**30)
    print(f"Available Disk Space: {free_gb} GB")

    # Check system load (different behavior on Windows vs Linux)
    if platform.system() != "Windows":
        load1, load5, load15 = os.getloadavg()
        print(f"System Load (1 min average): {load1}")
    else:
        print("System Load: Active (Windows OS)")

    print("=============================")
    return True


if __name__ == "__main__":
    check_system_health()