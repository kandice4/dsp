# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > 
> > * show current working directory path `pwd`
> > * creating a directory `mkdir <new dir name>`
> > * deleting a directory `rmdir <dir name>` (must be in the parent directory; directory must be empty)
> > * creating a file using `touch` command `touch <new file name>`
> > * deleting a file `rm <file name>`
> > * renaming a file `mv <old file name> <new file name>`
> > * listing hidden files `ls -a`
> > * copying a file from one directory to another `cp <old dir>/<file name> <new dir>`
> > * move up to parent directory `cd ..`
> > * move to home directory `cd ~`
> > * save link to current directory and change directory `pushd <dir name>`
> > * return to the previously saved directory in pushd `popd`
---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> >`ls`  list the visible files and folders in the current directory  
> >`ls -a`  list all files including hidden files in the current directory  
> >`ls -l`  list the long form of files and folders (adds detailed columns such as owner, size, date modified, etc)  
> >`ls -lh`  same as previous except changes the size to "human readable" MB or GB  
> >`ls -lah`  same as previous except includes hidden files  
> >`ls -t`   sorts the list by modified time  
> >`ls -Glp` includes details but omits group names and adds slash to end of directories  

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > `ls -R` recursivly list all sudirectories  
> > `ls -r` reverse the order of the list  
> > `ls -S` sort descending by size  
> > `ls -m` displays as a comma separated list  
> > `ls -1` displays one entry per line  

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` allows you to build and execute code from standard input  
> > for example: executing `xargs find -name` will then prompt for input  
> > input: `*.txt` then `Ctrl-D` and it will be passed to the find command  

 

