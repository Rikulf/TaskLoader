import work_ticket
import jira_load
import loader_types

__author__ = 'Darryl Martin'


'''
Input: A dictionary defined in loader_types of system type specifics
Output: A ticket dictionary using references and criteria defined in the connection dictionary
'''


def load_tickets(connection) -> list:
    """
    :type connection: dict
    """
    switcher = {
        "jira": _load_jira_tickets,
        "qtask": _load_qtask_tickets
    }
    # Get the function from the switcher dictionary
    func = switcher.get(connection.sys_type, lambda: {})
    return func(connection)

# TODO: NEXT
def _load_jira_tickets(connection) -> list:
    """
    :type connection: dict
    """
    jira_loader = jira_load.JiraLoader()
    jira_connection = jira_loader.connect_jira(connection.url, connection.login, connection.password)
    jira_loader.get_tasks(jira_connection, args)

# TODO
def _load_qtask_tickets(connection) -> list:
    """
    :type connection: dict
    """
    pass

# TODO
def load_connection_details() -> list:
    pass
