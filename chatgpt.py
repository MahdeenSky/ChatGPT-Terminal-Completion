from pychatgpt import Chat
import sys
import subprocess
import dotenv
import os
import re

dotenv.load_dotenv()

args = sys.argv[1]
args = "Write a one line bash command for this task: " + args
copy_command = "pbcopy"

email = os.getenv("email")
password = os.getenv("password")

# Initializing the chat class will automatically log you in, check access_tokens
chat = Chat(email, password)
answer, previous_convo_id, convo_id = chat.ask(args)

	# regex to get the one line bash command between the ``` and ```
test = re.search(r"(```\n)(.*)(\n```)", answer)
if test:
	answer = test.group(2)
	print("Copied to clipboard:  " + answer)
else:
	print(f"Could not Parse answer:   \n{'-'*50}\n{answer}\n{'-'*50}")

subprocess.run(copy_command, text=True, input=answer)

