class Worksheet(object):

    def __init__(self, id, importance=0, mandatory=False,
                 costcenter=None, duration=1, earliest_start=None, latest_start=None,
                 activities=[]):
        self.id = id
        self.importance = importance
        self.mandatory = mandatory,
        self.costcenter = costcenter,
        self.duration = duration
        self.earliest_start = earliest_start
        self.latest_start = latest_start
        self.activities = activities


class Activity(object):

    def __init__(self, id, worksheet, workers_needed=None, affected_road=None):
        self.id = id
        self.worksheet = worksheet
        self.workers_needed = workers_needed
        self.affected_road = affected_road


class Road(object):

    def __init__(self, id, pertubation=None):
        self.id = id
        self.pertubation = pertubation


class Workcenter(object):

    def __init__(self, id, number_of_workers):
        self.id = id
        self.number_of_workers = number_of_workers
