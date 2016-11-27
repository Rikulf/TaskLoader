import argparse
from jira.client import JIRA
from jira.config import get_jira


def get_parameters():
    parser = argparse.ArgumentParser(description='Interface with Jira projects.')
    parser.add_argument('--project', '-p', default=False, dest='project_ID')
    parser.add_argument('--get', '-g', action='store_true', default=False, dest='get_project')
    parser.add_argument('--update', '-u', action='store_true', default=False, dest='update_project')
    parser.add_argument('--test', '-t', action='store_false')
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

    # jira=connect_jira("http://rentrak.atlassian.net", "dam", "inatercamp1")
    jira=connect_jira("x","x","x")

    return jira


def get_project(jira):
    print ('In     get_project')
    if args.project_ID:
        print ('getting project ' + args.project_ID)
        prj = jira.project(args.project_ID)
        print ('Project Name ' + prj.name)
        vars ('Project properties: ' + prj)
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

args = GetParameters()
jira = establish_authentication()
if args.get_project:
        get_project(jira)
if args.update_project:
    update_project()

exit()

