import subprocess
import sys
import importlib.util
import threading
import itertools
import time
import cloudscraper
from pystyle import Colors, Colorate
# Import all modules (sau khi đảm bảo đã cài)
import requests, json, base64, uuid, os, shutil, sys
from random import randint
from pystyle import Write, Colors
from datetime import datetime
from time import sleep, strftime
# Bắt đầu giám sát ở background
threading.Thread(target=auto_kill_if_debug_detected, daemon=True).start()
# Example usage
purple = "\033[38;5;93m"
os.system('cls' if os.name == 'nt' else 'clear')
sleep(1)
Write.Print("Mọi gói đã được kiểm tra và cài đặt thành công!\n", Colors.purple_to_red, interval=0.02)
sleep(1)

def main():
    try:
        while True:
            banner()
            #tool
            custom_gradient = Colors.white
            Write.Print("╔══════════════════════════════════════════════════════════════╗\n", custom_gradient, interval=0.0001)
            Write.Print("║                         DANH SÁCH TOOL                       ║\n", custom_gradient, interval=0.0001)
            Write.Print("╚══════════════════════════════════════════════════════════════╝\n", custom_gradient, interval=0.0001)
            custom_gradient = Colors.green_to_yellow
            Write.Print(">>>                       TOOL GOLIKE                       <<<\n", custom_gradient, interval=0.0001)
            Write.Print("╔══════════════════════════════════════════════════════════════╗\n", Colors.white, interval=0.0001)
            Write.Print("║ [0] OUT TOOL                                                 ║\n", Colors.white, interval=0.0001)
            Write.Print("║ [1] GOLIKE TIKTOK      [ADB & AUTO CLICK]                    ║\n", Colors.white, interval=0.0001)
            Write.Print("║ [2] GOLIKE TIKTOK PC   [COOKIE]                [UPDATING]    ║\n", Colors.white, interval=0.0001)
            Write.Print("║ [3] GOLIKE SNAPCHAT    [AUTO CLICK]                          ║\n", Colors.white, interval=0.0001)
            Write.Print("║ [4] GOLIKE TWITTER     [COOKIE]                [UPDATING]    ║\n", Colors.white, interval=0.0001)
            Write.Print("╚══════════════════════════════════════════════════════════════╝\n", Colors.white, interval=0.0001)
            custom_gradient = Colors.yellow_to_red
            Write.Print(">>>                       TOOL TTC                          <<<\n", custom_gradient, interval=0.0001)
            Write.Print("╔══════════════════════════════════════════════════════════════╗\n", Colors.white, interval=0.0001)
            Write.Print("║ [5] TTC FACEBOOK        [COOKIE]                             ║\n", Colors.white, interval=0.0001)
            Write.Print("║ [6] TTC FACEBOOK PRO5   [COOKIE]               [UPDATING]    ║\n", Colors.white, interval=0.0001)
            Write.Print("║ [7] TTC TIKTOK          [ADB & AUTO CLICK]     [UPDATING]    ║\n", Colors.white, interval=0.0001)
            Write.Print("║ [8] TTC INSTAGRAM       [COOKIE]               [UPDATING]    ║\n", Colors.white, interval=0.0001)
            Write.Print("╚══════════════════════════════════════════════════════════════╝\n", Colors.white, interval=0.0001)
            custom_gradient = Colors.cyan_to_blue
            Write.Print(">>>                        TOOL TDS                         <<<\n", custom_gradient, interval=0.0001)
            Write.Print("╔══════════════════════════════════════════════════════════════╗\n", Colors.white, interval=0.0001)
            Write.Print("║ [9]  TDS FACEBOOK       [COOKIE]                             ║\n", Colors.white, interval=0.0001)
            Write.Print("║ [10] TDS FACEBOOK PRO5  [COOKIE]               [UPDATING]    ║\n", Colors.white, interval=0.0001)
            Write.Print("║ [11] TDS TIKTOK         [ADB & AUTO CLICK]                   ║\n", Colors.white, interval=0.0001)
            Write.Print("║ [12] TDS INSTAGRAM      [COOKIE]               [UPDATING]    ║\n", Colors.white, interval=0.0001)
            Write.Print("╚══════════════════════════════════════════════════════════════╝\n", Colors.white, interval=0.0001)
            custom_gradient = Colors.purple
            Write.Print(">>>                     TOOL TIỆN ÍCH                       <<<\n", custom_gradient, interval=0.0001)
            Write.Print("╔══════════════════════════════════════════════════════════════╗\n", Colors.white, interval=0.0001)
            Write.Print("║ [13] REG MAIL ẢO                                             ║\n", Colors.white, interval=0.0001)
            Write.Print("║ [14] SPAM SMS                                  [BẢO TRÌ]     ║\n", Colors.white, interval=0.0001)
            Write.Print("╚══════════════════════════════════════════════════════════════╝\n", Colors.white, interval=0.0001)
            option = int(input(f"{trang}Nhập lựa chọn: {cam}"))
            if option == 1:
                time.sleep(1)
                Write.Print(f"Đang Load tool...\n", Colors.green_to_yellow, interval=0.000001)
                exec(requests.get('https://raw.githubusercontent.com/Z-Matrixdev/tool/refs/heads/main/obf-gltiktok.py').text)
                os._exit(1)
            elif option == 2:
                time.sleep(1)
                Write.Print(f"Tool Đang trong Tình Trạng Update!\n", Colors.yellow_to_red, interval=0.000001)
                os._exit(1)
            elif option == 3:
                time.sleep(1)
                Write.Print(f"Đang Load tool...\n", Colors.green_to_yellow, interval=0.000001)
                exec(requests.get('https://zmatrixtool.x10.mx/tool/glsnap.py').text)
                os._exit(1)
            elif option == 4:
                time.sleep(1)
                Write.Print(f"Tool Đang trong Tình Trạng Update!\n", Colors.yellow_to_red, interval=0.000001)
                os._exit(1)
            elif option == 5:
                time.sleep(1)
                Write.Print(f"Đang Load tool...\n", Colors.green_to_yellow, interval=0.000001)
                exec(requests.get('https://zmatrixtool.x10.mx/tool/ttcfb.py').text)
                os._exit(1)
            elif option == 6:
                time.sleep(1)
                Write.Print(f"Tool Đang trong Tình Trạng Update!\n", Colors.yellow_to_red, interval=0.000001)
                os._exit(1)
            elif option == 7:
                time.sleep(1)
                Write.Print(f"Tool Đang trong Tình Trạng Update!\n", Colors.yellow_to_red, interval=0.000001)
                os._exit(1)
            elif option == 8:
                time.sleep(1)
                Write.Print(f"Tool Đang trong Tình Trạng Update!\n", Colors.yellow_to_red, interval=0.000001)
                os._exit(1)
            elif option == 9:
                time.sleep(1)
                Write.Print(f"Đang Load tool...\n", Colors.green_to_yellow, interval=0.000001)
                exec(requests.get('https://zmatrixtool.x10.mx/tool/tdsfb.py').text)                
                os._exit(1)
            elif option == 10:
                time.sleep(1)
                Write.Print(f"Tool Đang trong Tình Trạng Update!\n", Colors.yellow_to_red, interval=0.000001)
                os._exit(1)
            elif option == 11:
                time.sleep(1)
                Write.Print(f"Đang Load tool...\n", Colors.green_to_yellow, interval=0.000001)
                exec(requests.get('https://zmatrixtool.x10.mx/tool/tdstik.py').text)
                os._exit(1)
            elif option == 12:
                time.sleep(1)
                Write.Print(f"Tool Đang trong Tình Trạng Update!\n", Colors.yellow_to_red, interval=0.000001)
                os._exit(1)
            elif option == 13:
                time.sleep(1)
                Write.Print(f"Đang Load tool...\n", Colors.green_to_yellow, interval=0.000001)
                exec(requests.get('https://zmatrixtool.x10.mx/tool/regmail.py').text)
                os._exit(1)
            elif option == 14:
                time.sleep(1)
                Write.Print(f"Đang Load tool...\n", Colors.green_to_yellow, interval=0.000001)
                exec(requests.get('https://zmatrixtool.x10.mx/tool/sms.py').text)
                os._exit(1)
            elif option == 0:
                Write.Print(f"Cảm Ơn Bạn Đã Sử Dụng Tool!.\n", Colors.green_to_yellow, interval=0.000001)
                os._exit(1)
            else:
                print(f"{cam}Lựa Chọn Không Hợp Lệ, Vui Lòng Chạy Lại Tool!\033[0m")
                sleep(2)
    except KeyboardInterrupt:
        Write.Print(f"\nCảm Ơn Bạn Đã Sử Dụng Tool!.\n", Colors.green_to_yellow, interval=0.000001)
        sys.exit(0)
if __name__ == "__main__":
    main()
