import abc
import work_ticket


class ConnectionLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load_connections(self) -> (list, list):
        pass


class FileConnectionLoader(ConnectionLoader):
    """Task connecting configuration stored in two flat files"""
    def __init__(self, config_file: str, criteria_file: str):
        self.config_file = config_file
        self.criteria_file = criteria_file
        self.system_list = {}

    def _load_system_config(self):
        # open config file
        f = open(self.config_file, 'r')
        lines = f.readlines()
        for system_line in lines:
            system_line = system_line.rstrip('\r\n')
            fields = system_line.split('|')
            if fields[0][0] == '#':
                continue
            ticket_system = work_ticket.TicketSystem()

            for field in fields:
                our_ref, system_ref = field.split('=')
                if our_ref == 'name':
                    ticket_system.set_name(system_ref)
                elif our_ref == 'sys_type':
                    ticket_system.set_sys_type(system_ref)
                elif our_ref == 'url':
                    ticket_system.set_url(system_ref)
                elif our_ref == 'login':
                    ticket_system.set_login(system_ref)
                elif our_ref == 'password':
                    ticket_system.set_password(system_ref)
                elif our_ref == 'tkt_id':
                    ticket_system.set_tkt_id(system_ref)
                elif our_ref == 'tkt_requester':
                    ticket_system.set_tkt_requester(system_ref)
                elif our_ref == 'tkt_assigned':
                    ticket_system.set_tkt_assigned(system_ref)
                elif our_ref == 'tkt_description':
                    ticket_system.set_tkt_description(system_ref)
                elif our_ref == 'tkt_status':
                    ticket_system.set_tkt_status(system_ref)

            if ticket_system.name:
                self.system_list[ticket_system.name] = ticket_system
        f.close()

    def _load_query_criteria(self):
        # open config file
        f = open(self.criteria_file, 'r')
        lines = f.readlines()
        for criteria_line in lines:
            criteria_line = criteria_line.rstrip('\r\n')
            criteria = criteria_line.split('|')
            if criteria[0][0] == '#':
                continue
            if criteria[0] not in self.system_list:
                f.close()
                raise RuntimeError("I don't know what system '" + criteria[0] + "' is.")
            self.system_list[criteria[0]].criteria.append(criteria[1])
        f.close()

    def load_connections(self) -> dict:
        # TODO: add error checking
        self._load_system_config()
        self._load_query_criteria()
        return self.system_list

    def connection_names(self) -> list:
        # List individual connection names
        return list(self.system_list)





