
class Player:
    def __init__(self,name,tag,nameColor,icon_id,trophies,expLevel,expPoints,club,highestTrophies,soloVictories,duoVictories,teamVictores,bestRoboRumbleTime,bestTimeAsBigBrawler,brawlers):
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
        self.teamVictores = teamVictores
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
