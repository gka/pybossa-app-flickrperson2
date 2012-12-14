#
# Importing all tasks one by one, and setting n_answers for each.
# This is not as elegant as the csv bulk import as it involves
# lots of requests, but setting n_answers isn't possible in
# bulk importing.
#

import requests
import sys
import config
import pbclient


pbclient.set('endpoint', config.ENDPOINT)
pbclient.set('api_key', config.API_KEY)

app = pbclient.find_app(short_name=config.APP)[0]

# steal task from original flickrperson app
print 'loading tasks from flickrperson app'
r = requests.get('http://crowdcrafting.org/api/task?app_id=147&limit=1000')
tasks = r.json

print len(tasks), 'tasks loaded.'

finished = 0

for t in tasks:
    sent = False
    while not sent:
        #try:
            pbclient.create_task(app.id, t['info'], n_answers=100)
            print '\rsending tasks (%d of %d)' % (finished, len(tasks)),
            sys.stdout.flush()
            finished += 1
            sent = True
        #except:
        #    sent = False

print
