# iot-JichenLi 
## Project: Face detection and Internet penetration
### EE-629-Internet-of-Things
[2020-09-14] Bought a Raspberry Pi 4B and a 32GB sd card. Download the Noobs program and the ssh to manage the Raspberry Pi through my laptop.

[2020-10-3] Forget to update my progress. have learn some video about Raspberry Pi. decide to make a cnn network using Movidius Neural Compute Stick and Raspberry Pi. With Movidius Neural Compute Stick, the RP can run some deep learning network and get more functions like face detection.

[2020-10-10] Learn about the Docker showed in the Lab5a, its a package of the code we run, pack all the code into one docker.

[2020-10-12] Do the Lab5A as the lesson5 has showed. 

[2020-10-18] I'm making a security camera, using Human body sensing module. If the sensing detect human motion, the Raspberry Pi will start the camera and start recording. Meanwhile the Raspberry Pi can analysis human face in the video. If it is a stranger, the raspberry will send a message to my phone and I can watch the situation through Raspberry Pi's camera on the phone.

[2020-10-27] Connecting the Human body sensing module. And my camera for Raspberry Pi still on the road...

[2020-11-1] Learning to build a CNN for face recognition.

[2020-12-7] This month I finished my project. Face detection is not hard. However how to make Raspberry Pi visible on the internet is kind of difficult. I've tried many ways. First I try to use a python library called Wechat_sender. It should be able to send message to my wechat. But I find that the library need wechat web on the browser and Tecent has closed this service. Then I tried a internet penetraion tool called 'Peanut shells','花生壳' in Chinese. The problem is, my Rasberry Pi installed armv7l system, which is 32-bit. And the Peanut shells' latest version only support armv8, which is 64-bit system. It's not work again. Another way is using cloud server, and nearlly all of them need to pay an extra money like the Lab6's Particle Cloud. Finally I find a free tool named Cploar which can do intranet penetration. So I tried and succeeded. Besides lab6, I also do the lab7, lab8. Actually lab8 is the same as the homework3 of EE695.

# Face detection

## First, we have to bulid NCS environment 
Since my location is in China, it's better to change source to Tsinghua.edu.cn for faster downloading speed.  

run this code:  

    sudo nano /etc/apt/sources.list

add an '#' at the head of the first line and copy the command below:

    deb http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ stretch main contrib non-free rpi
    deb-src http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ stretch main contrib non-free rpi

Press 'ctrl + o', then press Enter to save, and 'ctrl + x'

Run this code:

    sudo apt-get update

So we succeed in changing source.

## Install the OpenVINO™ Toolkit for Raspbian* OS Package
This step could refer to 'https://docs.openvinotoolkit.org/latest/openvino_docs_install_guides_installing_openvino_raspbian.html#install-package'  

It's a guidence made by openvino to help you prepare the environment for NCS.

First run:

    cd ~/Downloads/
    
Then:

    sudo wget https://download.01.org/opencv/2020/openvinotoolkit/2020.1/l_openvino_toolkit_runtime_raspbian_p_2020.1.023.tgz

You can view 'https://software.intel.com/en-us/articles/OpenVINO-Install-RaspberryPI' to check which version you want to install. I choose the version '2020.1.023'.  

After downloading the file, you have to unpack the archive:

    sudo tar -xf  l_openvino_toolkit_runtime_raspbian_p_<version>.tgz --strip 1 -C /opt/intel/openvino

Now the OpenVINO toolkit components are installed. 

## Install External Software Dependencies
CMake* version 3.7.2 or higher is required for building the Inference Engine sample application. To install, open a Terminal* window and run the following command:  

    sudo apt install cmake

And in this step my terminal show me that 'cmake :rely on libcurl3 (>= 7.16.2) but it will not be installed.'   
So run this:

    sudo apt-get install -y libcurl3

This can solve the problem.

## Set the Environment Variables
You must update several environment variables before you can compile and run OpenVINO toolkit applications. Run the following script to temporarily set the environment variables:   

    source /opt/intel/openvino/bin/setupvars.sh

Or you can permanently set the environment variables as follows:

    echo "source /opt/intel/openvino/bin/setupvars.sh" >> ~/.bashrc

oepn a new terminal, if you see this below meaning success.

## Add USB Rules

    sudo usermod -a -G users "$(whoami)"
    sh /opt/intel/openvino/install_dependencies/install_NCS_udev_rules.sh

