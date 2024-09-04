# example-of-debian-package

Basic example of how to create a debian package with a simple Pyhton program. Basic preinst, postint and control file.  <br>

``` git clone https://github.com/Yun-Veronica/example-of-debian-package.git ```- to clone the repo.<br>
``` sudo dpkg -i  example-of-debian-package/my-program.deb ``` - to install.<br>
``` my_program ```- to run.<br>

in case you will need to pack it again: ```dpkg-deb --build /home/user/example-of-debian-package/my-program ```.<br>
