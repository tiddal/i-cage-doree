import sys
from ClientCatalog import *
from ExpertCatalog import *
from TaskCatalog import *


def update():
    '''
    This method is responsible for runing the application. First creates an empty experts catalog and an empty clients catalog, then fills the catalogs with the information of the input files that are expected to be well-formatted. Then it handles the exceptions that might raise from inconsistency in files. Then creates an empty tasks catalog with the experts and the clients catalogs. Finally it assigns the experts to the clientes, creates a schedule and saves it in a file as well as the experts catalog.

    Raises:
        IOError -- Raises an error if there is inconsistency between the headers of the files.

    '''

    # Initiates the experts and the clients catalog
    experts = ExpertCatalog()
    clients = ClientCatalog()
    # Loads the information in the files
    experts.load(sys.argv[1])
    clients.load(sys.argv[2])
    # Handles possible exceptions
    validateHeader(sys.argv[1], experts.header)
    validateHeader(sys.argv[2], clients.header)
    try:
        assert experts.header[:-1] == clients.header[:-1]
    except:
        raise IOError('Error in input files: inconsistent files {} and {}'.format(
            sys.argv[1], sys.argv[2]))

    # Initiates the taks catalog
    tasks = TaskCatalog(experts, clients)
    # Assign the experts to the clients creating tasks
    tasks.assign()
    # Saves the experts and tasks catalogs in a file
    experts.save()
    tasks.save()


def validateHeader(fileName, header):
    '''
    This method is responsible for validate the consistent between the name of the file and the header of the file.

    Arguments:
        fileName {string} -- The name of the file to validate.
        header {list} -- A list that contains every element of the header.

    Raises:
        IOError -- Raises an error if there is inconsistency between the name and the header in a file.

    '''

    hour = fileName.strip('.txt')[-5:]
    date = fileName[:10]
    scope = fileName.strip(date).strip(hour+'.txt')
    fileNameList = [date.replace(
        'y', '-').replace('m', '-'), hour.replace('h', ':'), scope.capitalize()+':']
    valid = True

    for i in fileNameList:
        if i not in header:
            valid = False

    try:
        assert valid
    except:
        raise IOError(
            'Error in input file: inconsistent name and header in file {}'.format(
                fileName))
