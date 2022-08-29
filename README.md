# Computer Networks Fall 2022

Welcome to the Computer Networks course! Through the assignments of this course, you will gain hands-on experience with real-world network programming. You will write a program that allows your computer to communicate with another, be it across the room or across the world. You will program a router to deliver information to the right destination in a network with thousands of nodes. You will learn how decisions made by protocol designers and network administrators affect Internet performance. You will learn how to analyze data from the network to detect security threats and learn how to prevent them.

The programming assignments are designed to be challenging but manageable in the time allotted. If you have questions, want to suggest clarifications, or are struggling with any of the assignments this semester, please come to office hours or ask questions on Piazza.

Unless stated otherwise, the assignments are not group assignments. **You are not allowed to copy or look at code from other students.** However, you are welcome to discuss the assignments with other students without sharing code.

Good luck.

## Setting up Vagrant

For programminmg assignments in this course, it is highly recommended that you use Vagrant to run your code as the environment here is the same as what we will be grading with. Follow this guide on how to setup the virtual machine, and if you have any questions or issues with this, feel free to ask on Piazza or ask at office hours.

### Step 1: Install Vagrant

Vagrant is a tool for automatically configuring a VM using instructions given in a single "Vagrantfile."

**macOS & Windows:** You need to install Vagrant using the correct download link for your computer [here](https://www.vagrantup.com/downloads.html).

**Windows only**: You will be asked to restart your computer at the end of the installation. Click Yes to do so right away, or restart manually later,
but don't forget to do so or Vagrant will not work!

**Linux:** First, make sure your package installer is up to date by running the command `sudo apt-get update`. To install Vagrant, you must have the "Universe" repository on your computer; run `sudo apt-add-repository universe` to add it. Finally, run `sudo apt-get install vagrant` to install vagrant.

### Step 2: Install VirtualBox

VirtualBox is a VM provider (hypervisor).

**macOS & Windows:** You need to install VirtualBox using the correct download link for your computer [here](https://www.virtualbox.org/wiki/Downloads). The links are under the heading "VirtualBox 5.x.x platform packages."

**Windows only:** Use all the default installation settings, but you can uncheck the "Start Oracle VirtualBox 5.x.x after installation" checkbox.

**Linux:** Run the command `sudo apt-get install virtualbox`.

**Note:** This will also install the VirtualBox application on your computer, but you should never need to run it, though it may be helpful (see Step 6).

### Step 3: Install Git (and SSH-capable terminal on Windows)

Git is a distributed version control system.

**macOS & Windows:** You need to install Git using the correct download link for your computer [here](https://git-scm.com/downloads).

**macOS only:** Once you have opened the .dmg installation file, you will see a Finder window including a .pkg file, which is the installer. Opening this normally may give you a prompt saying it can't be opened because it is from an unidentified developer. To override this protection, instead right-click on thet .pkg file and select "Open". This will show a prompt asking you if you are sure you want to open it. Select "Yes". This will take you to the (straightforward) installation.

**Windows only:** You will be given many options to choose from during the installation; using all the defaults will be sufficient for this course (you can uncheck "View release notes" at the end). The installation includes an SSH-capable Bash terminal usually located at `C:\Program Files\Git\bin\bash.exe`. Another option for a SSH-capable terminal is Windows Powershell.

**Linux:** `sudo apt-get install git`.

### Step 4: Install X Server

You will need an X Server to input commands to the virtual machine.

**macOS:** Install [XQuartz](https://www.xquartz.org/). You will need to log out and log back in to complete the installation (as mentioned by the prompt at the end).

**Windows:** Install [Xming](https://sourceforge.net/projects/xming/files/Xming/6.9.0.31/Xming-6-9-0-31-setup.exe/download). Use default options and uncheck "Launch Xming" at the end.

**Linux:** The X server is pre-installed!

### Step 5: Clone course Git repository

Open your terminal (use the one mentioned in step 3 if using Windows) and `cd` to wherever you want to keep files for this course on your computer.  

Run `https://github.com/sepehrabdous/Computer_Networks_Spring21.git` to download the course files from GitHub.

`cd Computer_Networks_Spring21` to enter the course assignment directory.

### Step 6: Provision virtual machine using Vagrant

From the `Computer_Networks_Spring21` directory you just entered, run the command  `vagrant up` to start the VM and  provision it according to the Vagrantfile. You will likely have to wait several minutes. You may see warnings/errors in red, such as "default: stdin: is not a tty", but you shouldn't have worry about them.

**Note 1**: The following commands will allow you to stop the VM at any point (such as when you are done working on an assignment for the day):

* `vagrant suspend` will save the state of the VM and stop it. Always suspend when you are done with the machine.
* `vagrant halt` will gracefully shutdown the VM operating system and power down the VM. Run this to completely stop the machine.
* `vagrant destroy` will remove all traces of the VM from your system. If you have files exclusively saved to your VM, save those to your actual machine before executing this command. 

Additionally, the command `vagrant status` will allow you to check the status of your machine in case you are unsure (e.g. running, powered off, saved...).
You must be in some subdirectory of the directory containing the Vagrantfile to use any of the commands above, otherwise Vagrant will not know which VM you are referring to.

**Note 2**: The VirtualBox application that was installed in Step 2 provides a visual interface as an alternative to these commands, where you can see the status of your VM and power it on/off or save its state. It is not recommended to use it, however, since it is not integrated with Vagrant, and typing commands should be no slower. It is also not an alternative to the initial `vagrant up` since this creates the VM.

### Step 7: Test SSH to VPN

Run `vagrant ssh` from your terminal. This is the command you will use every time you want to access the VM. If it works, your terminal prompt will change to `vagrant@networks:~$`. All further commands will execute on the VM. You can then run `cd /vagrant` to get to the course directory that's shared between your regular OS and the VM.

Vagrant is especially useful because of this shared directory structure.  You don't need to copy files to and from the VM. Any file or directory in the `Computer_Networks_Spring21` directory where the `Vagrantfile` is located is automatically shared between your computer and the virtual machine. This means you can use your IDE of choice from outside the VM to write your code (but will still have to build and run within the VM).

The command `logout` will stop the SSH connection at any point.

### Common Errors

Here are some fixes to known errors and problems with Vagrant.

#### Error 1: Aftering powering down Vagrant for the first time, `vagrant up` gets stuck on trying to connect to the machine.

This repeated attempt to connect may take anywhere from 1 to 10 minutes. There are a couple of ways to immeditely rectify this, but the easiet method that always works is to use `vagrant destroy` to tear down the virtual machine. Your files will remain on your computer so long as you are saving them to your computer and not exclusively to the vagrant machine. Afterwards, provision the machine the same way in step 6, using `vagrant up`. Make sure to only use `vagrant suspend` as this seems to keep the machine from stalling on starting it up between sessions. 

### Extra Note for Windows users

Line endings are symbolized differently in DOS (Windows) and Unix (Linux/MacOS). In the former, they are represented by a carriage return and line feed (CRLF, or "\r\n"), and in the latter, just a line feed (LF, or "\n"). Given that you ran `git pull` from Windows, git detects your operating system and adds carriage returns to files when downloading. This can lead to parsing problems within the VM, which runs Ubuntu (Unix). Fortunately, this only seems to affect the shell scripts (\*.sh files) we wrote for testing. The `Vagrantfile` is set to automically convert all files back to Unix format, so **you shouldn't have to worry about this**. **However**, if you want to write/edit shell scripts to help yourself with testing, or if you encounter this problem with some other type of file, use the preinstalled program `dos2unix`. Run `dos2unix [file]` to convert it to Unix format (before editing/running in VM), and run `unix2dos [file]` to convert it to DOS format (before editing on Windows). A good hint that you need to do this when running from the VM is some error message involving `^M` (carriage return). A good hint you need to do this when editing on Windows is the lack of new lines. Remember, doing this should only be necessary if you want to edit shell scripts.
