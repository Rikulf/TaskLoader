import abc


class ConnectionLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load_connections(self) -> Connections:
        pass


class ConnectionsInFiles(ConnectionLoader):
    """Task connecting configuration stored in two flat files"""
    def __init__(self, config_file: str, criteria_file: str):
        self.config_file = config_file
        self.criteria_file = criteria_file

    def _load_system_config(self) -> list:
        system_list = []

        # open config file
        f = open(config_filename, 'r')
        lines = f.readlines()
        for system_line in lines:
            system_line = system_line.rstrip('\r\n')
            system = system_line.split('|')
            system_list.append(work_ticket.TicketSystem(system[0], system[1], system[2]))
        f.close()

        return system_list


    def _load_query_criteria(self) -> list:
        system_list = []

        # open config file
        f = open(config_filename, 'r')
        lines = f.readlines()
        for system_line in lines:
            system_line = system_line.rstrip('\r\n')
            system = system_line.split('|')
            system_list.append(work_ticket.TicketSystem(system[0], system[1], system[2]))
        f.close()

        return system_list

    def load_connections(self) -> Connections:
        # add error checking
        _load_system_config()
        _load_query_criteria()


class Connections(object):
    def __init__(self):
        pass
