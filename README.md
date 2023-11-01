# python_variable_replacer
This python script is used to replace the variable names of a powershell script, the reasons for this is to make the script undetectable. The script will get the variable that starts with "$" and it would change it to random consisten letters which would lower the entropy of the script. However this alone will not pypass the AV, nore changes to the script are needed. 
-----------------------------------
You will need to download the py file and run it in a ide and replace the sample script with your script. You can easily change the python script to get the user input, but i preffer to do it this way
---------------------------------------

Keep in mind that you can make changes to the script however you want to suit your prefferences. 

--------------------------------------------------------------------------------------------------------------

## Usage 

```
git clone https://github.com/Illyr14n/python_variable_replacer
cd python_variable_replacer
python3 undetect.py
```

Inspired by @t3l3machus
