from pychatgpt import Chat
import sys
import subprocess
import dotenv
import os

dotenv.load_dotenv()

args = sys.argv[1]
args = "Write a one line bash command for: " + args

# Initializing the chat class will automatically log you in, check access_tokens
chat = Chat(email=os.getenv("email"), password=os.getenv("password"))
answer = chat.ask(args)

# parsing input to only get the command within ```
try:
	answer = answer.split("```")[1].strip()
except:
	answer  = answer.split("\n")[-1].strip()

subprocess.run("pbcopy", text=True, input=answer)
print("Copied to clipboard: " + answer)

