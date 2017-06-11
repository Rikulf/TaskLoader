import logging
import sys
import argparse
from jira.client import JIRA
from jira.config import get_jira


# Example:
# python jira_load.py --url https://rentrak.atlassian.net --user dam --password {pw} --get --query 'issue=PPTDEV-145'
def get_parameters(predefined_args=None):
    parser = argparse.ArgumentParser(description='Interface with Jira projects.')
    parser.add_argument('--project', '-P', default=False, dest='project_ID')
    parser.add_argument('--get', '-G', action='store_true', default=False, dest='get_tasks')
    parser.add_argument('--update', '-U', action='store_true', default=False, dest='update_project')
    parser.add_argument('--url', '-s', default=False, dest='jira_server')
    parser.add_argument('--user', '-u', default=False, dest='jira_user')
    parser.add_argument('--password', '-p', default=False, dest='jira_password')
    parser.add_argument('--test', '-t', action='store_true', default=False)
    parser.add_argument('--file', '-f', default=False, dest='arg_file')
    parser.add_argument('--query', '-q', default=False, dest='jira_query')
    _args = parser.parse_args(predefined_args)
    vars(_args)
    return _args


class JiraLoader:
    """Connect to a JIRA system. Return ticket information."""
    def __init__(self):
        if 'logit' not in locals():
            self.logit = logging.getLogger(__name__)
        return

    def connect_jira(self, jira_server, jira_user, jira_password) -> JIRA:
        """
        Connect to JIRA. Return None on error
        Doesn't reference "args"
        """
        self.logit.debug("Connecting to JIRA: %s", jira_server)
        try:
            # jira_options = {'server': jira_server}
            jira_connection = get_jira(url=jira_server, username=jira_user, password=jira_password)
            # jira_connection = JIRA(options=jira_options, basic_auth=(jira_user, jira_password))
            return jira_connection
        except Exception as e:
            print("Failed to connect to JIRA: %s" % e)
            return None

    def establish_authentication(self, args):
        self.logit.debug('In establish_authentication')

        jira = self.connect_jira(args.jira_server, args.jira_user, args.jira_password)

        return jira

    def get_tasks(self, jira, project_ID, jira_query) -> list:
        """
        :type jira: JIRA
        :type project_ID: str
        :type jira_query: str
        """
        self.logit.debug('In jira_load.get_tasks')
        if project_ID:
            self.logit.debug("Project: " + project_ID)
        if jira_query:
            self.logit.debug("Query: " + jira_query)
        if project_ID:
            try:
                self.logit.debug('getting project ' + project_ID)
                prj = jira.project(project_ID)
                self.logit.debug('Project Name ' + prj.name)
                issue_list = jira.search_issues("project = '" + project_ID + "'")
            except Exception as e:
                self.logit.error("Unable to find information for Project %s. Error: %s", project_ID, e)
                print("Unable to find information for Project %s" % project_ID)
                return None
        elif jira_query:
            try:
                self.logit.debug('getting tasks for query: ' + jira_query)
                issue_list = jira.search_issues(jira_query)
            except Exception as e:
                self.logit.error("Error parsing Jira criteria: %s. Error: %s", jira_query, e)
                print ("No tickets found for JIRA query: %s" % jira_query)
                return None
        else:
            print("I don't know what tickets to get!")
            exit(-1)
        return issue_list

    def update_project(self, project_ID):
        self.logit.debug('In update_project')
        self.logit.debug('In     get_tasks')
        if project_ID:
            print('updating project ' + project_ID)
        else:
            print('You must provide a project to update!')
            exit(-1)
        return 1

###########################################
#
# MAIN
#
###########################################
if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', stream=sys.stderr, level=logging.DEBUG)
    logit = logging.getLogger(__name__)

    jira_loader = JiraLoader()
    # main_args = get_parameters(
    #   predefined_args=
    #   "--url https://rentrak.atlassian.net --user dam --get --query issue=PPTDEV-145 --password {}".split( ))
    # command line =
    #   python jira_load.py
    #       --url https://rentrak.atlassian.net --user dam@rentrakmail.com --get --query key=PPTDEV-145 --password {pw}
    main_args = get_parameters()
    main_jira = jira_loader.establish_authentication(main_args)
    if main_jira is None:
        print('Error authenticating. Aborting.')
        exit(-1)

    if main_args.get_tasks:
        issue_list = jira_loader.get_tasks(main_jira, main_args.project_ID, main_args.jira_query)
        for issue in issue_list:
            print("Reporter: " + issue.fields.reporter + " Assignee: " + issue.fields.assignee)
    if main_args.update_project:
        jira_loader.update_project(main_args.project_ID)

    exit()

