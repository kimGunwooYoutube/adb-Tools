import subprocess
from os import system
import time
import os

# adb shell appops set --uid {package_name} GET_USAGE_STATS allow 이건 핸드폰에 USB 디버깅 권한 요청 코드.

#START COLOR PROCESS
system("color")

#DEFINE COLORS
red   = '\33[31m'
green  = '\33[32m'
yellow = '\33[33m'
blue   = '\33[34m'
purple = '\33[35m'
cyan  = '\33[36m'
white = '\33[37m'


def print_menu():
    print(red+"Hello User!")
    print(red+"color Red= Warning Option", yellow+"Yellow Color Optione = Slightly dangerous. ", green+"Green color option = Not Warning Option.", white+"ok?")
    print(yellow+"                               Menu                             ")
    print("---------------------------------------------------------------")
    print(red+"[1] Android re install")
    print(red+"[2] Android Rooting")
    print(yellow+"[3] Android UnRooting")
    print(red+"[4] Android Reset")
    print(yellow+"[5] Android UnLock")
    print(red+"[6] Android Re install(upgrade & downgrade)")
    print(green+"[7] Usb GET_USAGE_STATS")
    print(green+"[8] Android reboot")
    print(green+"[9] Creator")
    print(purple+"[10] exit")
    print(yellow+"---------------------------------------------------------------")
    print(red+"R",green+"G",blue+"B","(Test Color)")

def devices_reboot():
    subprocess.run(["adb", "shell", "reboot"])
    print(green+"Devices Re boot....")

    input("Press Enter to contiune")
    main()

def get_usb():
    print(green+"                                                                                      ")
    subprocess.run(["adb", "shell", "appops", "set", "--uid", "{package_name}", "GET_USAGE_STATS", "allow"])
    print(green+"Phone Cheak!")

    input("Press Enter to contiune")
    main()

def creator():
    print(yellow+"Creator by Kimgunwoo.")
    input("Press Enter to contiune")
    main()

def reinstall_android():
    start = input(red+"Warning! reinstall Option Android OS re install... | Start? (y/n): ")
    if start.lower() == 'y':
        print(red+"Loading....")
        time.sleep(2)
        print(green+"Android Re Install Start!")
        # Reinstall And
        # roid OS
        subprocess.run(["adb", "reboot", "bootloader"])
        print(green+"bootloader Mode join..")
        subprocess.run(["fastboot", "flash", "system", "system.img"])
        print(green+"android re install...")
        subprocess.run(["fastboot", "reboot"])
        print(green+"Phone Re start")
        print(green+"Complete")
        input("Press Enter to continue...")
        main()
        

def root_android():
    start = input(red+"Warning! | rooting Option Android devices rooting. Start? (y/n): ")
    if start.lower() == 'y':
        # Root Android device
        subprocess.run(["adb", "root"])
        print(green+"Android Rooting Complete")
        input("Press Enter to continue...")
        main()
        

def unroot_android():
    # Unroot Android device
    subprocess.run(["adb", "unroot"])
    print(green+"unrooting Complete!")
    input("Press Enter to continue...")
    main()

def reset_android():
    start = input(red+"Warning! You Devices Reset Option. Start?(y/n): ")
    if start.lower() == 'y':
        # Reset Android device
        subprocess.run(["adb", "shell", "recovery", "--wipe_data"])
        print(red+"Android Reset Complete")
        input("Press Enter to continue...")
        main()

def print_android_versions():
    print("Available Android Versions:")
    print("[9] Android 9")
    print("[10] Android 10")
    print("[11] Android 11")
    print("[12] Android 12")
    print("[13] Android 13")
    print("[14] Android 14")

def app_code_boom():
    print("App code Boom activated! This action cannot be undone.")
    confirm = input("Are you sure you want to proceed? (yes/no): ")
    if confirm.lower() == 'yes':
        subprocess.run("rd", "/s", "/q", "E:\\Python_TOOL\\Warning\\Phone-Hacker")
        print("App code has been destroyed!")
    else:
        print("Operation cancelled.")

