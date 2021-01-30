from tkinter import Tk, Canvas
from datetime import date, datetime

def getEvents():
    events = []
    with open('days.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            current_event = line.split(',')
            event_date = datetime.strptime(current_event[1], '%d/%m/%y').date()
            current_event[1] = event_date
            events.append(current_event)
        return events
    
def CalculatoringDays(date1, date2):
    time_between = str(date1 - date2)
    number_of_days = time_between.split(' ')
    
    return number_of_days[0]

root = Tk()
c = Canvas(root, width=800, height=800, bg='black')
c.pack()

c.create_text(100, 50, anchor='w', fill='cyan',\
font='Arial 28 bold underline', text='Important days')

events = getEvents()
today = date.today()

vertical_space = 100

for event in events:
    event_name = event[0]
    days_until = CalculatoringDays(event[1], today)
    display = 'Enään %s paivaa, niin on %s' % (days_until, event_name)
    c.create_text(100, vertical_space, anchor='w', fill='lightblue', \
                  font ='Arial 20 bold', text=display)
    vertical_space += 30
