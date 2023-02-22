## Prerequisites

Ubuntu 18.04 LTS required / 20.04 is partially supported. (This writeup is based on 20.04)

# System Requirements

![image](https://user-images.githubusercontent.com/589439/164785721-1e100b65-70fc-47db-8b8c-5d1e3de5934e.png)

# 1.1 Installing Nvidia Drivers on Ubuntu 20.04 LTS

-  This writeup is based on the docs hosted the <a href="https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/requirements.html">Nvidia Omniverse website</a>. Please check out their docs for the latest updates on installation.

`$ sudo apt-get update`

`$ sudo apt install build-essential -y`

## Install new Drivers (Please make sure the drivers are up-to-date with the minimum requirements of Nvidia Isaac)

-  Search for the "Software Updates" program in your ubuntu and open it.

![image](https://user-images.githubusercontent.com/589439/164801319-c03b41bf-1a2c-4abc-a2d7-bfd5aef323f7.png)

-  Click the "Additional Drivers" tab and select the latest version of:

        Using NVIDIA driver metapackage from nvidia-driver-xxx (proprietary)

![image](https://user-images.githubusercontent.com/589439/164801377-96cf1206-fc03-4a31-ad3a-744e1e415b06.png)

-  Reboot your system.

`$ reboot`

-  Run nvidia-smi to make sure you are on the latest nvidia drivers for Isaac.

`$ nvidia-smi`

![image](https://user-images.githubusercontent.com/589439/164801167-97d4249d-b7b3-42f0-824c-e65825389f5b.png)

# 1.2 Installing docker

-  See the <a href="https://docs.docker.com/engine/install/ubuntu/">Docker Docs</a> for more info.

`$ sudo apt-get update`

       $ sudo apt-get install \
       apt-transport-https \
       ca-certificates \
       curl \
       gnupg-agent \
       software-properties-common

`$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`

![image](https://user-images.githubusercontent.com/589439/164802008-001066e3-d6ef-4541-9c6d-bd7c43015f51.png)

`$ sudo apt-key fingerprint 0EBFCD88`

![image](https://user-images.githubusercontent.com/589439/164802062-3d1f207a-2be1-4012-9f1c-4a0dd5e591dd.png)

       sudo add-apt-repository \
              "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
              $(lsb_release -cs) \
              stable"

![image](https://user-images.githubusercontent.com/589439/164802124-b2508428-fef4-43cf-8902-9d978e2d5a7a.png)

`$ sudo apt-get update`

`$ sudo apt-get install docker-ce docker-ce-cli containerd.io`

![image](https://user-images.githubusercontent.com/589439/164802288-ceb4a115-c61f-4469-9559-baf411b385a1.png)

`$ y`

![image](https://user-images.githubusercontent.com/589439/164802257-8f2d9237-036f-42c3-9353-b8794912b7c1.png)

-  Docker is now installed on your system.

# 1.3 Installing NVIDIA Container Toolkit:

-  See the <a href="https://github.com/NVIDIA/nvidia-docker">NVIDIA Container Toolkit Repo</a> for more information.

-  Add the package repositories

`$ distribution=$(. /etc/os-release;echo $ID$VERSION_ID)`

`$ curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -`

![image](https://user-images.githubusercontent.com/589439/164802647-1f9b9163-e3cb-498f-9366-147ccbe07fea.png)

       $ curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

![image](https://user-images.githubusercontent.com/589439/164802712-e9a3ca86-aae7-424f-a286-307bd14e39b7.png)

`$ sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit`

![image](https://user-images.githubusercontent.com/589439/164802786-fe1599a8-288b-4db4-89cd-c811c42f447f.png)

`$ sudo systemctl restart docker`
