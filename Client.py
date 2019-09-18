from Date import *


class Client:
    '''
    This is a class to create a Client.

    Arguments:
        name {string} -- The name of the client.
        city {string} -- The city where the task was requested.
        date {string} -- The date when the task should be performed, in yyyy-mm-dd format.
        hour {string} -- The hour when the task should be performed, in hh:mm format.
        maxCost {string} -- The value that the client is willing to pay per hour.
        minReputation {string} -- The minimum reputation of the expert required, in n* format.
        domain {string} -- The domain of the expert required to complete the task.
        duration {string} -- The duration of the task, in HhMM format.

    '''

    def __init__(self, name, city, date, hour, maxCost, minReputation, domain, duration):
        '''
        The constructor for the Client class.

        Arguments:
            name {string} -- The name of the client.
            city {string} -- The city where the task was requested.
            date {string} -- The date when the task should be performed, in yyyy-mm-dd format.
            hour {string} -- The hour when the task should be performed, in hh:mm format.
            maxCost {string} -- The value that the client is willing to pay per hour.
            minReputation {string} -- The minimum reputation of the expert required, in n* format.
            domain {string} -- The domain of the expert required to complete the task.
            duration {string} -- The duration of the task, in HhMM format.

        '''

        self._name = name
        self._city = city
        self._date = date
        self._hour = hour
        self._maxCost = maxCost
        self._minReputation = minReputation
        self._domain = domain
        self._duration = duration

    # Getters
    @property
    def name(self):
        '''
        Gets the name of the client.

        Returns:
            string -- The name of the client.

        '''

        return self._name

    @property
    def city(self):
        '''
        Gets the name of the city where the task was requested.

        Returns:
            string -- The city where the task was requested.

        '''

        return self._city

    @property
    def date(self):
        '''
        Gets the date when the task should be performed.

        Returns:
            string -- The date when the task should be performed, in yyyy-mm-dd format.

        '''

        return self._date

    @property
    def hour(self):
        '''
        Gets the hour when the task should be performed.

        Returns:
            string -- The hour when the task should be performed, in hh:mm format.

        '''

        return self._hour

    @property
    def maxCost(self):
        '''
        Gets the value that the client is willing to pay per hour.

        Returns:
            string -- The value that the client is willing to pay per hour.

        '''

        return self._maxCost

    @property
    def minReputation(self):
        '''
        Gets the minimum reputation of the expert required.

        Returns:
            string -- The minimum reputation of the expert required, in n* format.

        '''

        return self._minReputation

    @property
    def domain(self):
        '''
        Gets the domain of the expert required to complete the task.

        Returns:
            string -- The domain of the expert required to complete the task.

        '''

        return self._domain

    @property
    def duration(self):
        '''
        Gets the duration of the task.

        Returns:
            string -- The duration of the task, in HhMM format.

        '''

        return self._duration

    # Setters
    @name.setter
    def name(self, name):
        '''
        Sets the name of the client.

        Arguments:
            name {string} -- The name of the client.

        '''

        self._name = name

    @city.setter
    def city(self, city):
        '''
        Sets the city where the task was requested.

        Arguments:
            city {string} -- The name of the city.

        '''

        self._city = city

    @date.setter
    def date(self, date):
        '''
        Sets the date when the task should be performed.

        Arguments:
            date {string} -- A date in yyyy-mm-dd format.

        '''

        self._date = date

    @hour.setter
    def hour(self, hour):
        '''
        Sets the hour when the task should be performed.

        Arguments:
            hour {string} -- An hour in hh:mm format.

        '''

        self._hour = hour

    @maxCost.setter
    def maxCost(self, maxCost):
        '''
        Sets the value that the client is willing to pay per hour.

        Arguments:
            maxCost {string} -- A value the client is willing to pay per hour.

        '''

        self._maxCost = maxCost

    @minReputation.setter
    def minReputation(self, minReputation):
        '''
        Sets the minimum reputation of the expert required.

        Arguments:
            minReputation {string} -- A value in n* format.

        '''

        self._minReputation = minReputation

    @domain.setter
    def domain(self, domain):
        '''
        Sets the domain of the expert required to complete the task.

        Arguments:
            domain {string} -- The domain required.

        '''

        self._domain = domain

    @duration.setter
    def duration(self, duration):
        '''
        Sets the duration of the task.

        Arguments:
            duration {string} -- A duration in HhMM format.

        '''

        self._duration = duration

    # Methods
    def performOn(self):
        '''
        This method uses the date and the hour of the (self) client to create a Date object with the date and the hour when the task should be performed.  

        Returns:
            Date -- The date and hour when the task should be performed.

        '''

        return Date(self.date, self.hour)

    # Overriding default methods
    def __str__(self):
        '''
        This method overrides the default 'str(Client)' method creating a string as 'name, city, date, hour, maxCost, minReputation, domain, duration'.

        Returns:
            string -- A string in 'name, city, date, hour, maxCost, minReputation, domain, duration' format.

        '''

        return f'{self.name}, {self.city}, {self.date}, {self.hour}, {self.maxCost}, {self.minReputation}, {self.domain}, {self.duration}'

    def __eq__(self, other):
        '''
        This method is used to compare this object to another object with the operator '=='.

        Arguments:
            other {Obj} -- Another object, Client is expected but not required.

        Returns:
            bool -- Returns True if the attributes of self are equal to the attributes of the other object and the object is an instance of Client. Returns False otherwise.

        '''

        return (self.name == other.name) and (self.city == other.city) and (self.date == other.date) and (self.maxCost == other.maxCost) and (self.minReputation == other.minReputation) and (self.domain == other.domain) and (self.hour == other.hour) if isinstance(other, Client) else False
