# Setup instructions (Python version, pip install commands)

For windows 11, vscode with anaconda already installed. If not, install vscode and anaconda first.

Configure the default terminal in vscode to launch conda terminal everytime.

CTRL+SHIFT+P in open search bar setting vscode, search "Preferences: Open User Settings (JSON)" and paste the following into the json file:

<pre>
"terminal.integrated.profiles.windows": {
  "Anaconda PowerShell": {
    "path": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
    "args": [
      "-NoExit",
      "-Command",
      "& 'C:\\ProgramData\\anaconda3\\shell\\condabin\\conda-hook.ps1'; conda activate base"
    ],
    "icon": "anaconda"
  }
},
"terminal.integrated.defaultProfile.windows": "Anaconda PowerShell"
</pre>
Save the json file and everytime you start terminal, it should launch conda terminal by default

Launch terminal inside vscode

Create virtual env by:

<pre>
conda create -n genai python=3.12

conda activate genai
</pre>
Then type 

<pre>
pip install -r requirements.txt
</pre> 

to install all the required packages

# How to create ~/.soonerai.env and required keys
Click on the "New File..." icon on the left side panel in vscode, then type in ".soonerai.env"

Then open the .soonerai.env and paste:

<pre>
SOONERAI_API_KEY=your_key_here
SOONERAI_BASE_URL=https://ai.sooners.us
SOONERAI_MODEL=gemma3:4b
</pre>

Get the API key by sign up and register with OU email at https://ai.sooners.us

Once logged in, click top right at the profile icon and click on Settings

Then click on Account

Look for API keys and click show

Copy the API keys over to the ".soonerai.env" file and replace the "your_key_here" with the API keys

# How to run the chatbot

run the script by typing 

<pre>
python spongebob_cli.py
</pre>
Type in anything to start chatting with spongebob

The history will keep track of the last 18 items in the list, so it will remember the last 9 full exchanges

To end the conversation, type "exit" or "quit"

# Example transcript (copy/paste 5–10 lines)
You: Do you know the direction to Mr. Krabs restaurant?
SpongeBob: (Voice bubbling with excitement and a tiny giggle)
Oh, barnacles, you want to go to the Krusty Krab?! Of course I do! It’s like, the BEST place in Bikini Bottom!
Well, you just keep swimmin’ straight ahead, past all the grumpy clams and the seaweed swirls – you’ll see a big red crab logo, and it’s right next to the best darn kelp shake stand in the whole ocean!  It's like, a *splash* of deliciousness!
Just follow your nose – you’ll smell the Krabby Patties a mile away!  Don’t be a jellyfish, keep swimmin’ and you’ll be there in a jiffy!      
(Giggles again)
Ooh, maybe I'll see you there!  Don't forget to order a Krabby Patty...it's like, a whole ocean of flavor!  Hehehe!

You: my favorite phrase is Mr. Krabs is a samurai. Thanks for the direction

SpongeBob: (Eyes widen with delight, bouncing excitedly)
Mr. Krabs is a samurai?! Oh, you *have* to tell him! That’s the bestest thing I’ve ever heard! He’d be so thrilled!
(Rapidly gesticulating)
It’s absolutely brilliant! A samurai Krabs!  He’d be swinging his spatula like a katana, defending the Krabby Patties with all his might!  It’s like… a *wave* of awesome!
(Giggles uncontrollably)
You know, maybe he *is* a samurai!  He's got that grumpy, focused look, and he's *always* protecting his treasure!  It’s like… a *current* of pure genius!
(Beaming)
You’re a brilliant fellow!  Keep on swimmin’, and tell Mr. Krabs I said hello!  And maybe he'll give you a special discount – a *wave* of savings!  Hehehe!

You: do you remember my favorite phrase?

SpongeBob: (Eyes light up, practically bouncing with glee!)
Mr. Krabs is a samurai?! Oh, you *have* to tell him! That’s the bestest thing I’ve ever heard!
(Giggles uncontrollably)
You know, you said it! You said “Mr. Krabs is a samurai!” It’s like… a *current* of pure genius!  I was just thinking about it!  It’s absolutely fantastic!
(Does a little happy wiggle)
You’re a brilliant fellow!  It’s stuck in my head now, I think!  It’s like… a *splash* of brilliantness!  Hehehe!
(Looks around excitedly)
Do you wanna order a Krabby Patty while we talk about Mr. Krabs being a samurai?!

You: exit