from __future__ import print_function
from datetime import datetime
from datetime import timedelta
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


class Calendar:
<<<<<<< HEAD
    def __init__(self):
        SCOPES = "https://www.googleapis.com/auth/calendar"
        store = file.Storage("token.json")
=======
    def addEvent(self, startDate, endDate, bookID):
        SCOPES = 'https://www.googleapis.com/auth/calendar'
        store = file.Storage('storage.json')
>>>>>>> parent of 39d6540... sphinx
        creds = store.get()
        if(not creds or creds.invalid):
            flow = client.flow_from_clientsecrets("credentials.json", SCOPES)
            creds = tools.run_flow(flow, store)
        self.service = build("calendar", "v3", credentials=creds)

    def addEvent(self,bookID,userName):
        borrowDate = datetime.now()
        returnDate = borrowDate + timedelta(days=7)
        borrowDateStr = borrowDate.strftime("%Y-%m-%d")
        returnDateStr = returnDate.strftime("%Y-%m-%d")
        bookReturnStart = "{}T23:59:00+10:00".format(borrowDateStr)
        bookReturnDueDate = "{}T23:59:00+10:00".format(returnDateStr)
        event = {
            "summary": "Book ID: " + bookID +" User Name: " + userName,
            "description": "New Book Return Date",
            "start": {
                "dateTime": bookReturnStart,
                "timeZone": "Australia/Melbourne",
            },
            "end": {
                "dateTime": bookReturnDueDate,
                "timeZone": "Australia/Melbourne",
            },
            "reminders": {
                "useDefault": False,
                "overrides": [
                    { "method": "email", "minutes": 120 },
                    { "method": "popup", "minutes": 120 },
                ],
            }
        }
        event = self.service.events().insert(calendarId = "primary", body = event).execute()
        print("Book return date added to calendar")

<<<<<<< HEAD
    def removeEvent(self,bookID):
        listEvents = self.service.events().list(calendarId = "primary", q = bookID).execute()
        getEvents = listEvents.get("items", [])
        for event in getEvents:
            eventId = event['id']
        event = self.service.events().delete(calendarId='primary', eventId= eventId).execute()
        print('Event removed from calendar')
=======
    def removeEvent(self):
        SCOPES = 'https://www.googleapis.com/auth/calendar'
        store = file.Storage('storage.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
            creds = tools.run_flow(flow, store)
        GCAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))
        e = GCAL.events().delete(calendarId='primary', eventId='eventId').execute()
        print('Book returned')
>>>>>>> parent of 39d6540... sphinx
