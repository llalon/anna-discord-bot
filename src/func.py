import os
import re
import tmdbsimple as tmdb
import settings
import dbtool


def show_help(msg):

    help_msg = """
    **Commands:**
    Invite email to plex
    ```!invite persons.email@gmail.com```
    Request movie or tv show (enter name exactly the same as it shows up on wikipedia basically)
    ```!request title of thing```
    Search for a movie or TV show
    ```!search search term```
    Show this help message
    ```!help```
    If something isnt working let me know using
    ```!issue whats the problem is```
    """

    return(help_msg)


def search(msg):
    """Search for a movie or TV show and return the IDs and other info.
    """

    msg_args = " ".join(str(msg.content).split()[1:])

    if not msg_args:
        return("ERROR: Invalid Arguments")

    tmdb.API_KEY = settings.TMDB_TOKEN
    search = tmdb.Search()
    response = search.movie(query=msg_args)

    reply = ""

    for s in search.results:
        reply = reply + \
            s['title'] + " (" + s['release_date'].split('-')[0] + \
            ") " + "ID: " + str(s['id'])
        reply = reply + "\n"

    if reply == "":
        return("ERROR: Movie not found.")

    return("Search results for " + msg_args + ":\n" + reply)


def request(msg):

    msg_args = " ".join(str(msg.content).split()[1:])
    msg_auth = str(msg.author)

    title = msg_args
    id = -999

    if not msg_args:
        return("ERROR: Invalid Arguments")

    # Log the request
    dbtool.log_request(msg_args, id, msg_auth)

    return("You requested: " + msg_args)


def invite(msg):

    msg_args = " ".join(str(msg.content).split()[1:])

    reg = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if not msg_args:
        return("ERROR: Invalid Arguments")
    elif not (re.search(reg, msg_args)):
        return("Oops! Invalid E-mail")
    else:
        # TODO: Invite email to plex here
        pass

    return("Invite sent to: " + msg_args)


def send_feedback(msg):

    msg_args = " ".join(str(msg.content).split()[1:])

    return("Thanks for your feedback!")
