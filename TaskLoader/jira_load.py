import argparse
from jira.client import JIRA
from jira.config import get_jira


#Needs attention (all)
def get_parameters():
    parser = argparse.ArgumentParser(description='Interface with Jira projects.')
    parser.add_argument('--project', '-P', default=False, dest='project_ID')
    parser.add_argument('--get', '-G', action='store_true', default=False, dest='get_project')
    parser.add_argument('--update', '-U', action='store_true', default=False, dest='update_project')
    parser.add_argument('--url', '-s', default=False, dest='jira_server')
    parser.add_argument('--user', '-u', default=False, dest='jira_user')
    parser.add_argument('--password', '-p', default=False, dest='jira_password')
    parser.add_argument('--test', '-t', action='store_true', default=False)
    _args = parser.parse_args()
    vars(_args)
    return _args


def connect_jira(jira_server, jira_user, jira_password) -> JIRA:
    """
    Connect to JIRA. Return None on error
    """
    try:
        print("Connecting to JIRA: %s" % jira_server)
        jira_options = {'server': jira_server}
        jira_connection = get_jira(url=jira_server, username=jira_user, password=jira_password)
        # jira_connection = JIRA(options=jira_options, basic_auth=(jira_user, jira_password))
        return jira_connection
    except Exception as e:
        print("Failed to connect to JIRA: %s" % e)
        return None
    

def establish_authentication():
    print ('In establish_authentication')

    # jira=connect_jira("http://rentrak.atlassian.net", "dam", "password")
    jira=connect_jira(args.jira_server, args.jira_user, args.jira_password)

    return jira


def get_project(jira):
    print ('In     get_project')
    if args.project_ID:
        print ('getting project ' + args.project_ID)
        prj = jira.project(args.project_ID)
        print ('Project Name ' + prj.name)
#        print (vars (prj))
        issues_in_project = jira.search_issues("project = '" + args.project_ID + "'")
        for issue in issues_in_project:
            print(issue.fields.assignee)
    else:
        print ('You must provide a project to get!')
        exit(-1)
    return 1


def update_project():
    print ('In update_project')
    print ('In     get_project')
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

args = get_parameters()
jira = establish_authentication()
if args.get_project:
    get_project(jira)
if args.update_project:
    update_project()

exit()

