"""
A simple code utilizing Google Sheets API as a database for orders.
Follow the steps described in the following link to enable API and obtain
credentials.json: https://developers.google.com/sheets/api/quickstart/python.
"""
from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

# The ID and range of a sample spreadsheet.
# Create a new spreadsheet and identify its id in the link:
# https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0

SPREADSHEET_ID = '[PASTE-YOUR-SPREADSHEET-ID-HERE]'

def sheet(values):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('./_sheets/token.json'):
        creds = Credentials.from_authorized_user_file('./_sheets/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                './_sheets/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('./_sheets/token.json', 'w') as token:
            token.write(creds.to_json())

    # update the sheets
    try:
        # Call the Sheets API
        service = build('sheets', 'v4', credentials=creds)
        # Call the Sheets API to get the values in column A (to find empty row)
        result = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID, range='Sheet1!A:A').execute()
        row = result.get('values', []) # Extract the values from the response
        # Find the index of the next empty row in column A (add 1 to account for the header row)
        next_empty_row = len(row) + 1

        # Write and update in the empty row
        sheet_range = f'A{next_empty_row}:Z{next_empty_row}'
        service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=sheet_range,
        valueInputOption='RAW',
        body={'values': [values]},
        ).execute()
    except HttpError as err:
        print(err)