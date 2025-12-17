# How to install
1. Install the required fonts:

    ~~~shell
    sudo pacman -S ttf-nerd-fonts-symbols
    sudo pacman -S ttf-jetbrains-mono-nerd
    ~~~

2. Сlone the repository and copy the files to your waybar config directory (make a copy of your current config just in case):

    ~~~shell
    git clone https://github.com/abl1v1on/waybar-black-and-white-theme.git
    cp -r waybar-black-and-white-theme/* ~/.config/waybar && cd ~/.config/waybar
    ~~~

3. Run the script to reload the waybar:

    ~~~shell
    # In waybar config directory
    sudo chmod +x scripts/restart.sh
    ./scripts/restart.sh
    ~~~

# Modules
You can change the modules configuration in the config.jsonc file. For example, change the time zone or format for clock:

~~~json
"clock": {
  "interval": 60,
  "timezone": "Asia/Yekaterinburg", // set your timezone here
  "format": " {:%I:%M %p}" // 03:20 AM/PM
},
~~~

# Theme configuration
You can switch between dark and light theme. If you have dark wallpaper, choose a light theme. if the wallpaper is light, select a dark theme:
~~~css
/* style.css */

/* just swap them */
@define-color main-text-color #f0f0f0; /* light */
@define-color main-bg-color #212121; /* dark */
~~~

### Dark theme
![dark theme](readme_assets/dark.png)

### Light theme
![light theme](readme_assets/light.png)


> ⚠️ **This config is recommended to be used only in conjunction with dark or light wallpaper!**
