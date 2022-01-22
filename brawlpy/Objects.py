
class Player:
    def __init__(self,name,tag,nameColor,icon_id,trophies,expLevel,expPoints,club,highestTrophies,soloVictories,duoVictories,teamVictories,bestRoboRumbleTime,bestTimeAsBigBrawler,brawlers):
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

    def __repr__(self):
        return "<Player name='{0.name}' tag='{0.tag}'>".format(self)

    def __str__(self):
        return "{0.name} ({0.tag})".format(self)

class Club:
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
    def __init__(self,name,icon_id,tag,role,nameColor):
        self.name = name
        self.icon_id = icon_id
        self.tag = tag
        self.role = role
        self.nameColor = nameColor
    
    def __repr__(self):
        return "<ClubMember name='{0.name}' tag='{0.tag}' role='{0.role}'>".format(self)

    def __str__(self):
        return "{0.name} ({0.tag}) => {0.role}".format(self)


class ClubRanking:
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
        return "{0.name} ({0.tag})".format(self)


class BrawlerRanking:
    def __init__(self,brawler,playerTag,playerName,playerNameColor,playerIconID,rank,clubName):
        self.brawler = brawler
        self.playerTag = playerTag
        self.playerName = playerName
        self.playerNameColor = playerNameColor
        self.playerIconID = playerIconID
        self.rank = rank
        self.clubName = clubName

    def __repr__(self):
        return "<Player name='{0.name}' tag='{0.tag}' rank={0.rank} brawler={0.brawler}>".format(self)

    def __str__(self):
        return "{0.rank}. {0.name} ({0.tag}) => {0.brawler}".format(self)

class Event:
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
    def __init__(self,name,id,starPowers,gadgets):
        self.name = name
        self.id = id
        self.starPowers = starPowers
        self.gadgets = gadgets
    
    def __repr__(self):
        return "<Brawler name='{0.name}' id='{0.id}'>".format(self)

    def __str__(self):
        return "{0.name} ({0.id})".format(self)

class PlayerBrawler:
    def __init__(self,name,id,power,rank,highestTrophies,gadgets,gears,starPowers):
        self.name = name
        self.id = id
        self.power = power
        self.rank = rank
        self.highestTrophies = highestTrophies
        self.gadgets = gadgets
        self.gears = gears
        self.starPowers = starPowers
    
    def __repr__(self):
        return "<Brawler name='{0.name}' rank={0.rank} trophies={0.trophies}>".format(self)

    def __str__(self):
        return "{0.name} ({0.player})".format(self)


class Gadget:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def __repr__(self):
        return "<Gadget name='{0.name}' id='{0.id}'>".format(self)

    def __str__(self):
        return "{0.name} ({0.id})".format(self)

class StarPower:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def __repr__(self):
        return "<StarPower name='{0.name}' id='{0.id}'>".format(self)

    def __str__(self):
        return "{0.name} ({0.id})".format(self)

class Gear:
    def __init__(self,name,id,level):
        self.name = name
        self.id = id
        self.level = level
    
    def __repr__(self):
        return "<Gear name='{0.name}' id='{0.id}' level={0.level}>".format(self)
    
    def __str__(self):
        return "level {0.level} gear {0.name} ({0.id})".format(self)