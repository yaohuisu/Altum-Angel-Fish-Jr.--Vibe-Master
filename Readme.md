# Altum Angel Fish Jr. - Vibe Master
# Introduction
This work is based on the WE-I Plus platform and use the emotion recognition AI model to identify the user’s emotions, and use the results to give feedback to the user, such as: adjusting the ambient lights, playing music that suits the current vibe, and LINE Bot sending caring messages to help user to achieve a better mental state.
# HW & SW Setup
## HW
- WE-I Board
- Smart Phone compatible with Line app
## SW
- set up https://github.com/foss-for-synopsys-dwc-arc-processors/arc_contest.git enviroment
- Python3
# User Manual
## WE-I
- Put `vibe_master` folder into `arc_constest\Synopsys_SDK\User_Project` clone from [link](https://github.com/foss-for-synopsys-dwc-arc-processors/arc_contest.git)
- open cmd in `vibe_master` floder, type
```shell
make
```
- the ```.elf``` and ```.map``` are generated
- in Ubuntu enviroment, vibe_master` floder, type
```shell
make flash
```
- tne ```.img``` file is than generated
- Upload the ```.img``` file with **teraterm**
- Press reset button and the program is excuted
## Linebot
### How to run
1. Follow [this link](https://dashboard.ngrok.com/get-started/setup) to setup your Ngrok environment.
2. Copy the forwarding link and paste to Linebot channel to establish webhook.![](img/cmd_ngrok.png)
![](img/line.png)
3. Excute **Linebot_server.py**.
