def show_help(msg_args):
    
    help_msg = """
**Commands:**
Invite email to plex
```!invite persons.email@gmail.com```
Request movie or tv show (enter name exactly the same as it shows up on wikipedia basically)
```!request title of thing```
Show this help message
```!help```
"""
    
    return(help_msg)

def request(msg_args):
    if not msg_args:
        return("ERROR: Invalid Arguments")

    return("You requested: " + msg_args)

def invite(msg_args):
    if not msg_args:
        return("ERROR: Invalid Arguments")
    
    return("Invite sent to: " + msg_args)
