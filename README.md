# iot-JichenLi
### EE-629-Internet-of-Things
[2020-09-14]Bought a Raspberry Pi 4B and a 32GB sd card. Download the Noobs program and the ssh to manage the Raspberry Pi through my laptop\
[2020-10-3] forget to update my progress. have learn some video about Raspberry Pi. decide to make a cnn network using Movidius Neural Compute Stick and Raspberry Pi. With Movidius Neural Compute Stick, the RP can run some deep learning network and get more functions like face detection.\
[2020-10-10] learn about the Docker showed in the Lab5a, its a package of the code we run, pack all the code into one docker.\
[2020-10-12] Do the Lab5A as the lesson5 has showed. \
[2020-10-18]I'm making a security camera, using Human body sensing module. If the sensing detect human motion, the Raspberry Pi will start the camera and start recording. Meanwhile the Raspberry Pi can analysis human face in the video. If it is a stranger, the raspberry will send a message to my phone and I can watch the situation through Raspberry Pi's camera on the phone.\
[2020-10-27]Connecting the Human body sensing module. And my camera for Raspberry Pi still on the road...\
[2020-11-1]Learning to build a CNN for face recognition.

## First, we have to bulid NCS environment 
Since my location is in China, it's better to change source to Tsinghua.edu.cn for faster downloading speed..  

run this code:  

    sudo nano /etc/apt/sources.list

add an '#' at the head of the first line and copy the command below:
    deb http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ stretch main contrib non-free rpi
    deb-src http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ stretch main contrib non-free rpi
Press 'ctrl + o', then press Enter to save, and 'ctrl + x'

run this code:
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

 


