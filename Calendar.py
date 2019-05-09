from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

class Calendar:
  def __init__(self):
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    GCAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))

  def addEvent(self, startDate,endDate,bookID):
    EVENT = {
        'summary': 'Book Return Date',
        'bookID': {bookID},
        'Start':  {'dateTime': startDate,},
        'End':    {'dateTime': endDate,},
    }
    e = GCAL.events().insert(calendarId='primary',
          sendNotifications=True, body=EVENT).execute()
    print('''event added:
        bookID:
        Start: 
        End:  ''' % (e['summary'].encode('utf-8'),e['bookID'],
            e['start']['dateTime'], e['end']['dateTime']))

  def removeEvent(self):
    e = GCAL.events().delete(calendarId='primary',eventId='eventId').execute()
    print('Book returned')

