# ChatGPT-Terminal-Completion
Attempt at using ChatGPT to issue commands based on comments in the terminal. (Python 3.9+)

Supports MacOS, uses pbcopy to copy to clipboard

Implements `how` command for querying ChatGPT.

![ezgif-2-e5baff6ad3](https://user-images.githubusercontent.com/49484385/206848258-bc43d529-3ec2-4a85-856d-4704fc84327b.gif)

## Setup
1. Install python packages using `pip3 install -r requirements.txt`
2. Put the function in script.sh to your bashrc/zshrc configuration file.
3. Replace the path in the function with the path to your python file.
4. Make a new .env file in the python file directory with your email and password formatted like
5. That should be everything

``` 
export EMAIL=email_chatgpt
export PWD=your_password
git clone git@github.com:MahdeenSky/ChatGPT-Terminal-Completion.git ~/.chatgpt_completion
cd ~/.chatgpt_completion
pip3 install -r requirements.txt
cat script.sh|sed -r "s|\"Directory of the script\"|`pwd`|g" >>~/.${SHELL##*/}rc
echo "email=${EMAIL}" >> .env
echo "password=${PWD}" >> .env
source ~/.${SHELL##*/}rc
```


## Support
For linux, an alternate copy to clipboard command is to use `xsel` or `xclip`
and replacing the current copy command with said commands.

## Reference
https://github.com/acheong08/ChatGPT
