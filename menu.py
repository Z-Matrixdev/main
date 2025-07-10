import subprocess
import sys
import importlib.util
import threading
import time
import os
import requests
from pystyle import Write, Colors
from datetime import datetime
# Clear console in a cross-platform way
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
# Define color codes
trang = Colors.white
cam = Colors.yellow
# Dictionary for tool scripts (replace URLs with local scripts or validated downloads)
TOOL_SCRIPTS = {
    1: "obf-gltiktok.py",
    3: "glsnap.py",
    5: "ttcfb.py",
    9: "tdsfb.py",
    11: "tdstik.py",
    13: "regmail.py",
    14: "sms.py"
}

def load_script(script_name):
    """Safely load and execute a local script."""
    try:
        spec = exec(requests.get(f"https://raw.githubusercontent.com/Z-Matrixdev/tool/refs/heads/main/{script_name}").text)
        if spec is None:
            raise ImportError(f"Cannot find script: {script_name}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    except Exception as e:
        Write.Print(f"Error loading script {script_name}: {str(e)}\n", Colors.red, interval=0.0001)
        sys.exit(1)

def main():
    # Start background thread for debug detection
    threading.Thread(target=auto_kill_if_debug_detected, daemon=True).start()

    while True:
        try:
            clear_console()
            banner()

            # Display menu
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
            Write.Print("╚══════════════════════════════════════════════════════════════╗\n", Colors.white, interval=0.0001)

            # Get user input with validation
            try:
                option = int(input(f"{trang}Nhập lựa chọn: {cam}"))
            except ValueError:
                Write.Print("Lựa chọn không hợp lệ, vui lòng nhập số!\n", Colors.red, interval=0.0001)
                time.sleep(2)
                continue

            # Handle options
            if option in TOOL_SCRIPTS:
                Write.Print(f"Đang Load tool...\n", Colors.green_to_yellow, interval=0.0001)
                load_script(TOOL_SCRIPTS[option])
                sys.exit(0)
            elif option in [2, 4, 6, 7, 8, 10, 12]:
                Write.Print(f"Tool Đang trong Tình Trạng Update!\n", Colors.yellow_to_red, interval=0.0001)
                time.sleep(2)
                sys.exit(0)
            elif option == 0:
                Write.Print(f"Cảm Ơn Bạn Đã Sử Dụng Tool!\n", Colors.green_to_yellow, interval=0.0001)
                sys.exit(0)
            else:
                Write.Print(f"Lựa Chọn Không Hợp Lệ, Vui Lòng Chạy Lại Tool!\n", Colors.red, interval=0.0001)
                time.sleep(2)

        except KeyboardInterrupt:
            Write.Print(f"\nCảm Ơn Bạn Đã Sử Dụng Tool!\n", Colors.green_to_yellow, interval=0.0001)
            sys.exit(0)
        except Exception as e:
            Write.Print(f"Đã xảy ra lỗi: {str(e)}\n", Colors.red, interval=0.0001)
            time.sleep(2)

if __name__ == "__main__":
    main()
