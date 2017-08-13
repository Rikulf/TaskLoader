import logging
import sys
import argparse
import work_ticket

# Example:
'''
def get_parameters(predefined_args=None):
    parser = argparse.ArgumentParser(description='Interface with qtask projects.')
    parser.add_argument('--project', '-P', default=False, dest='project_ID')
    parser.add_argument('--get', '-G', action='store_true', default=False, dest='get_tasks')
    parser.add_argument('--update', '-U', action='store_true', default=False, dest='update_project')
    parser.add_argument('--url', '-s', default=False, dest='qtask_server')
    parser.add_argument('--user', '-u', default=False, dest='qtask_user')
    parser.add_argument('--password', '-p', default=False, dest='qtask_password')
    parser.add_argument('--test', '-t', action='store_true', default=False, dest='test_only')
    parser.add_argument('--file', '-f', default=False, dest='arg_file')
    parser.add_argument('--query', '-q', default=False, dest='qtask_query')
    _args = parser.parse_args(predefined_args)
    vars(_args)
    return _args
'''


class QtaskLoader:
    """Connect to a Qtask system. Return ticket information."""
    def __init__(self, sys_type, sys_name):
        if 'logit' not in locals():
            self.logit = logging.getLogger(__name__)
        self.sys_type = sys_type
        self.sys_name = sys_name
        return

    def connect_qtask(self, qtask_server, qtask_user, qtask_password) -> qtask:
        """
        Connect to qtask. Return None on error
        Doesn't reference "args"
        """
        self.logit.debug("Connecting to qtask: %s", qtask_server)
        try:
            # qtask_options = {'server': qtask_server}
            qtask_connection = get_qtask(url=qtask_server, username=qtask_user, password=qtask_password)
            # qtask_connection = qtask(options=qtask_options, basic_auth=(qtask_user, qtask_password))
            return qtask_connection
        except Exception as e:
            print("Failed to connect to qtask: %s" % e)
            return None

    def establish_authentication(self, args):
        self.logit.debug('In establish_authentication')

        qtask = self.connect_qtask(args.qtask_server, args.qtask_user, args.qtask_password)

        return qtask

    def get_tasks(self, qtask, project_ID, qtask_query) -> list:
        """
        :type qtask: qtask
        :type project_ID: str
        :type qtask_query: str
        """
        global issue_list
        self.logit.debug('In qtask_load.get_tasks')
        if project_ID:
            try:
                self.logit.debug('getting project ' + project_ID)
                prj = qtask.project(project_ID)
                self.logit.debug('Project Name ' + prj.name)
                issue_list = qtask.search_issues("project = '" + project_ID + "'")
            except Exception as e:
                self.logit.error("Unable to find information for Project %s. Error: %s", project_ID, e)
                print("Unable to find information for Project %s" % project_ID)
                return None
        elif qtask_query:
            try:
                self.logit.debug('getting tasks for query: ' + qtask_query)
                issue_list = qtask.search_issues(qtask_query)
            except Exception as e:
                self.logit.warning("Error parsing qtask criteria: %s. Error: %s", qtask_query, e)
                print ("No tickets found for qtask query: %s" % qtask_query)
                return None
        else:
            print("I don't know what tickets to get!")
            exit(-1)
        return self._qtask_to_work_tickets(issue_list)

    def update_project(self, project_ID):
        self.logit.debug('In update_project')
        self.logit.debug('In     get_tasks')
        if project_ID:
            print('updating project ' + project_ID)
        else:
            print('You must provide a project to update!')
            exit(-1)
        return 1

    def _qtask_to_work_tickets(self, issue_list):
        self.logit.debug('Converting qtask issues to work tickets.')
        if issue_list is None:
            return None
        ticket_list = []
        for issue in issue_list:
            ticket = work_ticket.WorkTicket(self.sys_type, self.sys_name)
            ticket.set_assigned(issue.fields.assignee)
            ticket.set_description(issue.fields.description)
            ticket.set_id(issue.key)
            ticket.set_requester(issue.fields.reporter)
            ticket.set_status(issue.fields.status)
            ticket_list.append(ticket)
        return ticket_list

###########################################
#
# MAIN
#
###########################################
if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', stream=sys.stderr, level=logging.DEBUG)
    logit = logging.getLogger(__name__)

    qtask_loader = qtaskLoader()
    # main_args = get_parameters(
    #   predefined_args=
    #   "--url https://rentrak.atlassian.net --user dam --get --query issue=PPTDEV-145 --password {}".split( ))
    # command line =
    #   python qtask_load.py
    #       --url https://rentrak.atlassian.net --user dam@rentrakmail.com --get --query key=PPTDEV-145 --password {pw}
    main_args = get_parameters()
    main_qtask = qtask_loader.establish_authentication(main_args)
    if main_qtask is None:
        print('Error authenticating. Aborting.')
        exit(-1)

    if main_args.get_tasks:
        issue_list = qtask_loader.get_tasks(main_qtask, main_args.project_ID, main_args.qtask_query)
        for issue in issue_list:
            print("Reporter: " + repr(issue.fields.reporter) + " Assignee: " + repr(issue.fields.assignee))
    if main_args.update_project:
        qtask_loader.update_project(main_args.project_ID)

    exit()

