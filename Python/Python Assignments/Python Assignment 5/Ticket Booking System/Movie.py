from Events import Event

class Movie(Event):
    def __init__(self, Event, Genre, ActorName, ActressName):
        self.event = Event
        self.genre = Genre
        self.actorName = ActorName
        self.actressName = ActressName

    @property
    def getname(self):
        return self.event.event_name

    @getname.setter
    def setname(self, name):
        self.event.event_name = name

