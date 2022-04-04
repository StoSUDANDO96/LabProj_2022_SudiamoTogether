# LabProj_2022_SudiamoTogether

MESSAGE TO ALL THE GROUP MEMBERS:

This very simple repository is a tester for lab activities in Software and Computing for Applied Physics. Unfortunately I do not know how much time I will be able to spend at daytime on all of this, but feel free to modify, add and comment anything you like :) 

Wish you the very best, remember that in any case:

*Science is a cemetery of dead ideas, even though life may issue from them.* (M. De Unamuno) <3

## How to collaborate

Since we are still learning how to work on Github, here is a very basic guide to collaborate on this repository. After being invited to collaborate:
* It is advised that you 'watch' this repository in order to receive notifications of new commits and updates.
* Then, if you don't have Git installed:
  * Under Ubuntu, open a terminal and install Git with the following command:
    ```shell
        sudo apt-get install git
    ```
  * If you are using Windows, open the PowerShell as administrator (right click + Run as administrator) and install [chocolatey](https://chocolatey.org/install) (follow their instructions). Then install Git with the following command:
    ```powershell
        cinst git
    ```
* Find a local directory on your computer where you can work. It can be a directory which contains your Master's degree projects, or you can create a new one.
* Open a terminal and move into the directory you chose with:
  ```
      cd /full/path/to/my/folder
  ```
  If you don't want to write the whole path each time, you can create an environment variable on Linux:
  ```shell
      echo -e "\n export WORKSPACE=/full/path/to/my/folder \n" >> ~/.bashrc
  ```
  On Windows you can run this:
  ```powershell
      rundll32 sysdm.cpl,EditEnvironmentVariables
  ```
  and it will open a window where you can manage environment variables. Name one variable `WORKSPACE` and assign the path to your directory to it. Then, after opening the terminal again, you can change the current/working directory with:
  ```
      cd $WORKSPACE       # on Linux
      cd $env:WORKSPACE   # on Windows PowerShell
      cd %WORKSPACE%      # on Windows Command Prompt (cmd.exe)
  ```
* Clone this repository on your workspace (you need to do this only once):

      git clone https://github.com/StoSUDANDO96/LabProj_2022_SudiamoTogether.git
  
  This will create a new directory, containing the repository with all its history. So move into that directory with:

      cd LabProj_2022_SudiamoTogether
  
* Check the status of the local branch against the remote repository:

      git status

  It will say if your local repository is up to date (nothing to be done), behind (you need to pull), ahead (you need to push) or even if you have pending changes that need to be committed.

* Make sure your local repository is up to date before editing its content:

      git pull

* After your edits, you can commit the changes into your local repository with:

      git commit -a -m "A description of what you did to the unlucky code"

  This will ignore all files with names, paths or extensions contained inside `.gitignore`. If the programs you are using create temporary and junk files, you can add them to `.gitignore`, so that they will not be tracked nor committed.

* You can then update the files on the remote repository:

      git push

  Note that you can commit many times before pushing, but it is advised to push as soon as possible in order to minimize chances of diverging branches. All your commits will be visible on remote only after you run `git push`. The first time you do this, Github will ask for your credentials.

If anything goes wrong, Git will abort the command and propose suggestions to solve the problem (for example, running other commands). Check [Enrico Giampieri's slides](https://unibodifabiophysics.github.io/programmingCourseDIFA/Lesson_03_version_control.slides.html#/21) for other info.
