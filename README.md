# CodeBlocks-Arduino (version: 0.9)

> &copy; 2012-2013 Scott Daniels (<http://provideyourown.com>)
> under GNU General Public License

> Portions are: &copy; 2012 Stanley Huang (<stanleyhuangyc@gmail.com>)
> under GNU General Public License


CodeBlocks-Arduino contains added functionality for Code::Blocks to allow Arduino software development. Code::Blocks is a more advanced IDE than the ArduinoIDE, yet is still fairly straightforward. When an Arduino project starts incorporating custom libraries, it often becomes too cumbersome for the ArduinoIDE. This package adds a custom project wizard for creating Arduino projects. The distribution also integrates the latest Arduino core files and libraries, AVR toolchains, avrdude for uploading, and a serial terminal.


##Features

* Dedicated project wizard for Arduino development
* Integrated Arduino core files and libraries
* Integrated pre-configured AVR compiler toolchain
* Integrated AVRDUDE for uploading (Flash and EEPROM) via USB or programmer
* Integrated serial terminal
* Various Arduino boards supported as build targets


##Installation

Certain files must be placed in the Code::Blocks' data folder. The following instructions apply to Linux computers. For other operating systems installations, contributions on how to do it are welcome - <http://provideyourown.com/contact>.

The data folder for CodeBlocks is located in: 

    /home/USER/.codeblocks

In this folder place:

1. A symlink to your Arduino directory. It must be named 'arduino'. For example if your Arduino install is at: 
         
        /home/bin/arduino1.0.1
    then use this command (from within /home/USER/.codeblocks):

        $ln -s /home/bin/arduino1.0.1 arduino

2. Copy the 'helpers' directory to the codeblocks folder (or symlink it)

3. There should be the following folder path: 

        /share/codeblocks/templates/wizard
    If there is not, then create it. The copy the folder '/wizards/arduino' to the wizard folder.

4. Copy the 'default.conf' file


When you are done, your data folder should look like the following:

        arduino -> /home/scott/bin/arduino-1.0.1
        default.conf
        helpers
        share

The '/share/codeblocks/templates/wizard' folder should look like:

        arduino


###Instructions for Code::Blocks newer than version 10
When you try to create a new project, newer versions of Code::Blocks will not show the arduino wizard by default. The wizard must first be registered. To do so, select *New/Project* from the menu. Then right-click on any of the wizards. Select 'Edit Global Registration Script'. Under the function *RegisterWizards()*, place this line:

        RegisterWizard(wizProject,     _T("arduino"),      _T("Arduino Project"),       _T("Embedded Systems"));

and save the file. It will be placed in your user wizard folder.

For further details, see - <http://wiki.codeblocks.org/index.php?title=Wizard_scripts>

##Using
1. Launch Code::Blocks. Select *New/Project* menu item. You should see 'Arduino Project' in red. If you do not, then something in your installation is wrong.

2. Select 'Arduino Project'. After the intro page, the next page will be where you configure your project. Most of the defaults are fine to use. If you are using a programmer instead of the Arduino bootloader to program your device, select the programmer you will be using. Also, now is the time to choose the serial port to use for uploading your code.

3. On the next page, creating a new project is pretty self-explanatory. If you are using an existing Arduino project, do the following:

    a. Select the folder to create project in - this will be your existing Arduino project folder

    b. Give it the project title - usually this will be the same as the folder name

    c. Edit the Resulting Filename box and remove the extra folder being created

##Modifying
Sometimes you need to modify a project after creating it. For most settings, go to *Project/Build Options...*. You will find different sets of options for both the project and individual target devices. The two sets are merged at compile time (you can change this if desired), so you will need to check both when looking for configurations to change. Some common ones you might want to change are:

* Compiler Settings/#defines (project setting) - arduino version & what core libraries to include
* Custom Variables (device setting)
    - programmer protocol
    - upload port
 
##Known Issues
1. The method of linking used is not as efficient as the ArduinoIDE. No solution is known at present. In most projects it won't matter, but if a project is reaching the maximum flash memory point, it may be a problem.

2. Supports Leonardo, but automatic reset does not work. You must press the reset button just before uploading the code.

3. Upload tools need to be generalized for ISP programmers

##Future Plans
1. Fix known issues
2. Add support for command-line make tool(<https://github.com/sudar/Arduino-Makefile>)  from the Tools menu

## Changelog
###1/16/13 - changes to Stanley Huang's original code:

* Added size calculation to postprocessing steps to calculate both flash memory and SRAM.
* Fixed avrdude configuration to work with ATtiny
* Added support for Leonardo
* Added support for alternative configurations such as ATtiny boards
* Added support for ISP programmers for uploads
* Added support for Code::Blocks version 12
* Added tooltips to Wizard options







