# Omniverse and Isaac Sim installation (executable)

# 2.1 Create nvidia developer account.

## This is required to access some of the downloads as well as obtaining API keys for Nvidia NGC

-  Go to this <a href="https://developer.nvidia.com/developer-program">link</a> and create an account.

![image](https://user-images.githubusercontent.com/589439/143655734-92f93f94-723b-4a03-aee3-9004ebdfa931.png)

-  Fill out your NVIDIA profile.

![image](https://user-images.githubusercontent.com/589439/143655803-423dddd8-398e-49e0-839f-d96a5e655441.png)

# 2.2 Go to this <a href="https://www.nvidia.com/en-us/omniverse/">omniverse link</a> and download Omniverse and install.

![image](https://user-images.githubusercontent.com/589439/143158851-a4f7a00b-4f25-40e0-ae2e-2fba3edef08e.png)

-  Fill out the form.

![image](https://user-images.githubusercontent.com/589439/143158880-17506781-abc2-4188-aca3-4546dcb475f9.png)

-  Click the download link for Linux.

![image](https://user-images.githubusercontent.com/589439/143158912-97fb24ad-8b49-432e-a3d7-4badb0977714.png)

-  Download and save the AppImage file to your ~/Downloads folder.

![image](https://user-images.githubusercontent.com/589439/143158967-afad1831-822f-4440-9a4b-9248c909007d.png)

-  Run these commands to execute the AppImage.

`$ cd ~/Downloads`

`$ ls`

`$ chmod +x omniverse-launcher-linux.AppImage`

`$ ./omniverse-launcher-linux.AppImage`

![image](https://user-images.githubusercontent.com/589439/143656306-85f1aefd-a6a8-4f07-a2e9-b7153ff175ce.png)

# 2.3 Login to Omniverse to install Isaac Sim 2021.

-  Login with your NVIDIA credentials.

![image](https://user-images.githubusercontent.com/589439/143160948-90380e23-e8cc-42b3-8933-4d88c5c9bc90.png)

-  Accept the terms of agreement.

![image](https://user-images.githubusercontent.com/589439/143161008-59913f3c-cfde-4c9f-93d4-609dc0346469.png)

-  Click continue. (default paths)

![image](https://user-images.githubusercontent.com/589439/143161046-21afc550-6bf7-450c-b023-3296de59d7b4.png)

-  Install cache. (NVIDIA Omniverse Cache is a service that optimizes data transfers between Nucleus and Omniverse Apps and Connectors on user workstations.)

-  Host data with Nucleus Docker and locally cache downloaded data from Nucleus to significantly reduce time to load assets into Omniverse Apps and Connectors.

![image](https://user-images.githubusercontent.com/589439/143161192-9936a489-e81d-4ccc-a2e0-caf120ce92c4.png)

# 2.4 Installing Isaac through Omniverse.

-  Click the Exchange tab in Omniverse.

![image](https://user-images.githubusercontent.com/589439/143165080-9daa5e96-99c0-4e60-9a40-ff4f77944311.png)

-  Search for Isaac and Click Isaac Sim.

![image](https://user-images.githubusercontent.com/589439/143165387-659a75bf-ba62-49e4-9bab-320b0da9eeb1.png)

-  Click install.

![image](https://user-images.githubusercontent.com/589439/143165778-75f9cbea-b93b-4c0a-9661-269ec0e643f5.png)

# 2.5 Go to the nucleus tab and create a nucleus local server to run the Omniverse Isaac Sim Samples. (Assets)

-  Create your local nucleus account by clicking the Nucleus tab in Omniverse.

-  Click Add Local Nucleus Service.

![image](https://user-images.githubusercontent.com/589439/143163402-c38ef3e5-64a8-437f-8a4c-7f978b37e40b.png)

-  Click Next. (Default Path)

![image](https://user-images.githubusercontent.com/589439/143163446-5fa6c2bc-6437-4239-bcd7-5be8f9159de7.png)

-  Create Administrator Account. (Note: this account is not related to your NVIDIA Account
   .)

![image](https://user-images.githubusercontent.com/589439/164572862-88406493-2826-4246-aafe-a8dc28d2ce8c.png)

-  Server Instasllation.

![image](https://user-images.githubusercontent.com/589439/164573461-9b4f1c75-b562-4ada-a239-85d9276439b8.png)

-  Log into the Nucleus Service with the credentials you created.
   read

![image](https://user-images.githubusercontent.com/589439/164575160-968a154a-0b4f-47f2-9058-26ce013dc8db.png)

-  Enter the settings below.

        Name: Isaac

        Type: Amazon S3

        Host: d28dzv1nop4bat.cloudfront.net

        Service: s3

        Redirection: https://d28dzv1nop4bat.cloudfront.net

![image](https://user-images.githubusercontent.com/589439/164575465-06c23de3-5a99-43d6-bc30-fca9ef245bc6.png)

-  Your Isaac folder should now look like this.

![image](https://user-images.githubusercontent.com/589439/164575720-54249580-8f20-4bd7-b22d-0972fc21973d.png)

# 2.6 Running Isaac for the first time.

-  Click Launch in the Library Tab of Omniverse.

![image](https://user-images.githubusercontent.com/589439/143657605-6b09b104-698d-4eba-b5f7-e027eee033eb.png)

-  Click Start with the default settings with "Issac Sim" selected.

![image](https://user-images.githubusercontent.com/589439/143657653-c3d31131-1da7-4919-b7dd-8a9555c4aba6.png)
