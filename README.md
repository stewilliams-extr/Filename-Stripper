# Filename-Stripper

This is a simple script that will rename all files in a directory and strip out some of the file name you dont want.  Enjoy!

File: [rename.py](rename.py)

**Example:**
Removing "-junk" from filenames.
```
strip@PC:~/strip$ ls -la
total 0
drwxr-xr-x 1 root root 4096 Dec  3 09:48 .
drwxr-xr-x 1 root root 4096 Dec  3 09:47 ..
-rw-r--r-- 1 root root    0 Dec  3 09:47 happy-file1-junk.file
-rw-r--r-- 1 root root    0 Dec  3 09:47 happy-file2-junk.file
-rw-r--r-- 1 root root    0 Dec  3 09:47 happy-file3-junk.file

strip@PC:~/strip$ python ~/rename.py
What string would you like to remove (Use "quotes if there is a space".)? -junk


Commands to be executed:
mv "happy-file1-junk.file" "happy-file1.file"
mv "happy-file2-junk.file" "happy-file2.file"
mv "happy-file3-junk.file" "happy-file3.file"

Would you like to continue (y/n)? y
strip@PC:~/strip$ ls -la
total 0
drwxr-xr-x 1 root root 4096 Dec  3 09:50 .
drwxr-xr-x 1 root root 4096 Dec  3 09:47 ..
-rw-r--r-- 1 root root    0 Dec  3 09:47 happy-file1.file
-rw-r--r-- 1 root root    0 Dec  3 09:47 happy-file2.file
-rw-r--r-- 1 root root    0 Dec  3 09:47 happy-file3.file
strip@PC:~/strip$
```
