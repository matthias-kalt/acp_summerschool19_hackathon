class Worksheet(object):

    def __init__(self, id, importance=0, mandatory=False, workcenter=None, duration=1,
                 earliest_start=None, latest_start=None, activities=[]):
        self.id = id
        self.importance = importance
        self.mandatory = mandatory,
        self.workcenter = workcenter,
        self.duration = duration
        self.earliest_start = earliest_start
        self.latest_start = latest_start
        self.activities = activities

    def __str__(self):
        return f"Workcenter(ID {self.id})\nImportance: {self.importance}\nMandatory: {self.mandatory}\nDuration: {self.duration}"


class Activity(object):

    def __init__(self, id, worksheet, workers_needed=None, affected_road=None):
        self.id = id
        self.worksheet = worksheet
        self.workers_needed = workers_needed
        self.affected_road = affected_road

    def __str__(self):
        return f"Activity(ID {self.id})\nwithin Worksheet ID {self.worksheet.id}\nAffected road: {self.affected_road}\nWorkers needed: {self.workers_needed}"


class Road(object):

    def __init__(self, id, pertubation=None):
        self.id = id
        self.pertubation = pertubation

    def __str__(self):
        return f"Road(ID {self.id})\nPertubation {self.pertubation}"


class Workcenter(object):

    def __init__(self, id, number_of_workers):
        self.id = id
        self.number_of_workers = number_of_workers

    def __str__(self):
        return f"Workcenter(ID {self.id})\nNumber of workers available per day: {self.number_of_workers}"


class ProblemInstance(object):

    def __init__(self, filename, output_filename=None):

        self.filename = filename
        self.output_filename = output_filename if output_filename else filename + ".sol"

        number_of_days, worksheets, roads, workcenters, max_roads_blocked, precendence_relations = read_data(filename)
        self.number_of_days = number_of_days
        self.worksheets = worksheets
        self.roads = roads
        self.workcenters = workcenters
        self.max_roads_blocked = max_roads_blocked
        self.precendence_relations = precendence_relations

    def __str__(self):
        return f"Problem instance read from {self.filename} - output in {self.output_filename}"
