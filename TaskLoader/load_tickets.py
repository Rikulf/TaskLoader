import jira_load

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


# TODO : NEXT : Return WorkTickets
def _load_jira_tickets(connection) -> list:
    """
    :type connection: dict
    """
    jira_loader = jira_load.JiraLoader()
    jira_connection = jira_loader.connect_jira(connection.url, connection.login, connection.password)
    if jira_connection is None:
        print("ERROR: Couldn't authenticate to JIRA: %s :: %s" + connection.url, connection.login)
        return None
    ticket_list = []
    for jira_query in connection.criteria:
        tasks = jira_loader.get_tasks(jira_connection, '', jira_query)
        if tasks is None:
            continue
        ticket_list += tasks

    return ticket_list

# TODO
def _load_qtask_tickets(connection) -> list:
    """
    :type connection: dict
    """
    pass
