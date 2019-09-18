from Date import *


class Expert:
    '''
    This is a class to creare an Expert.

    Arguments:
        name {string} -- The name of the expert.
        city {string} -- The city where the expert works.
        domain {string} -- The domains of the expert in '(domain1; domain2; ...)' format.
        reputation {string} -- The reputation of the expert in 'n*' format.
        price {string} -- Price for hour of work.
        date {string} -- The date of the expert's last completed task in yyyy-mm-dd format.
        hour {string} -- The hour of the expert's last completed task in hh:mm format.
        balance {string} -- The amount gained by work already done.

    '''

    def __init__(self, name, city, domains, reputation, price, date, hour, balance):
        '''
        The constructor for the Expert class.

        Arguments:
            name {string} -- The name of the expert.
            city {string} -- The city where the expert works.
            domain {string} -- The domains of the expert, in '(domain1; domain2; ...)' format.
            reputation {string} -- The reputation of the expert, in 'n*' format.
            price {string} -- Price for hour of work.
            date {string} -- The date of the expert's last completed task, in yyyy-mm-dd format.
            hour {string} -- The hour of the expert's last completed task, in hh:mm format.
            balance {string} -- The amount earned by the work already done.

        '''

        self._name = name
        self._city = city
        self._domains = domains
        self._reputation = reputation
        self._price = price
        self._date = date
        self._hour = hour
        self._balance = balance

    # Getters
    @property
    def name(self):
        '''
        Gets the name of the expert.

        Returns:
            string -- Name of the expert.

        '''

        return self._name

    @property
    def city(self):
        '''
        Gets the city where the expert works.

        Returns:
            string -- The name of the city.

        '''

        return self._city

    @property
    def domains(self):
        '''
        Gets the domains of the expert.

        Returns:
            string -- The domains of the expert, in '(domain1; domain2; ...)' format.

        '''

        return self._domains

    @property
    def reputation(self):
        '''
        Gets the reputation of the expert.

        Returns:
            string -- The reputation of the expert, in 'n*' format.

        '''

        return self._reputation

    @property
    def price(self):
        '''
        Gets price for hour of work.

        Returns:
            string -- The price for hour of work.

        '''

        return self._price

    @property
    def date(self):
        '''
        Gets the date of the expert's last completed task.

        Returns:
            string -- A date in yyyy-mm-dd format.

        '''

        return self._date

    @property
    def hour(self):
        '''
        Gets the hour of the expert's last completed task.

        Returns:
            string -- The hour in hh:mm format.

        '''

        return self._hour

    @property
    def balance(self):
        '''
        Gets the amount earned by the work already done.

        Returns:
            string -- The amount earned by the work already done.

        '''

        return self._balance

    # Setters
    @name.setter
    def name(self, name):
        '''
        Sets the name of the expert.

        Arguments:
            name {string} -- Name of the expert.

        '''

        self._name = name

    @city.setter
    def city(self, city):
        '''
        Sets the city where the expert works.

        Arguments:
            city {string} -- The name of the city.

        '''

        self._city = city

    @domains.setter
    def domains(self, domains):
        '''
        Sets the domains of the expert.

        Arguments:
            domains {string} -- The domains of the expert, in '(domain1; domain2; ...)' format.

        '''

        self._domains = domains

    @reputation.setter
    def reputation(self, reputation):
        '''
        Sets the reputation of the expert.

        Arguments:
            reputation {string} -- The reputation of the expert, in 'n*' format.

        '''

        self._reputation = reputation

    @price.setter
    def price(self, price):
        '''
        Sets the price for hour of work.

        Arguments:
            price {string} -- The price for hour of work.

        '''

        self._price = price

    @date.setter
    def date(self, date):
        '''
        Sets the date of the expert's last completed task.

        Arguments:
            date {string} -- A date in yyyy-mm-dd format.

        '''

        self._date = date

    @hour.setter
    def hour(self, hour):
        '''
        Sets the hour of the expert's last completed task.

        Arguments:
            hour {string} -- An hour in hh:mm format.

        '''

        self._hour = hour

    @balance.setter
    def balance(self, balance):
        '''
        Sets the amount earned by the work already done.

        Arguments:
            balance {string} -- The amount earned by the work already done.

        '''

        self._balance = balance

    # Methods
    def fits(self, client):
        '''
        This method evaluates if the (self) expert fits the given client needs. Considering that the an expert fits the client needs when he can perform the task with the reputation required by the client as well as the price per hour. Also the expert's city of work and the domain has to match the client's city and domain.

        Arguments:
            client {Client} -- The Client to try to fit. An instance of Client is required to use this method.

        Returns:
            bool -- Returns True if the expert fits the client need. Returns False otherwise.

        '''

        return client.domain in self.domains[1:-1].split('; ') and int(self.reputation[0]) >= int(client.minReputation[0]) and int(self.price) < int(client.maxCost) and self.city == client.city

    def availableOn(self):
        '''
        This method uses the date and the hour of the (self) expert to create a Date object with the date and the hour when the expert is available. Considering that an expert is only available 1 hour (60 minutes) after his last task is completed and a task that has to be started in the next day, starts at 8h00.

        Returns:
            Date -- The date and hour when the expert is available.

        '''

        available = Date(self.date, self.hour)
        d = available.as_dict()
        if int(d['hours']) == 19:
            available.update(60-int(d['min']))
        else:
            available.update(60)
        return available

    def update(self, duration, appointment):
        '''
        This method takes the duration and the date of a task and updates the date, hour and balance of the (self) expert.

        Arguments:
            duration {string} -- The duration of the task in HhMM format.
            appointment {Date} -- [description]

        '''

        minutes = int(duration.split('h')[0])*60 + int(duration.split('h')[1])
        appointment.update(minutes)

        self.balance = float(self.balance) + minutes * (float(self.price)/60)
        self.date = appointment.date
        self.hour = appointment.hour

    # Overriding default methods
    def __str__(self):
        '''
        This method overrides the default 'str(Expert)' method creating a string as 'name, city, domains, reputation, price, date, hour, balance'.

        Returns:
            string -- A string in 'name, city, domains, reputation, price, date, hour, balance' format.

        '''

        return f'{self.name}, {self.city}, {self.domains}, {self.reputation}, {self.price}, {self.date}, {self.hour}, {self.balance}'

    def __eq__(self, other):
        '''
        This method is used to compare this object to another object with the operator '=='.

        Arguments:
            other {Obj} -- Another object, Expert is expected but not required.

        Returns:
            bool -- Returns True if the attributes of self are equal to the attributes of the other object and the object is an instance of Expert. Returns False otherwise.

        '''

        return (self.name == other.name) and (self.city == other.city) and (self.domains == other.domains) and (self.reputation == other.reputation) and (self.date == other.date) and (self.hour == other.hour) and (self.balance == other.balance) if isinstance(other, Expert) else False

    def __lt__(self, other):
        '''
        This method is used to compare this Expert to another Expert with the operators '<' and '>'.

        Arguments:
            other {Expert} -- Another Expert is requiered to compare to this (self) expert.

        Returns:
            bool -- Returns True if the self's date is lower than the other expert's date. If the dates are the same, returns True if the self's hour is lower than the other expert's hour. If the hours are equal as well, returns True if the self's price is lower than the other expert's price. If the prices are equal, returns True if the self's balance is lower than the other expert's balance. If the balances are the same, returns True if the self's name is alphabetically lower than the other expert's name. Returns False otherwise.

        '''

        return (self.date, self.hour, int(self.price), float(self.balance), self.name) < (other.date, other.hour, int(other.price), float(other.balance), other.name)
