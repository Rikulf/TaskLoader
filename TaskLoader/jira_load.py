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

    def get_tasks(self, jira, args: dict):
        """
        :type jira: JIRA
        :type args: dict
        """
        self.logit.debug('In jira_load.get_tasks')
        self.logit.debug(args)
        if args.project_ID:
            try:
                self.logit.debug('getting project ' + args.project_ID)
                prj = jira.project(args.project_ID)
                self.logit.debug('Project Name ' + prj.name)
                issue_list = jira.search_issues("project = '" + args.project_ID + "'")
                for issue in issue_list:
                    print(issue.fields.assignee)
            except Exception as e:
                print("Error returning Project Information: %s" % e)
                self.logit.error("Error returning Project Information: %s", e)
                return None

        elif args.jira_query:
            try:
                self.logit.debug('getting tasks for query: ' + args.jira_query)
                issue_list = jira.search_issues(args.jira_query)
                for issue in issue_list:
                    print(issue.fields.reporter)
            except Exception as e:
                print("Error parsing Jira criteria: %s" % e)
                self.logit.error("Error parsing Jira criteria: %s", e)
                return None
        else:
            print('You must provide a project to get!')
            exit(-1)
        return 1

    def update_project(self, args):
        self.logit.debug('In update_project')
        self.logit.debug('In     get_tasks')
        if args.project_ID:
            print('updating project ' + args.project_ID)
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
        jira_loader.get_tasks(main_jira, main_args)
    if main_args.update_project:
        jira_loader.update_project(main_args)

    exit()
