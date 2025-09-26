# September 26, 2025 

I had some difficulties packaging a Kivy/KivyMD app for AMD64 PC !!

So I found the method of AMD64 PC using UBUNTU 24.04(NOT 22.04) LTS

# First Install oracle virutalbox: 7.0.18 version. 

THE SPECIFIC VERSION IS VERY IMPORTANT!

# Second Install Ubuntu 24.04 Desktop Verison

# Third .... USING TERMINAL ... IN UBUNTU 24.04.

# Step by step ... Build Android apk with Buildozer on ubuntu 24.04 LST

1. sudo apt install python3-pip

2. sudo apt install python3.12-venv

3. mkdir myapp                   ## example directory

4. sudo chmod -R 777 myapp

5. cd myapp

6. ls -lart

7. sudo python3 -m venv .venv

8. source .venv/bin/activate

9. sudo chmod -R 777 .venv

10. pip install --upgrade buildozer

11. sudo apt update

12. sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

13. pip3 install --upgrade Cython==0.29.33 virtualenv       

14. export PATH=$PATH:~/.local/bin/                         # add the following line at the end of your ~/.bashrc file

15. sudo apt install -y automake

16. sudo apt update

17. wget http://security.ubuntu.com/ubuntu/pool/universe/n/ncurses/libtinfo5_6.3-2ubuntu0.1_amd64.deb

18. sudo apt install ./libtinfo5_6.3-2ubuntu0.1_amd64.deb

19. pip3 install setuptools

20. buildozer init                                          # modify buildozer.spec

21. buildozer -v android debug
 
