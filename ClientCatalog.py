from Client import *


class ClientCatalog:
    '''
    This is a class to creare a Client catalog or a collection of clients.

    Keyword Arguments:
        catalog {list} -- A list that should contain instances of Client. (default: {[]})
        header {list} -- A list that should contain every element of the header from a file. (default: {[]})

    '''

    def __init__(self, catalog=[], header=[]):
        '''
        The constructor for the ClientCatalog class.

        Keyword Arguments:
            catalog {list} -- A list that should contain instances of Client. (default: {[]})
            header {list} -- A list that should contain every element of the header from a file. (default: {[]})

        '''

        self._catalog = catalog
        self._header = header

    # Getters
    @property
    def catalog(self):
        '''
        Gets the clients catalog.

        Returns:
            list -- The clients catalog.

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

    # Setters
    @catalog.setter
    def catalog(self, catalog):
        '''
        Sets the clients catalog.

        Arguments:
            catalog {list} -- A list with instances of Client.

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

    # Methods
    def add(self, client):
        '''
        This method adds a client to the clients catalog.

        Arguments:
            client {Client} -- client should be an instance of Client.

        '''

        self.catalog.append(client)

    def load(self, fileName):
        '''
        This method loads a catalog from a file. Takes the first 7 lines of the file and add them to the catalog's header, then creates an instance of Client for each line in the file and appends it to the catalog.

        Arguments:
            fileName {string} -- The name of the file to be loaded.

        '''

        inFile = open(fileName)
        i = 0
        for line in inFile:
            i += 1
            if i <= 7:
                self.header.append(line.strip())
            else:
                name, city, date, time, maxCost, minReputation, domains, duration = line.strip().split(
                    ', ')
                self.add(Client(name, city, date, time, maxCost,
                                minReputation, domains, duration))
        inFile.close()

    # Overriding default methods
    def __str__(self):
        '''
        This method overrides the default 'str(ClientCatalog)' method creating a string as 
        '- name1, city1, date1, hour1, maxCost1, minReputation1, domain1, duration1
         - name2, city2, date2, hour2, maxCost2, minReputation2, domain2, duration2
         - (...)'.

        Returns:
            string -- A string in the format described above with every client in the catalog.

        '''

        string = ''
        for client in self.catalog:
            string += f'- {client}\n'
        return string
