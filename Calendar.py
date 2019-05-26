from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools


class Calendar:
    """ 
    This class makes requests to the Google Calendar API. It includes adding and remove events of the library. 
    """

    def addEvent(self, startDate, endDate, bookID):
        """ 
        Adds an event to the Calendar of the library for 7 days when a book is borrowed
        with details of 
            param1 'BookID' of the borrowed book. 
            param2: 'UserId' of the user who borrowed the book
            param3: 'Start' date when the book is borrowed
            param4: 'End' date when the book has to be returned
        
        then prints " Event added " message on the console. 
        """
        SCOPES = 'https://www.googleapis.com/auth/calendar'
        store = file.Storage('storage.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
            creds = tools.run_flow(flow, store)
        GCAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))

        EVENT = {
            'summary': 'Book Return Date',
            'bookID': {bookID},
            'Start':  {'dateTime': startDate, },
            'End':    {'dateTime': endDate, },
        }
        e = GCAL.events().insert(calendarId='primary',
                                 sendNotifications=True, body=EVENT).execute()
        print("Event added")

    def removeEvent(self):
        """
        Removes an event from the calendar of the library then 
        print " Book returned " message on the console.
        """
        SCOPES = 'https://www.googleapis.com/auth/calendar'
        store = file.Storage('storage.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
            creds = tools.run_flow(flow, store)
        GCAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))
        e = GCAL.events().delete(calendarId='primary', eventId='eventId').execute()
        print('Book returned')