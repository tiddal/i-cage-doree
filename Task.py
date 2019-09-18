class Task:
    '''
    This is a class to create a task assigning a Client and an Expert.

    Arguments:
        date {string} -- The date when the task is going to be performed, in yyyy-mm-dd format.
        hour {string} -- The hour when the task is going to be performed, in hh:mm format.
        client {string} -- The name of the client that requested the task.
        expert {string} -- The name of the expert to perform the task.

    '''

    def __init__(self, date, hour, client, expert):
        '''
        The constructor for the Task class.

        Arguments:
            date {string} -- The date when the task is going to be performed, in yyyy-mm-dd format.
            hour {string} -- The hour when the task is going to be performed, in hh:mm format.
            client {string} -- The name of the client that requested the task.
            expert {string} -- The name of the expert to perform the task.

        '''

        self._date = date
        self._hour = hour
        self._client = client
        self._expert = expert

    # Getters
    @property
    def date(self):
        '''
        Gets the date when the task is going to be performed.

        Returns:
            string -- The date when the task is going to be performed, in yyyy-mm-dd format.

        '''

        return self._date

    @property
    def hour(self):
        '''
        Gets the hour when the task is going to be performed.

        Returns:
            string -- The hour when the task is going to be performed, in hh:mm format.

        '''

        return self._hour

    @property
    def client(self):
        '''
        Gets the name of the client that requested the task.

        Returns:
            string -- The name of the client.

        '''

        return self._client

    @property
    def expert(self):
        '''
        Gets the name of the expert to perform the task.

        Returns:
            string -- The name of the expert.

        '''

        return self._expert

    # Setters
    @date.setter
    def date(self, date):
        '''
        Sets the date when the task is going to be performed.

        Arguments:
            date {string} -- A date in yyyy-mm-dd format.

        '''

        self._date = date

    @hour.setter
    def hour(self, hour):
        '''
        Sets the hour when the task is going to be performed.

        Arguments:
            hour {string} -- A hour in hh:mm format.

        '''

        self._hour = hour

    @client.setter
    def client(self, client):
        '''
        Sets the name of the client that requested the task.

        Arguments:
            client {string} -- The name of the client.

        '''

        self._client = client

    @expert.setter
    def expert(self, expert):
        '''
        Sets the name of the expert to perform the task.

        Arguments:
            expert {string} -- The name of the expert.

        '''

        self._expert = expert

    # Overriding default methods
    def __str__(self):
        '''
        This method overrides the default 'str(Task)' method creating a string as 'date, hour, client_name, expert_name'.

        Returns:
            string -- A string in 'date, hour, client_name, expert_name' format.

        '''

        return f'{self.date}, {self.hour}, {self.client}, {self.expert}'

    def __eq__(self, other):
        '''
        This method is used to compare this object to another object with the operator '=='.

        Arguments:
            other {Obj} -- Another object, Task is expected but not required.

        Returns:
            bool -- Returns True if the attributes of self are equal to the attributes of the other object and the object is an instance of Task. Returns False otherwise.

        '''

        return (self.date == other.date) and (self.hour == other.hour) and (self.client == other.client) and (self.client == other.client) and (self.expert == other.expert) if isinstance(other, Task) else False

    def __lt__(self, other):
        '''
        This method is used to compare this Task to another Task with the operators '<' and '>'.

        Arguments:
            other {Task} -- Another Task is requiered to compare to this (self) task.

        Returns:
            bool -- Returns True if the self's date is lower than the other task's date. If the dates are the same, returns True if the self's hour is lower than the other task's hour. If the hours are equal as well, returns True if the self client's name is alphabetically lower than the other client's name. Returns False otherwise.

        '''

        return (self.date, self.hour, self.client) < (other.date, other.hour, other.client)
