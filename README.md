# PDF Splitter

## Requirement
* PyPDF2
  
> ## Installation
* for Linux/macOS
  ```
  pip3 install PyPDF2
  ```
* For Windows
  ```
  pip install PyPDF2
  ```
## pip installation
pip comes with with python >=3.4 for windows. <b> So no need to install pip in windows.</b> 

For Linux -
 ```
 sudo apt install python3-pip
 ```
For MacOS - 
[See here](https://www.geeksforgeeks.org/how-to-install-pip-in-macos/)

## How to use splitter
For easy use you can copy pdf_splitter.py file to home directory.

Open terminal and run following command(If system have only python3)
```
python pdf_splitter.py pdf_file_path start_page end_page target_file_path
```

If system has both versions of python(python2 and python3) installed. Then run
```
python3 pdf_splitter.py pdf_file_path start_page end_page target_file_path
```
If target file path is not specified it will saved to default path.

This code is written on linux environment and default target path is set to 
``` 
/home/user/Documents
```
Users are advised to change default target path according to the choice/system.

### Note - If the number of inputs given less(target path may be or not specified) or invalid, you will encounter an error.