then we are ready to compile and run Object detection sample

## Build and Run Object Detection Sample
Follow the next steps to run pre-trained Face Detection network using Inference Engine samples from the OpenVINO toolkit.

1.Navigate to a directory that you have write access to and create a samples build directory. This example uses a directory named build:
    
    mkdir build && cd build

2.Build the Object Detection Sample:
    
    cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS="-march=armv7-a" /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp
    make -j2 object_detection_sample_ssd

## Download the pre-trained Face Detection model or copy it from the host machine:
Should pay attention here: if you download the model from the Guide, it will not work. The model after 2020 all has a bug that it can not run correctly.

You may meet this trouble:

![image](https://github.com/Ostrich96/iot-JichenLi/blob/master/pic/pic%20(8).png)

So I recommond you download the model below:
    
    wget --no-check-certificate https://download.01.org/opencv/2019/open_model_zoo/R3/20190905_163000_models_bin/face-detection-adas-0001/FP16/face-detection-adas-0001.xml
 
To download the .xml file with the network topology:
    
    wget --no-check-certificate https://download.01.org/opencv/2019/open_model_zoo/R3/20190905_163000_models_bin/face-detection-adas-0001/FP16/face-detection-adas-0001.bin

## Run human face detection:
Put the model we download before into the same folder with the face_detection.py.

To run this .py, you have to install opencv
    
    pip3 install opencv-python

Then check the camera situation. Attention, you have to turn on the camera service

![image](https://github.com/Ostrich96/iot-JichenLi/blob/master/pic/pic%20(6).png)

Run:
    
    python3 face_detection.py

You can check the result now.

![image](https://github.com/Ostrich96/iot-JichenLi/blob/master/pic/pic%20(3).png)

## Quit
 Press 'q' if you want to quit the face_detection program, and the program will generate an 'out.png' in the folder, which catch the last frame through the detection.

 # Internet penetration
 We have succeed in doing face detection, however, you can only watch it through your Raspberry Pi. What if we want to make it a monitor and can observe the situation from far away through internet?

 ## Install Mjpg-Streamer
    
    sudo apt-get install cmake libjpeg8-dev
    wget https://github.com/Five-great/mjpg-streamer/archive/master.zip

Then unzip the file:

    unzip master.zip

Enter the table run make:

    cd mjp*g-*
    cd mjpg-*
    make

    sudo make install

    cd

Run the Mjpg-Streamer:

    /usr/local/bin/mjpg_streamer -i "/usr/local/lib/mjpg-streamer/input_uvc.so -n -f 30 -r 1280x720" -o "/usr/local/lib/mjpg-streamer/output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www"

You can get the similar result like me:

![image](https://github.com/Ostrich96/iot-JichenLi/blob/master/pic/pic%20(5).png)

-f 30 means frame rate, you can change it as you want.

-r 1280x720 means resolution, youcan also change it.

-p 8080 means through the 8080 port.

## Install Cpolar

To make our Raspberry Pi visible on the internet, I used a tool name Cpolar. It a free tool for intranet penetration

you can learn more on https://www.cpolar.com/

First we have to register an account.

Then install Cpolar on the Raspberry Pi:

    sudo wget https://www.cpolar.com/static/downloads/cpolar-stable-linux-arm.zip
    sudo unzip cpolar-stable-linux-arm.zip

## Set up token

Get your account's token from the Cpolar' web.

For my internet safety I covered part of my token

![image](https://github.com/Ostrich96/iot-JichenLi/blob/master/pic/pic%20(7).png)

Run:

    ./cpolar authtoken  <yourauthtoken>

## Open 8080 port

Open a new window shell, run this:

    ./cpolar http 8080

You will get this:

![image](https://github.com/Ostrich96/iot-JichenLi/blob/master/pic/pic%20(4).png)

The Tunnel Status should be: online. It means you penetrate intranet successfully.

The Account is your user name

Fowarding is the ip address tha Cpolar distribute to you Raspberry Pi.

Use any device that can get into internet, enter the address in the picture, you can watch the camera through internet now.

![image](https://github.com/Ostrich96/iot-JichenLi/blob/master/pic/pic%20(1).png)

![image](https://github.com/Ostrich96/iot-JichenLi/blob/master/pic/pic%20(2).png)


