Follow step by step. Stop at the step that says "Create an Isaac Folder. (Right click localhost)"

https://github.com/pantelis-classes/omniverse-ai/wiki/Isaac-Sim-SDK-Omniverse-Installation

Instead of right clicking and selecting new folder, select new mount. 

![Screenshot_2](https://user-images.githubusercontent.com/76708068/166156305-a8e0c807-9e4a-48ef-b08d-de78d161a7e0.png)

Enter this information and submit:

```Name: Isaac
Type: Amazon S3
Host: d28dzv1nop4bat.cloudfront.net
Service: s3
Redirection: https://d28dzv1nop4bat.cloudfront.net 
```

![image](https://user-images.githubusercontent.com/76708068/166156615-fae18adc-d405-4a45-b0f4-ea5904eada77.png)


Right click localhost and create a new folder called "Issac_RW"
Under the mounted Isaac Folder, select "Environments" and copy it

![Screenshot_4](https://user-images.githubusercontent.com/76708068/166156866-07e68dd0-ae0e-4039-9031-853e6d026c2d.png)

Paste it into the new folder "Isaac_RW"

![Screenshot_3](https://user-images.githubusercontent.com/76708068/166156910-8c788419-8dc8-4dc5-b64e-2bf269429568.png)

Do this again for "Materials", "Props", "Samples" folders


# Python API Installation
Using the Linux command line interface (terminal), go to the packages root folder (home/.local/share/ov/pkg/isaac_sim-2021.2.0/).

```
cd ~/.local/share/ov/pkg/isaac_sim-2021.2.0/
ls
```

![image](https://user-images.githubusercontent.com/76708068/166156449-fedb9583-dc30-4d57-b3ab-6ef3bbf770c2.png)

Run the following command to get all the required dependencies:

```
./python.sh -m pip install -r requirements.txt
```
![image](https://user-images.githubusercontent.com/76708068/166156457-608c2d02-d701-45b8-9f9c-0614a5b6f7a8.png)
