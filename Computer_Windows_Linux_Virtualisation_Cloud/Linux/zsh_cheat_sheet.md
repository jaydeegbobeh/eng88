# zsh Command cheat sheet

- **pwd** print working directory

- **ls** list directory contents
	- Options: -a -l
	- ls -a : shows all files/directories within a directory
	- ls -l : prints as list
	- ls -la : prints all files/directories as list

- **./** current directory
- **../** parent directory of current directory

- **cd** change directory
	- cd ../ : change to parent directory

- **mkdir** create a directory

- **rm** remove files/directories
	- rm -r : allows you to recursively delete a directory and all its contents (rm usually only deletes empty directories)

- **type** find out if a command is builtin or an external binary file
	- type -t  : prints either alias, keyword, function, builtin, file

- **man** print manual or get help for a command
	- e.g man ls: shows info/options of ls

- **touch** creates a file
	- touch file_name

- **cat** read, create, concatenate files

- **nano** text editor

- **vi** file editor
	- vi file_name
	- exiting
		- :wq save and quit
		- :q quit
		- :q! quit without saving latest changes

- **echo** prints text to terminal windows
	- echo "Hello user" : prints Hello user in terminal
	- echo > file_name : allows you to edit file but replaces
	- echo >> file name : allows you to append a file

- **cp** copies files and directories
	- cp -r : copy everything inside directory recursively

- **mv** - move or rename directory

- **history** history of all commands

- **top** monitors processes and system resource usage

- **tree** displays the directory structure of a path (parent directory, current directory and sub directory)

- **top**

- **chmod** sets the file permissions flag on a file/folder

- **chown** change user and/or group ownerships of a file/directory

- **sudo** SuperUser Do : allows a normal user to execute commands with root privileges
	- sudo apt install package_name : install packages
	- sudo apt remove : remove packages
	- sudo cat /var/log/auth.log : view usage of authorisation systems
	- sudo more /var/log/auth.log : view as pages
	- sudo tail /var/log/auth.log : get tail of log file

- **. script_file.sh** runs scripts
