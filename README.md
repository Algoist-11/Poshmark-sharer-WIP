# Begin your path to Poshmark ambassador! (WIP)
This is a tool that automates listing sharing for your Poshmark marketplace account using Playwright, up-to-date as of March 2026.

The tool can currently share the listings of your following or followers.

# Quick start
Requirements: Chrome, a computer
No need to install extra packages, simply download the dist folder and run the .exe file.

Click on the dist folder -> click on path-to-ambassador.exe -> on the top right, click on "Download raw code" -> save and run!

Be sure to interact with the program only through the control panel, unless a reCAPTCHA is triggered.

When running the program for the first time, it will ask you a series of questions about how you wish the program to operate. Your answers will be stored as default settings in the future, and the program will ask you if you wish to use default or use new mode every time it runs in the future.

Similarly, when the program runs for the first time, it automatically asks you for login information. When it runs in the future, you will not need to enter this information again. If you wish to change the login information, or operate on a separate account, open the project folder and go to credentials.json where you can edit your credentials.

You can stop the program by pressing ctrl + C twice.

This tool limits operating speed to avoid having your account identified as bot, as well as places a limit of 8000 shares per day, a safe value close to Poshmark's daily share limit (the exact value is not publicized).


This is still a work in progress. Future functions will include:
- self share, or custom share for a list of users
- sharing to relevant parties based on tag and item name
- bulk following seller accounts

This is my first open-source project, if there are any suggestions or issues, let me know!
