from Expert import *


class ExpertCatalog:
    '''
    This is a class to creare an Expert catalog or a collection of experts.

    Keyword Arguments:
        catalog {list} -- A list that should contain instances of Expert. (default: {[]})
        header {list} -- A list that should contain every element of the header from a file. (default: {[]})
        fileName {string} -- The name of the file to save the catalog. (default: {''})

    '''

    def __init__(self, catalog=[], header=[], fileName=''):
        '''
        The constructor for the ExpertCatalog class.

        Keyword Arguments:
            catalog {list} -- A list that should contain instances of Expert (default: {[]})
            header {list} -- A list that should contain every element of the header from a file. (default: {[]})
            fileName {string} -- The name of the file to save the catalog. (default: {''})

        '''

        self._catalog = catalog
        self._header = header
        self._fileName = fileName

    # Getters
    @property
    def catalog(self):
        '''
        Gets the experts catalog.

        Returns:
            list -- The experts catalog.

        '''

        return self._catalog

    @property
    def header(self):
        '''
        Gets the header of the catalog.

        Returns:
            list -- The header of the catalog.

        '''

        return self._header

    @property
    def fileName(self):
        '''
        Gets the name of the file to save the catalog.

        Returns:
            string -- the name of the file.

        '''

        return self._fileName

    @catalog.setter
    def catalog(self, catalog):
        '''
        Sets the experts catalog.

        Arguments:
            catalog {list} -- A list with instances of Expert.

        '''

        self._catalog = catalog

    @header.setter
    def header(self, header):
        '''
        Sets the header of the catalog.

        Arguments:
            header {list} -- A list that should contain every element of the header from a file.

        '''

        self._header = header

    @fileName.setter
    def fileName(self, fileName):
        '''
        Sets the name of the file to save the catalog.

        Arguments:
            fileName {string} -- The name of the file.

        '''

        self._fileName = fileName

    # Methods
    def add(self, expert):
        '''
        This method adds an expert to the experts catalog.

        Arguments:
            expert {Expert} -- expert should be an instance of Expert.

        '''

        self.catalog.append(expert)

    def update(self, newDate):
        '''
        This method updates the self's header as well as the file name with the given Date.

        Arguments:
            newDate {Date} -- An instance of Date to update the header and the file name.

        '''

        self.header[1], self.header[3] = newDate.date, newDate.hour
        d = newDate.as_dict()
        self.fileName = f"{d['year']}y{d['month']}m{d['day']}experts{d['hours']}h{d['min']}.txt"

    def load(self, fileName):
        '''
        This method loads a catalog from a file. Takes the first 7 lines of the file and add them to the catalog's header, then creates an instance of Expert for each line in the file and appends it to the catalog. Also updates the self's file name to the given file name and sorts the catalog.

        Arguments:
            fileName {string} -- The name of the file to be laoded.

        '''

        self.fileName = fileName
        inFile = open(fileName)
        i = 0
        for line in inFile:
            i += 1
            if i <= 7:
                self.header.append(line.strip())
            else:
                name, city, domains, reputation, price, lastRequest, availability, balance = line.strip().split(', ')
                self.add(Expert(name, city, domains, reputation,
                                price, lastRequest, availability, balance))

        inFile.close()
        self.catalog.sort()

    def save(self):
        '''
        This method saves the catalog in a file with the self's file name, header and catalog.

        '''

        newFile = open(self.fileName, 'w')
        for line in self.header:
            newFile.write(f'{line}\n')
        for expert in self.catalog:
            newFile.write(f'{expert}\n')
        newFile.close()

    # Overriding default methods
    def __str__(self):
        '''
        This method overrides the default 'str(ExpertCatalog)' method creating a string as 
        '- name1, city1, domains1, reputation1, price1, date1, hour1, balance1
         - name2, city2, domains2, reputation2, price2, date2, hour2, balance2
         - (...)'.

        Returns:
            string -- A string in the format described above with every expert in the catalog.

        '''

        string = ''
        for expert in self.catalog:
            string += f'- {expert}\n'
        return string
