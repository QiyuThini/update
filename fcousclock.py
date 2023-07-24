import time

def main():
    while True:
        current_time = time.strftime("%H:%M:%S")
        print(f"{current_time} {' '*6} [专注时钟]")
        time.sleep(1)  # 停顿1秒

if __name__ == "__main__":
    main()
