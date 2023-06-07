# Load appropriate packages 

import instaloader
import tkinter as tk
from tkinter import simpledialog


'''root.geometry("800x500")
root.title("Who unfollowed you?")


label = tk.Label(root, text="Who unfollowed you?", font=('Arial', 18))
label.pack(padx=20, pady=20)

'''

# Get username and password from user
username = simpledialog.askstring(title="Username",
                                   prompt="Enter username:")


pw = simpledialog.askstring(title="Password",
                                    prompt="Enter password:")


Loader = instaloader.Instaloader()
Loader.login(username,pw)

profile = instaloader.Profile.from_username(Loader.context, user_name)

follower_list = []
following_list = []

# Get list of accounts that follower the user

for follower in profile.get_followers():
    follower_list.append(follower.username)
    
# Get list of accounts followed by the user 
for followee in profile.get_followees():
    following_list.append(followee.username)
    

d = []

# Search for accounts that are followed by the user, but do not follow the user back
for x in following_list:
    if x not in follower_list:
        d.append(x)
        
        
root = tk.Tk()

# Show final list graphically

list_display = tk.Listbox(root)

for i,j  in enumerate(d):
    list_display.insert(i, j)
    
list_display.pack()


root.mainloop()
