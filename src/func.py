import os
import re
import tmdbsimple as tmdb
import settings
import dbtool


def show_help(msg):
    """ Shows this Help message
    """

    help_msg = """
**Commands:**
Invite an email to plex. If the email does not belong to an approved member of this discord server it will need to be manually approved. To invite friends please contact me.
```!invite persons.email@gmail.com```
Request a movie or TV show. Enter the Movie/TV series title as it appears on The Movie Database, or the best description. To speed up matching use the optional flags - "--movie (--tv, --anime), and --id"
```!request Title of Thing```
```!request --movie --id 3847```
Search for a movie or TV show. To show more results than the top 5 use the optional flag --all
```!search [--all] Title of Thing```
Show this help message
```!help```
Show leaderboard
```!top```
If something isn't working or you have any feedback let me know
```!feedback whats the problem is```
"""

    return(help_msg)


def leader_board(msg):
    """Sows the leaderboard of suggestions
    """

    # Todo get this data from the db
    reply = "The users with the best taste are:\n1. LeMonkey\n2. Wilbus\n3. Mtat"

    return(reply)


def search(msg):
    """Searches for a movie or tv. Discord arguments are '--all'
    """

    msg_args = " ".join(str(msg.content).split()[1:])
    if not msg_args:
        return("ERROR: Invalid Arguments")

    if ('--all' in msg_args):
        max_res = 999
        title = re.compile('(\s*)--all(\s*)').sub('', msg_args)
    else:
        max_res = 5
        title = msg_args

    tmdb.API_KEY = settings.TMDB_TOKEN
    search = tmdb.Search()

    # Search Movies
    response = search.movie(query=title)
    reply = "Movie results for " + title + "\n"
    for s in search.results[:max_res]:
        reply = reply + \
            s['title'] + " (" + s['release_date'].split('-')[0] + \
            ") " + "ID: " + str(s['id'])
        reply = reply + "\n"

    # Search TV
    response = search.tv(query=title)
    reply = reply + "\nTV results for " + title + "\n"
    for s in search.results[:max_res]:
        reply = reply + \
            s['name'] + " (" + s['first_air_date'].split('-')[0] + \
            ") " + "ID: " + str(s['id'])
        reply = reply + "\n"

    return(reply)


def request(msg):
    """Makes a request. Discord arguments are --id, --movie, --tv
    """

    msg_args = " ".join(str(msg.content).split()[1:])
    msg_auth = str(msg.author)

    if not msg_args:
        return("ERROR: Invalid Arguments")

    title = msg_args
    id = -999

    if (msg_args.isnumeric()):
        id = int(msg_args)

    # Log the request
    dbtool.log_request(msg_args, id, msg_auth)

    return("You requested: " + msg_args)


def invite(msg):
    """Sends a plex invite to the email
    """

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
    """Logs feedback
    """

    msg_args = " ".join(str(msg.content).split()[1:])

    return("Thanks for your feedback!")
