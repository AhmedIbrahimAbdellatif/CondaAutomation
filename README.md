# Conda Automation

### Motivation

> When you want to install a python package using anaconda, you might not know the correct command or the correct package name. 
>
> If you're working on a project frequently, interrupting your work on the code to search for the command on the internet can be a little distracting.
>
> So this python script automates this boring stuff. It searches for the correct package name and gives you alternative commands if found.

***

### Used Technologies

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white)

***

### What does this script do? & How to use it ?

1. It takes from the user two arguments, one for the conda environment `-e` and another for the package name `-p`

   > *Package name doesn't have to be exact*

   - Example:

     <img src=".\pics\1.png">

   - **<u>NB:</u>** You can also use  `-h` to see the command structure

2. The script does the search for you and finds results on google for how to install this package using conda

3. If this package can be installed by conda and is officially documented on `anaconda.org` then this script parses the `anaconda.org` web page and gets all the correct commands for installing it

4. You're prompted by the found commands sequentially (adding to them your provided conda environment and -y option) and you either accept the command to be executed or reject it by typing (`y` or `n`)

   - Example

     <img src=".\pics\2.png">

***

