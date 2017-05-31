import argparse
from jira.client import JIRA
from jira.config import get_jira


# Example:  python jira_load.py --url https://rentrak.atlassian.net --user dam --password {pw} --get --query 'issue=PPTDEV-145'
# Needs attention (all)
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


def connect_jira(jira_server, jira_user, jira_password) -> JIRA:
    """
    Connect to JIRA. Return None on error
    """
    try:
        print("Connecting to JIRA: %s" % jira_server)
        # jira_options = {'server': jira_server}
        jira_connection = get_jira(url=jira_server, username=jira_user, password=jira_password)
        # jira_connection = JIRA(options=jira_options, basic_auth=(jira_user, jira_password))
        return jira_connection
    except Exception as e:
        print("Failed to connect to JIRA: %s" % e)
        return None
    

def establish_authentication(args):
    print ('In establish_authentication')

    # jira=connect_jira("http://rentrak.atlassian.net", "dam", "password")
    jira=connect_jira(args.jira_server, args.jira_user, args.jira_password)

    return jira


def get_tasks(jira, args):
    """
    :type jira: JIRA
    :type args: dict
    """
    print ('In jira_load.get_tasks')
    if args.project_ID:
        print ('getting project ' + args.project_ID)
        prj = jira.project(args.project_ID)
        print ('Project Name ' + prj.name)
#        print (vars (prj))
        issue_list = jira.search_issues("project = '" + args.project_ID + "'")
        for issue in issue_list:
            print(issue.fields.assignee)
    elif args.jira_query:
        print ('getting tasks for query')
        issue_list = jira.search_issues(args.jira_query)
        for issue in issue_list:
            print(issue.fields.reporter)
    else:
        print ('You must provide a project to get!')
        exit(-1)
    return 1


def update_project(args):
    print ('In update_project')
    print ('In     get_tasks')
    if args.project_ID:
        print ('updating project ' + args.project_ID)
    else:
        print ('You must provide a project to update!')
        exit(-1)
    return 1


###########################################
#
# MAIN
#
###########################################
if __name__ == '__main__':
    #main_args = get_parameters("--url https://rentrak.atlassian.net --user dam --get --query 'issue=PPTDEV-145'")
    main_args = get_parameters()
    main_jira = establish_authentication(main_args)
    if main_jira is None:
        print ('Error authenticating. Aborting.')
        exit(-1)


    if main_args.get_tasks:
        get_tasks(main_jira, main_args)
    if main_args.update_project:
        update_project(main_args)

    exit()

