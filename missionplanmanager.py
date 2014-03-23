#!/usr/bin/python
"""
    missionplanmanager.py
    This is the Mission Plan Manager module that will handle CRUD for Mission Plan
"""

from bottle import route, run, static_file, request
import json
import requests
import validator
import time
import datetime

validator.start()

###Routes for static css, js, html, etc...

@route('/status')
def getStatus():
    print request.query
    print request.query_string
    tData = {'status': 'succeededgfdf'}
    return json.dumps(tData)


@route('/activateMissionPlan')
def getStatus():
    tData = {'status': 'failed', 'reason': 'Not implemented yet'}
    return json.dumps(tData)


@route('/createMissionPlan', method='POST')
def createMissionPlan():
    #validdate to make sure shortname and description
    #construc mp from here

    success, res = validator.validaterequest(request.json, 'createMissionPlan')

    if (not success):
        tData = {'status': 'failed', 'reason': 'Wrong schema'}
        return json.dumps(tData)

    ret = _storeMissionPlan(request.json)
    tData = {'status': 'failed', 'reason': 'Internal Error'}
    if ret:
        tData = {'status': 'succeeded'}
    else:
        tData = {'status': 'failed', 'reason': 'Unable to store mission plan'}
    return json.dumps(tData)


@route('/updateMissionPlan', method='POST')
def updateMissionPlan():
    #validdate to make sure shortname and description
    #construc mp from here

    # success, res = validator.validaterequest(request.json, 'updateMissionPlan')
    #
    # if(not success):
    #     tData = {'status' : 'failed', 'reason':'Wrong schema'}
    #     return json.dumps(tData)

    ret = _updateMissionPlan(request.json)
    tData = {'status': 'failed', 'reason': 'Internal Error'}
    if ret:
        tData = {'status': 'succeeded'}
    else:
        tData = {'status': 'failed', 'reason': 'Unable to store mission plan'}
    return json.dumps(tData)


@route('/getMissionPlan')
def getStatus():
    tData = {'status': 'failed', 'reason': 'Not implemented yet'}
    return json.dumps(tData)


@route('/getMissionPlans')
def getStatus():
    tData = {'status': 'failed', 'reason': 'Not implemented yet'}
    return json.dumps(tData)


#############################################################################################
@route('/<filename>')
def server_static(filename):
    print request.params.dict
    print request.params.dict['id']
    tData = {'status': 'failure', 'reason': 'exception retrieving TestServer data'}
    return json.dumps(tData)
    #return static_file(filename, root='C:/DEVBIB32/TestServer/web')


@route('/js/<filename>')
def server_static(filename):
    return static_file(filename, root='C:/DEVBIB32/TestServer/web/js')


@route('/models/<filename>')
def server_static(filename):
    return static_file(filename, root='C:/DEVBIB32/TestServer/web/models')


@route('/media/css/<filename>')
def server_static(filename):
    return static_file(filename, root='C:/DEVBIB32/TestServer/web/media/css', mimetype='text/css')


@route('/media/scripts/<filename>')
def server_static(filename):
    return static_file(filename, root='C:/DEVBIB32/TestServer/web/media/scripts', mimetype='application/javascript')


@route('/media/fonts/<filename>')
def server_static(filename):
    return static_file(filename, root='C:/DEVBIB32/TestServer/web/media/fonts', mimetype='application/font-woff')


@route('/media/images/<filename>')
def server_static(filename):
    return static_file(filename, root='C:/DEVBIB32/TestServer/web/media/images')


##Query Arduino TestServer Controller for current data (basically a proxy to avoid XSS errors)
@route('/TestServer')
def index(name='TestServer'):
    try:
        r = requests.get('http://localhost:8080/foo')
        TestServerStatus = r.text;
        TestServerStatus = TestServerStatus.replace(':busy', ':"busy"');
        return (r.text);
    except:
        tData = {'status': 'failure', 'reason': 'exception retrieving TestServer data'}
        return json.dumps(tData)


###Set Arduino TestServer Controller preference data (basically a proxy to avoid XSS errors)
@route('/TestServerPost', method='POST')
def index(name='TestServer'):
    print(request.json)
    # try:
    #     r = requests.post('http://192.168.1.50:8084/TestServer/setPreferences', data='toggleJet=1')
    #     return (r.text)
    # except:
    #     tData = {'status' : 'failure', 'reason' : 'exception setting TestServer data'}
    #     return json.dumps(tData)


###Default catch-all route for blank or unknown url - redirect to index.html
@route('/:#.*#', method='ANY')
def index():
    return static_file('index.html', root='CC:/DEVBIB32/TestServer/web')


def _storeMissionPlan(pMissionPlan):
    #Validate MP is a valid json
    try:
        missionid = _getIncrementId("missionid")
        res = requests.put('http://localhost:9200/mission_plan_manager/MissionPlans/' + str(missionid) + '/_create',
                           json.dumps(pMissionPlan))

        print ("Added mission plan with id", missionid)
        print res.content
        print res.status_code

    except requests.exceptions.ConnectionError:
        return False
    if res.status_code == requests.codes['created'] or res.status_code == requests.codes['ok']:
        return True


def _updateMissionPlan(pMissionPlan):
    missionid = pMissionPlan['id']
    try:
        #Create an elasticsearch doc for update
        missiondoc = {"doc": pMissionPlan}
        print missiondoc
        print json.dumps(missiondoc)
        print requests.codes['ok']
        res = requests.post('http://localhost:9200/mission_plan_manager/MissionPlans/' + str(missionid) + "/_update",
                            json.dumps(missiondoc))

        print ("Updated mission plan with id", missionid)
        print res.content
        print res.status_code

    except requests.exceptions.ConnectionError:
        return False
    if res.status_code == requests.codes['created'] or res.status_code == requests.codes['ok']:
        return True


def _loadMissionPlan(id):
    res = requests.get('http://localhost:9200/mission_plan_manager/MissionPlans/' + str(id) + '/_source?')
    missionplan = json.loads(res.content)
    return missionplan


def _getIncrementId(pIdType):
    try:
        res = requests.put('http://localhost:9200/sequence/sequence/' + pIdType, data="{}")
        retJson = json.loads(json.dumps(res.json()))
        return retJson["_version"]
    except:
        return None


_loadMissionPlan(23)

run(host='localhost', port=8080, debug=True)
