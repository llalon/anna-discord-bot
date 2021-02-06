import os
import re
import tmdbsimple as tmdb
import APIKEY


def show_help(msg_args):

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


def search(msg_args):
    """Search for a movie or TV show and return the IDs and other info.
    """
    if not msg_args:
        return("ERROR: Invalid Arguments")

    tmdb.API_KEY = APIKEY.TMDB_TOKEN
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


def request(msg_args):
    if not msg_args:
        return("ERROR: Invalid Arguments")

    return("You requested: " + msg_args)


def invite(msg_args):
    reg = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if not msg_args:
        return("ERROR: Invalid Arguments")
    elif not (re.search(reg, msg_args)):
        return("Oops! Invalid E-mail")
    else:
        # TODO: Invite email to plex here
        pass

    return("Invite sent to: " + msg_args)


def send_feedback(msg_args):
    print(msg_args)
    return("Thanks for your feedback!")


# DEBUG
if __name__ == "__main__":
    request("Toy Story")
