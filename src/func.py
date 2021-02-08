import os
import re
import tmdbsimple as tmdb
import settings
import dbtool


def show_help(msg):

    help_msg = """
**Commands:**
Invite an email to plex. If the email does not belong to an approved member of this discord server it will need to be manually approved. To invite friends please contact me.
```!invite persons.email@gmail.com```
Request a movie or TV show. The ID number (TMDB) can be found using the search command. If no ID is found enter the best description; doing so may increase the time to be added. 
```!request 7263```
Search for a movie or TV show
```!search Title of Thing```
Show this help message
```!help```
If something isn't working or you have any feedback let me know
```!feedback whats the problem is```
"""

    return(help_msg)


def search(msg):
    """Search for a movie or TV show and return the IDs and other info.
    """
    msg_args = " ".join(str(msg.content).split()[1:])
    if not msg_args:
        return("ERROR: Invalid Arguments")

    # Max results to show
    max_res = 5

    tmdb.API_KEY = settings.TMDB_TOKEN
    search = tmdb.Search()

    # Search Movies
    response = search.movie(query=msg_args)
    reply = "Movie results for " + msg_args + "\n"
    for s in search.results[:max_res]:
        reply = reply + \
            s['title'] + " (" + s['release_date'].split('-')[0] + \
            ") " + "ID: " + str(s['id'])
        reply = reply + "\n"

    # Search TV
    response = search.tv(query=msg_args)
    reply = reply + "\nTV results for " + msg_args + "\n"
    for s in search.results[:max_res]:
        reply = reply + \
            s['name'] + " (" + s['first_air_date'].split('-')[0] + \
            ") " + "ID: " + str(s['id'])
        reply = reply + "\n"

    return(reply)


def request(msg):

    msg_args = " ".join(str(msg.content).split()[1:])
    msg_auth = str(msg.author)

    if not msg_args:
        return("ERROR: Invalid Arguments")

    tmdb.API_KEY = settings.TMDB_TOKEN

    title = msg_args
    id = -999 # -999 = NA

    # Find movie info if ID is given
    if (msg_args.isnumeric()):
        print("Is Numeric")
        id = int(msg_args)
        m = tmdb.Movies(id)
        r = m.info()
        title = m.title

    # Log the request. The downloader indexes this database.
    #dbtool.log_request(title, str(id), msg_auth)
    print(title + ":" + str(id) + ":" + msg_auth)

    return("You requested: " + title)


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
