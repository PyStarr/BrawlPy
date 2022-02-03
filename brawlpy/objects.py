import os
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

class Player:

    """
    Player object with all its attribute

    name - The Name of the player
    tag - The Tag of the player
    nameColor - The Color of the name of the player
    icon_id - The ID of the player's icon
    trophies - The Trophies of the player
    highestTrophies - The Highest Trophies the player ever reached
    soloVictories - The number of Solo-Showdown matches the player has won
    duoVictories - The number of Duo-Showdown matches the player has won
    teamVictories - The number of 3 vs 3 matches the player has won
    bestTimeAsBigBrawler - The Player's best time as being the big brawler
    bestRoboRumbleTime - The Player's best time in Robo-Rumble mode
    brawlers - A list of all the brawlers the player has
    club - The club that the player is in
    """

    def __init__(self,name,tag,nameColor,icon_id,trophies,expLevel,expPoints,club,highestTrophies,soloVictories,duoVictories,teamVictories,bestRoboRumbleTime,bestTimeAsBigBrawler,brawlers,battleLog):
        self.name = name
        self.tag = tag
        self.nameColor = nameColor
        self.icon_id = icon_id
        self.trophies = trophies
        self.expLevel = expLevel
        self.expPoints = expPoints
        self.highestTrophies = highestTrophies
        self.soloVictories = soloVictories
        self.duoVictories = duoVictories
        self.teamVictories = teamVictories
        self.bestTimeAsBigBrawler = bestTimeAsBigBrawler
        self.bestRoboRumbleTime = bestRoboRumbleTime
        self.brawlers = brawlers
        self.club = club
        self.battleLog = battleLog

    def __repr__(self):
        return "<Player name='{0.name}' tag='{0.tag}'>".format(self)

    def __str__(self):
        return "{0.name} ({0.tag})".format(self)

class Club:

    """
    Club object with all its attribute

    name - The Name of the club
    tag - The Tag of the club
    description - The Description of the club
    type - The Type of the club (inviteOnly,closed,open)
    badgeID - The Badge ID of the club
    requiredTrophies - The amount of trophies required to join the club
    members - A list a all the members of the club
    """

    def __init__(self,tag,name,description,type,badgeID,requiredTrophies,trophies,members):
        self.tag = tag
        self.name = name
        self.description = description
        self.type = type
        self.badgeID = badgeID
        self.requiredTrophies = requiredTrophies
        self.trophies = trophies
        self.members = members

    def __repr__(self):
        return "<Club name='{0.name}' tag='{0.tag}'>".format(self)

    def __str__(self):
        return "{0.name} ({0.tag})".format(self)

class ClubMember:

    """
    ClubMember object with all its attribute

    name - The Name of the member
    tag - The Tag of the member
    icon_id - The ID of the player's icon
    role - The role of the member (president,vicePresident,senior,member)
    nameColor - The color of their name
    trophies - The total trophies of the member
    """

    def __init__(self,name,icon_id,tag,role,nameColor,trophies):
        self.name = name
        self.icon_id = icon_id
        self.tag = tag
        self.role = role
        self.nameColor = nameColor
        self.trophies = trophies
    
    def __repr__(self):
        return "<ClubMember name='{0.name}' tag='{0.tag}' role='{0.role}'>".format(self)

    def __str__(self):
        return "{0.name} ({0.tag}) => {0.role}".format(self)


class ClubRanking:

    """
    ClubRanking object with all its attribute

    name - The Name of the Club
    tag - The Tag of the Club
    badgeID - The ID of the club's badge
    trophies - The Trophies of the club
    rank - The rank of the Club
    memberCount - The amount of the member the club has
    """

    def __init__(self,tag,name,badgeID,trophies,rank,memberCount):
        self.tag = tag
        self.name = name
        self.badgeID = badgeID
        self.trophies = trophies
        self.rank = rank
        self.memberCount = memberCount

    def __repr__(self):
        return "<Club name='{0.name}' tag='{0.tag}' rank={0.rank}>".format(self)

    def __str__(self):
        return "{0.rank}. {0.name} ({0.tag})".format(self)

class PlayerRanking:

    """
    PlayerRanking object with all its attribute

    name - The Name of the player
    tag - The Tag of the player
    nameColor - The Color of the name of the player
    icon_id - The ID of the player's icon
    trophies - The Trophies of the player
    rank - The rank of the player
    clubName - The name of the club the player is in
    """

    def __init__(self,name,tag,nameColor,icon_id,trophies,rank,clubName):
        self.name = name
        self.tag = tag
        self.nameColor = nameColor
        self.icon_id = icon_id
        self.trophies = trophies
        self.rank = rank
        self.clubName = clubName

    def __repr__(self):
        return "<Club name='{0.name}' tag='{0.tag}'>".format(self)

    def __str__(self):
        return "{0.rank}. {0.name} ({0.tag})".format(self)


