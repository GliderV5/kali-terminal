import os 

os.system("clear")
if str(input("This tool will install zsh and configure it like kali terminal. Continue ? (y/n) >>> ")) == "y":
    os.system("sudo apt-get install zsh -y")
    os.system("sudo cp .zshrc ~/.zshrc")
    os.system("dconf load /org/gnome/terminal/ < gnome_terminal_settings_backup.txt")
    os.system("clear")
    print()
    if str(input("The system need to reboot. Reboot now ? (y/n) >>> ")) == "y":
        os.system("sudo reboot")
    else:
        exit()
    
else:
    exit()