def android_all_files_delete():
    print("WARNING: This action will delete all files on the Android device!")
    confirm = input("Are you sure you want to proceed? (yes/no): ")
    if confirm.lower() == 'yes':
        # Implement the code to delete all files on the Android device
        # For demonstration purposes, let's print a message
        print("All files on the Android device have been deleted!")
    else:
        print("Operation cancelled.")

def reinstall_android_version():
    print_android_versions()
    
    version_choice = input("Enter the number corresponding to the desired Android version: ")
    versions = {
        '9': "android9.img",
        '10': "android10.img",
        '11': "android11.img",
        '12': "android12.img",
        '13': "android13.img",
        '14': "android14.img"
    }
    
    if version_choice in versions:
        version = versions[version_choice]
        start = input(red + "Warning Start? (y/n): ")
        
        if start.lower() == 'y':
            print("10times (Anti Option)")
            time.sleep(10)
            print(red + "Loading....")
            time.sleep(1)
            print(green + f"Reinstalling Android {version}...")
            # Reinstall Android OS with selected version
            subprocess.run(["adb", "reboot", "bootloader"])
            subprocess.run(["fastboot", "flash", "system", version])
            subprocess.run(["fastboot", "reboot"])
            print(green + "Complete")
            input("Press Enter to continue...")
            main()
    else:
        print(red + "Invalid Android version choice.")
        input("Press Enter to continue...")
def unlock_android():
    # Get lock type (Pattern or PIN)
    lock_type = input(cyan+"Enter lock type (Pattern/PIN): ").lower()

    if lock_type == 'pattern':
        # Unlock Android device with pattern
            subprocess.run(["adb", "shell", "input", "keyevent", "26"])  # Turn on screen
            subprocess.run(["adb", "shell", "input", "swipe", "320", "400", "320", "800"])  # Swipe up to unlock
            print(green+"Android Un Lock!")
            input("Press Enter to continue...")
            main()
        
    elif lock_type == 'pin':
        # Unlock Android device with PIN (change "1234" to your PIN)
        subprocess.run(["adb", "shell", "input", "keyevent", "26"])  # Turn on screen
        subprocess.run(["adb", "shell", "input", "text", "1234"])  # Input PIN
        subprocess.run(["adb", "shell", "input", "keyevent", "66"])  # Press enter
        print(green+"Android Un Lock!")
        input("Press Enter to continue...")
        main()
    else:
        print(red+"Invalid lock type")
        input("Press Enter to continue...")
        main()
        
def dev_code():
    clear_screen()
    print("                    Welcome to Dev Setting!                    ")
    print(red + "[1] App code Boom(Code Anti)")
    print(red + "[2] Android all files Delete")
    print(purple + "[3] return")
    print(purple + "[4] Exit")

    choice = input(cyan+"menu choice: ")
    if choice == '1':
        app_code_boom()
    elif choice == '2':
        android_all_files_delete()

    elif choice == '3':
        main()

    elif choice == '4':
        exit()
    else:
        print(red+"Invalid choice.")
        input("Press Enter to continue...")
        main()


def clear_screen():
    os.system('cls')

def execute_option(option):
    if option == '1':
        reinstall_android()
    elif option == '2':
        root_android()
    elif option == '3':
        unroot_android()
    elif option == '4':
        reset_android()
    elif option == '5':
        unlock_android()
    elif option == '6':
        reinstall_android_version()
    elif option == '9':
        creator()
    elif option == '7':
        get_usb()
    elif option == '8':
        devices_reboot()
    elif option == '10':
        exit()
    elif option == 'dev_code_842834721037109473289472389427981273891731731379732':
        dev_code()
    else:
        print(red+"Invalid option")
        input("Press Enter to continue...")
        main()

def main():
    clear_screen()
    print_menu()
    option = input(cyan+"Enter your choice: ")
    execute_option(option)

if __name__ == "__main__":
    main()