class BrawlerRanking:

    """
    BrawlerRanking object with all its attribute

    brawler - The brawler that the player pushed (I couldn't think of any other description lol)
    playerName - The Name of the player
    playerTag - The Tag of the player
    playerNameColor - The color of the player's name
    playerIconID - The ID of the player's icon
    trophies - The Trophies of the player
    rank - The rank of the player
    clubName - The Name of the player's Club
    """

    def __init__(self,brawler,playerTag,playerName,playerNameColor,playerIconID,trophies,rank,clubName):
        self.brawler = brawler
        self.playerTag = playerTag 
        self.playerName = playerName
        self.playerNameColor = playerNameColor
        self.playerIconID = playerIconID
        self.trophies = trophies
        self.rank = rank
        self.clubName = clubName

    def __repr__(self):
        return "<Player name='{0.playerName}' tag='{0.playerTag}' rank={0.rank} brawler={0.brawler}>".format(self)

    def __str__(self):
        return "{0.rank}. {0.playerName} ({0.playerTag}) => {0.brawler}".format(self)

class Event:

    """
    Event object with all its attribute

    id - The event ID
    mode - The mode of the event
    map - The map currently in rotation
    startTime - The time when the event got in rotation
    endTime - The time when the event will be out of rotation
    """

    def __init__(self,id,mode,map,startTime,endTime):
        self.id = id
        self.mode = mode
        self.map = map
        self.startTime = startTime
        self.endTime = endTime
    
    def __repr__(self):
        return "<Event mode='{0.mode}' map='{0.map}' id={0.id}>".format(self)

    def __str__(self):
        return "{0.mode} => {0.map} ({0.id})".format(self)

class Brawler:

    """
    Brawler object with all its attribute

    name - The name of the brawler
    id - The ID of the brawler
    icon_url = The URL of the brawler's icon
    starPowers - A list of all the starPowers the brawler has
    gadgets - A list of all the gagdets the brawler has
    """

    def __init__(self,name,id,starPowers,gadgets):
        self.name = name
        self.id = id
        self.starPowers = starPowers
        self.icon_url = self.get_icon_url()
        self.gadgets = gadgets
    
    def __repr__(self):
        return "<Brawler name='{0.name}' id='{0.id}'>".format(self)

    def __str__(self):
        return "{0.name} ({0.id})".format(self)

    def get_icon_url(self):

        with open(os.path.join(__location__, "brawler_icons.json")) as icons:
            data = json.load(icons)

        return data[str(self.id)]

class PlayerBrawler:

    """
    PlayerBrawler object with all its attribute

    name - The name of the brawler
    id - The ID of the brawler
    icon_id - The ID of the brawler's icon
    power - The power level of the brawler
    trophies - The amount of trophies the player has on the brawler
    highestTrophies - The highest amount of trophies the player ever had on the brawler
    gadgets - A list of all the gadgets the player has on this brawler
    startPowers - A list of all the star powers the player has on this brawler
    gears - A list of all the gears the player has on this brawler
    """

    def __init__(self,name,id,power,rank,trophies,highestTrophies,gadgets,gears,starPowers):
        self.name = name
        self.id = id
        self.icon_id = self.get_icon_url()
        self.power = power
        self.rank = rank
        self.trophies = trophies
        self.highestTrophies = highestTrophies
        self.gadgets = gadgets
        self.gears = gears
        self.starPowers = starPowers
    
    def __repr__(self):
        return "<Brawler name='{0.name}' rank={0.rank} trophies={0.trophies}>".format(self)

    def __str__(self):
        return "{0.name} ({0.id})".format(self)

    def get_icon_url(self):

        with open(os.path.join(__location__, "brawler_icons.json")) as icons:
            data = json.load(icons)

        return data[str(self.id)]


class Gadget:
    
    """
    Gadget object with all its attribute

    name - The name of the gadget
    id - The ID of the gadget
    """

    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def __repr__(self):
        return "<Gadget name='{0.name}' id='{0.id}'>".format(self)

    def __str__(self):
        return "{0.name} ({0.id})".format(self)

class StarPower:
    
    """
    StarPower object with all its attribute

    name - The name of the star power
    id - The ID of the star power
    """

    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def __repr__(self):
        return "<StarPower name='{0.name}' id='{0.id}'>".format(self)

    def __str__(self):
        return "{0.name} ({0.id})".format(self)

class Gear:
    
    """
    Gear object with all its attribute

    name - The name of the gear
    id - The ID of the gear
    level - The level of the gear
    """

    def __init__(self,name,id,level):
        self.name = name
        self.id = id
        self.level = level
    
    def __repr__(self):
        return "<Gear name='{0.name}' id='{0.id}' level={0.level}>".format(self)
    
    def __str__(self):
        return "level {0.level} gear {0.name} ({0.id})".format(self)
