# CodeBlocks-Arduino (version: 1.0b2)

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

1. A symlink to your Arduino directory. It must be named `arduino`. For example if your Arduino install is at: 
         
        /home/USER/bin/arduino1.0.3
    then use this command (from within `/home/USER/.codeblocks`):

        $ln -s /home/USER/bin/arduino1.0.3 arduino

2. A symlink to your Sketches directory. It must be named `sketches`. For example if your Sketches directory is at: 
         
        /home/USER/mySketches
    then use this command (from within `/home/USER/.codeblocks`):

        $ln -s /home/USER/mySketches sketches

3. Copy the `helpers` directory to the `codeblocks` folder (or 'symlink' it)

4. There should be the following folder path: 

        /share/codeblocks/templates/wizard
    If there is not, then create it. The copy the folder `/wizards/arduino` to the wizard folder.

5. Copy the `default.conf` file


When you are done, your data folder should look like the following:

        arduino -> /home/USER/bin/arduino-1.0.3
        sketches -> /home/USER/mySketches
        default.conf
        helpers
        share

The `/share/codeblocks/templates/wizard` folder should look like:

        arduino


###Instructions for Code::Blocks newer than version 10
When you try to create a new project, newer versions of Code::Blocks will not show the arduino wizard by default. The wizard must first be registered. To do so, select *New/Project* from the menu. Then right-click on any of the wizards. Select *Edit Global Registration Script*. Under the function `RegisterWizards()`, place this line:

        RegisterWizard(wizProject,     _T("arduino"),      _T("Arduino Project"),       _T("Embedded Systems"));

and save the file. It will be placed in your user wizard folder.

For further details, see - <http://wiki.codeblocks.org/index.php?title=Wizard_scripts>

##Using
###Creating an Arduino Project using the Wizard
1. Launch Code::Blocks. Select *New/Project* menu item. You should see *Arduino Project* in red. If you do not, then something in your installation is wrong.

2. Select *Arduino Project*. After the intro page, the next page will be where you configure your project. Most of the defaults are fine to use. If you are using a programmer instead of the Arduino bootloader to program your device, select the programmer you will be using. Also, now is the time to choose the serial port to use for uploading your code. 

    **TIP for serial port selection:**

    * For Usbasp programmers, choose ttyUSB0.
    * For Uno & Leonardo, choose ttyACM0 in most cases.
    * For all others, ttyUSB0 is a safe bet.

    **Note:**&nbsp;&nbsp;You can change/select the board from the *Build target* menu after finishing the wizard. The programmer and serial port remain the same for each board. They can be changed for individual boards after completing the wizard - see the *Modifying* section for details.

3. On the next page, creating a new project is pretty self-explanatory. If you are using an existing Arduino project, do the following:

    a. Select the folder to create project in - this will be your existing Arduino project folder

    b. Give it the project title - usually this will be the same as the folder name

    c. Edit the Resulting Filename box and remove the extra folder being created

###Tools Menu
Several tools are provided in the Tools menu. They are:

* Serial Terminal
* Upload Code
* Upload EEPROM
* Arduino-Make
* Arduino-Make (Clean)
* Arduino-Make (Upload)

####Serial Terminal Tool
This tool opens a serial comm window just like the ArduinoIDE. It does not close automatically before an upload, so if using the same serial port for uploading, you will need to close this window first.

####Upload Tools
If after compiling, you need to upload your code again, use the *Upload Code* tool. EEPROM data is not uploaded by default, so the *Upload EEPROM* tool is provided for that.

####Arduino-Make
These tools invoke the make function using command-line Arduino-Make tool(<https://github.com/sudar/Arduino-Makefile>). You must install this script and create your config file within your project folder before using. You can add your own additional make commands from the *Configure tools...* menu item in the *Tools* menu.

####GitG
This tool launches the GitG application for your project.


##Modifying
Sometimes you need to modify a project after creating it. For most settings, go to *Project/Build Options...*. You will find different sets of options for both the project and individual target devices. The two sets are merged at compile time (you can change this if desired), so you will need to check both when looking for configurations to change. Some common ones you might want to change are:

* Compiler Settings/#defines (project setting) - arduino version & what core libraries to include
* Custom Variables (device setting)
    - programmer protocol
    - upload port

You can select which board to compile and upload your program to by choosing from the *Build target* menu in the toolbar. This will change the appropriate upload settings, with the exception of the programmer used and the upload port. 

###Programmer
For Arduino boards with bootloaders, the correct programmer is already chosen. For other boards using a programmer, the one chosen in the wizard will be the one used. If it needs to be changed, then go to the *Project/Build options...* and select the correct *build target* and go to the *Custom Variables* tab. Edit the correct *PROTOCOL* there.

###Upload Port
The correct port varies across the boards. Different ISP programmers may have their own port. The Uno and Leonardo use a different port than their predecessors. If you have other devices sharing the same port labeling system plugged in, then the port number will change. 

In most cases, these values will work:

* Uno/Leonardo: &nbsp;&nbsp;ttyACM0 (because Leonardo connects & disconnects all the time, expect it to change from time to time, usually to ttyACM1 or ttyACM2.
* Usbasp programmers: &nbsp;&nbsp;ttyUSB0
* All others: &nbsp;&nbsp;ttyUSB0 is a safe bet.

To change the port for a board, then go to the *Project/Build options...* and select the correct *build target* and go to the *Custom Variables* tab. Edit the correct *UPLOAD_PORT* setting there.

 
##Known Issues
1. The method of linking used is not as efficient as the ArduinoIDE. No solution is known at present. In most projects it won't matter, but if a project is reaching the maximum flash memory point, it may be a problem.

2. Leonardo uploading is still problematic (and not recommended at this time), and automatic reset does not work. Sometimes uploading will put the Leonardo in an unresponsive state. The only way to revive it is to upload a sketch from the ArduinoIDE while pressing the reset button (sometimes it has to be done more than once).

3. Everything has been written and tested on Linux systems. Use on Windows systems may require some tweaking - Upload port selection and Tool menu settings.

##Future Plans
1. Fix known issues
2. Do more with command-line make tool?
3. Make sketch.cpp file more compatible with the ArduinoIDE sketch.ino file (eliminate the need for both) when using either IDE.

## Changelog
### 8/18/13 - directory includes improvements:

* Improved various directory includes:
    * The hardware directory for ATTiny support is now located in the sketches directory as per standard ArduinoIDE location. You can get support for most ATTiny chips here - <https://github.com/provideyourown/attiny.git>
    * The libraries directory for your sketches is now included by default. Libraries can now be included by name only without specifying a relative path - just like the ArduinoIDE.

### 1/17/13 - bug fixes; Tools menu changes:

* Tools Menu:
    * Generalized upload cmds to work with any target board
    * Added support for command-line make tool(<https://github.com/sudar/Arduino-Makefile>)
* Added -D option to avrdude for Arduino boards (must not be used for ATtinys)
* Removed default port selection (can't get it to work)
* Added more instruction to README file

###1/16/13 - changes to Stanley Huang's original code:

* Added size calculation to postprocessing steps to calculate both flash memory and SRAM.
* Fixed avrdude configuration to work with ATtiny
* Added support for Leonardo
* Added support for alternative configurations such as ATtiny boards
* Added support for ISP programmers for uploads
* Added support for Code::Blocks version 12
* Added tooltips to Wizard options







