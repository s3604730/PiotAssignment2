from datetime import datetime
from datetime import timedelta
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

class Calendar:
    """ 
    This class makes requests to the Google Calendar API. It includes adding and remove events of the library. 
    """
    def __init__(self):
        SCOPES = "https://www.googleapis.com/auth/calendar"
        store = file.Storage("token.json")
        creds = store.get()
        if(not creds or creds.invalid):
            flow = client.flow_from_clientsecrets("credentials.json", SCOPES)
            creds = tools.run_flow(flow, store)
        self.service = build("calendar", "v3", credentials=creds)

    def addEvent(self, bookID,userName):
        """ 
        Adds an event to the Calendar of the library for 7 days when a book is borrowed
        with details of 
            param1 'BookID' of the borrowed book. 
            param2: 'UserId' of the user who borrowed the book
            param3: 'Start' date when the book is borrowed
            param4: 'End' date when the book has to be returned
        
        then prints " Event added " message on the console. 
        """
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

    def removeEvent(self, bookID):
        
        """
        Removes an event from the calendar of the library then 
        print " Book returned " message on the console.
        """
        listEvents = self.service.events().list(calendarId = "primary", q = bookID).execute()
        getEvents = listEvents.get("items", [])
        for event in getEvents:
            eventId = event['id']
        event = self.service.events().delete(calendarId='primary', eventId= eventId).execute()
        print('Event removed from calendar')