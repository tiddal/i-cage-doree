class Date:
    '''
    This is a class to create a date.

    Arguments:
        date {string} -- Date in yyy-mm-dd format.
        hour {string} -- Hour in hh:mm format.

    '''

    def __init__(self, date, hour):
        '''
        The constructor for the Date class.

        Arguments:
            date {string} -- Date in yyy-mm-dd format.
            hour {string} -- Hour in hh:mm format.

        '''

        self._date = date
        self._hour = hour

    # Getters
    @property
    def date(self):
        '''
        Gets the date.

        Returns:
            string -- The date in yyyy-mm-dd format.

        '''
        return self._date

    @property
    def hour(self):
        '''
        Gets the hour.

        Returns:
            string -- The hour in hh:mm format.

        '''

        return self._hour

    # Setters
    @date.setter
    def date(self, date):
        '''
        Sets the date.

        Arguments:
            date {string} -- The date in yyyy-mm-dd format.

        '''

        self._date = date

    @hour.setter
    def hour(self, hour):
        '''
        Sets the hour.

        Arguments:
            hour {string} -- The hour in hh:mm format.

        '''

        self._hour = hour

    # Methods
    def update(self, inc):
        '''
        This method updates the date with the given increment in minutes. Considering that a working day has 12 hours from 8:00 to 20:00, every month has 30 days and every year has 12 months.

        Arguments:
            inc {int} -- The increment in minutes to update the date.

        '''

        minutes = int(self.hour.split(':')[1]) + inc
        hours = int(self.hour.split(':')[0]) + (minutes // 60)
        day = int(self.date.split('-')[2])
        month = int(self.date.split('-')[1])
        year = int(self.date.split('-')[0])

        minutes = minutes % 60

        while hours >= 20:
            day += 1
            hours = 8 + (hours - 20)

        while day > 30:
            month += 1
            day -= 30

        while month > 12:
            year += 1
            month -= 12

        self.hour = f'{hours:02d}:{minutes:02d}'
        self.date = f'{year}-{month:02d}-{day:02d}'

    def as_dict(self):
        '''
        This method creates a dictionary with the date.

        Returns:
            dict -- A dictionary in '{year: yyyy, month: mm, day: dd, hours: HH, min: MM}' format.

        '''

        dateList = self.date.split('-') + self.hour.split(':')
        dateDict = {'year': dateList[0], 'month': dateList[1],
                    'day': dateList[2], 'hours': dateList[3], 'min': dateList[4]}

        return dateDict

    # Overriding default methods
    def __str__(self):
        '''
        This method overrides the default 'str(Date)' method creating a string as 'date, hour'.

        Returns:
            string -- a string in 'date, hour' format.

        '''

        return f'{self.date}, {self.hour}'

    def __eq__(self, other):
        '''
        This method is used to compare this object to another object with the operator '=='.

        Arguments:
            other {Obj} -- Another object, Date is expected but not required.

        Returns:
            bool -- Returns True if the attributes of self are equal to the attributes of the other object and the object is an instance of Date. Returns False otherwise.

        '''

        return (self.date == other.date) and (self.hour == other.hour) if isinstance(other, Date) else False

    def __lt__(self, other):
        '''
        This method is used to get the most recent date. Can be used with the '<' and '>' operators but it might change the return.

        Arguments:
            other {Date} -- Another Date is requiered to compare to this (self) date.

        Returns:
            Date -- The most recent date.

        '''

        if (self.date, self.hour) > (other.date, other.hour):
            return self
        return other
