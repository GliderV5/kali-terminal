import os 

os.system("clear")
if str(input("This tool will install zsh and configure it like kali terminal. Continue ? (y/n) >>> ")) == "y":
    os.system("sudo apt-get install zsh")
    os.system("sudo cp .zshrc ~/.zshrc")
    os.system("dconf load /org/gnome/terminal/ < gnome_terminal_settings_backup.txt")
    os.system("chsh -s $(which zsh)")
    os.system("clear")
    print()
    os.system("mkdir ~/.config/zsh/")
    input()
    os.system("git clone https://github.com/zsh-users/zsh-syntax-highlighting ~/.config/zsh/zsh-syntax-highlighting")
    os.system("git clone https://github.com/zsh-users/zsh-autosuggestions ~/.config/zsh/zsh-autosuggestions")
    os.system("git clone https://github.com/zap-zsh/sudo ~/.config/zsh/sudo-zsh")
    os.system("source ~/.zshrc")
    if str(input("The system need to reboot. Reboot now ? (y/n) >>> ")) == "y":
        os.system("sudo reboot")
    else:
        exit()
    
else:
    exit()
