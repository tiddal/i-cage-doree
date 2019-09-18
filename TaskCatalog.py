from Task import *
from Date import *


class TaskCatalog:
    '''
    This is a class to creare a Task catalog or a collection of tasks.

    Arguments:
        experts {ExpertCatalog} -- The collection of the experts.
        clients {ClientCatalog} -- The collection of the clients.

    Keyword Arguments:
        catalog {list} -- A list that should contain instances of Task. (default: {[]})
        header {list} -- A list that should contain every element of a header. (default: {[]})
        fileName {string} -- The name of the file to save the catalog. (default: {''})

    '''

    def __init__(self, experts, clients, catalog=[], header=[], fileName=''):
        '''
        The constructor for the TaskCatalog class.

        Arguments:
            experts {ExpertCatalog} -- The collection of the experts.
            clients {ClientCatalog} -- The collection of the clients.

        Keyword Arguments:
            catalog {list} -- A list that should contain instances of Task. (default: {[]})
            header {list} -- A list that should contain every element of a header. (default: {[]})
            fileName {string} -- The name of the file to save the catalog. (default: {''})

        '''

        self._experts = experts
        self._clients = clients
        self._catalog = catalog
        self._header = header
        self._fileName = fileName

    # Getters
    @property
    def experts(self):
        '''
        Gets the experts catalog.

        Returns:
            list -- The experts catalog.

        '''

        return self._experts

    @property
    def clients(self):
        '''
        Gets the clients catalog.

        Returns:
            list -- The clients catalog.

        '''

        return self._clients

    @property
    def catalog(self):
        '''
        Gets the tasks catalog.

        Returns:
            list -- The tasks catalog.

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

    # Setters
    @experts.setter
    def experts(self, experts):
        '''
        Sets the experts catalog.

        Arguments:
            catalog {list} -- A list with instances of Expert.

        '''

        self._experts = experts

    @clients.setter
    def clients(self, clients):
        '''
        Sets the clients catalog.

        Arguments:
            catalog {list} -- A list with instances of Client.

        '''

        self._clients = clients

    @catalog.setter
    def catalog(self, catalog):
        '''
        Sets the task catalog.

        Arguments:
            catalog {list} -- A list with instances of Task.

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
    def add(self, task):
        '''
        This method adds a task to the tasks catalog.

        Arguments:
            task {Task} -- task should be an instance of Task.

        '''

        self.catalog.append(task)

    def assign(self):
        '''
        This method starts by updating the current instance of the catalog. Then goes through the clients catalog, the experts catalog and tries to assign an expert to a client. If an expert doesn't fill the client's needs the task gets declined. Since the expert catalog is sorted and updated in every iteration the client always gets the best fit. Every task is added to the tasks catalog, even the declined ones. Finally the tasks catalog is sorted.

        '''

        self.update()
        for client in self.clients.catalog:
            assigned = False

            for expert in self.experts.catalog:

                if expert.fits(client) and not assigned:
                    appointment = (client.performOn() <
                                   expert.availableOn())
                    self.add(Task(appointment.date, appointment.hour,
                                  client.name, expert.name))
                    assigned = True
                    expert.update(client.duration, appointment)

            if not assigned:
                self.add(
                    Task(self.header[1], self.header[3], client.name, 'declined'))

        self.experts.catalog.sort()
        self.catalog.sort()

    def update(self):
        '''
        This method updates the current instance of the catalog. Creates an instance of Date with the experts catalog header and updates it in 30 minutes then updates the experts catalog and gets the header to create the tasks catalog header changing the word 'Experts' to 'Schedule'. Finally it gets the experts catalog file name and sets it to the tasks catalog file name replacing the word 'experts' with 'schedule'.

        '''

        newDate = Date(self.experts.header[1], self.experts.header[3])
        newDate.update(30)
        self.experts.update(newDate)
        for line in self.experts.header:
            self.header.append(line)
        self.header[6] = 'Schedule:'
        self.fileName = self.experts.fileName.replace('experts', 'schedule')

    def save(self):
        '''
        This method saves the catalog in a file with the self's file name, header and catalog.

        '''

        newFile = open(self.fileName, 'w')
        for line in self.header:
            newFile.write(f'{line}\n')
        for task in self.catalog:
            newFile.write(f'{task}\n')
        newFile.close()

    # Overriding default methods
    def __str__(self):
        '''
        This method overrides the default 'str(TaskCatalog)' method creating a string as 
        '- date1, hour1, client_name1, expert_name1
         - date2, hour2, client_name2, expert_name2
         - (...)'.

        Returns:
            string -- A string in the format described above with every task in the catalog.

        '''

        string = ''
        for task in self.catalog:
            string += f'- {task}\n'
        return string
