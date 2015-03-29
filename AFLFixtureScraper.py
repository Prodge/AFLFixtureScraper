'''
Author: Prodge
    prodge.net
    https://github.com/Prodge

Scrapes the afl.com.au website for fixtures for a given season

nextGame() Moves to the start of a game listing, 
getHome() Returns the next instance of a home team
getAway() Returns the next instance of an away team

Calling all 3 in succession repeatedly will scan a whole page

main() Iterates through urls getting all the rounds

'''

import urllib2

global html

def nextGame():
    global html
    gameDiv = '<div class="team-names">'
    end = '</tbody>'
    for i in range(len(html)):
        if html[i:i+len(gameDiv)] == gameDiv:
            html = html[i+len(gameDiv):]
            return True 
        if html[i:i+len(end)] == end:
            return False

def getHome():
    global html
    home = '<span class="home"><span class="team">'
    for i in range(len(html)):
        if html[i:i+len(home)] == home:
            html = html[i+len(home):]
            break
    end = ' v</span>'
    for j in range(len(html)):
        if html[j:j+len(end)] == end:
            return html[:j]

def getAway():
    global html
    home = '<span class="away"><span class="team">'
    for i in range(len(html)):
        if html[i:i+len(home)] == home:
            html = html[i+len(home):]
            break
    end = '</span>'
    for j in range(len(html)):
        if html[j:j+len(end)] == end:
            return html[:j]

def main():
    global html
    maxNumGames = 9
    numRounds = 23
    year = 2015
    for x in range(numRounds):
        url = "http://www.afl.com.au/fixture?roundId=CD_R" + str(year) + "014" + str("%02d" % (x+1)) + "#tround"
        page = urllib2.urlopen(url)
        html = page.read()
        print('\n\nRound ' + str(x+1) + ':')
        for i in range(maxNumGames):
            if not nextGame():
                continue 
            home = getHome()
            away = getAway()            
            print('Game: ' + str(i+1) + '   Home: ' + home + '\n          Away: ' + away)

main()
