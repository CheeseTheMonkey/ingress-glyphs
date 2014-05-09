#! /usr/bin/env python
# -*- coding: utf8 -*-

from Tkinter import *

box_width = 110
box_height = 120
glyph_height = 90
line_width = 4
node_radius = 3

glyph_coords = [
    (0,-35),
    (-35,-15),
    (35,-15),
    (-17,-5),
    (17,-5),
    (0,5),
    (-17,15),
    (17,15),
    (-35,25),
    (35,25),
    (0,45)
]

glyphs = [
    {
        'name': 'Abandon',
        'vertices': [2,4,5,6,8,10]
    },
    {
        'name': 'Adapt',
        'vertices': [1,6,5,7]
    },
    {
        'name': 'Advance',
        'vertices': [0,3,8]
    },
    {
        'name': 'Again/Repeat',
        'vertices': [8,3,6,5,4,7]
    },
    {
        'name': 'All',
        'vertices': [0,1,8,10,9,2,0]
    },
    {
        'name': 'Answer',
        'vertices': [3,4,7,5]
    },
    {
        'name': 'Attack/War',
        'vertices': [8,3,0,4,9]
    },
    {
        'name': 'Avoid/Struggle',
        'vertices': [1,0,4,2,7]
    },
    {
        'name': 'Barrier/Obstacle',
        'vertices': [0,5,7,9]
    },
    {
        'name': 'Begin',
        'vertices': [0,6,10,7]
    },
    {
        'name': 'Being/Human',
        'vertices': [3,4,7,10,6,3]
    },
    {
        'name': 'Body/Shell',
        'vertices': [3,4,5,3]
    },
    {
        'name': 'Breathe',
        'vertices': [1,3,5,4,2]
    },
    {
        'name': 'Calibration Grid',
        'vertices': []
    },
    {
        'name': 'Capture',
        'vertices': [10,8,6,5,7,2]
    },
    {
        'name': 'Change/Modify',
        'vertices': [6,5,10,7]
    },
    {
        'name': 'Chaos/Disorder',
        'vertices': [8,1,0,2,4,5,6,10]
    },
    {
        'name': 'Clear',
        'vertices': [0,5,10]
    },
    {
        'name': 'Close All',
        'vertices': [0,1,8,10,9,2,0,5,10]
    },
    {
        'name': 'Complex',
        'vertices': [4,3,5,8]
    },
    {
        'name': 'Conflict',
        'vertices': [8,3,6,7,4,9]
    },
    {
        'name': 'Consequence',
        'vertices': [1,3,6,7,9]
    },
    {
        'name': 'Contemplate',
        'vertices': [0,2,9,10,6,3,5,4]
    },
    {
        'name': 'Contract/Reduce',
        'vertices': [7,6,9]
    },
    {
        'name': 'Courage',
        'vertices': [8,3,6,7]
    },
    {
        'name': 'Create/Creation',
        'vertices': [8,6,5,4,2]
    },
    {
        'name': 'Creativity',
        'vertices': [1,3,4,10,6,1]
    },
    {
        'name': 'Creativity/Mind',
        'vertices': [6,8,1,3,5,7,9,2,4]
    },
    {
        'name': 'Danger',
        'vertices': [0,3,5,10]
    },
    {
        'name': 'Data/Signal',
        'vertices': [0,4,5,6,10]
    },
    {
        'name': 'Defend',
        'vertices': [1,6,10,7,2]
    },
    {
        'name': 'Destination',
        'vertices': [2,9,10]
    },
    {
        'name': 'Destiny',
        'vertices': [3,5,4,7,6,10]
    },
    {
        'name': 'Destruction',
        'vertices': [1,3,5,7,9]
    },
    {
        'name': 'Deteriorate/Erode',
        'vertices': [3,5,6,8]
    },
    {
        'name': 'Die',
        'vertices': [8,6,5,7,9]
    },
    {
        'name': 'Difficult',
        'vertices': [2,4,7,5,6]
    },
    {
        'name': 'Discover',
        'vertices': [2,9,10,8]
    },
    {
        'name': 'Distance/Outside',
        'vertices': [0,1,8]
    },
    {
        'name': 'Easy',
        'vertices': [4,5,6,10]
    },
    {
        'name': 'End/Close',
        'vertices': [0,2,7,10,5,0]
    },
    {
        'name': 'Enlightened',
        'vertices': [3,4,5,3,0,2,9,10]
    },
    {
        'name': 'Equal',
        'vertices': [6,3,4,7]
    },
    {
        'name': 'Escape',
        'vertices': [0,2,4,3,6]
    },
    {
        'name': 'Evolution/Success',
        'vertices': [0,5,3,6]
    },
    {
        'name': 'Failure',
        'vertices': [0,5,4,7]
    },
    {
        'name': 'Fear',
        'vertices': [3,4,7,2]
    },
    {
        'name': 'Follow',
        'vertices': [0,4,2,9]
    },
    {
        'name': 'Forget',
        'vertices': [6,8]
    },
    {
        'name': 'Futere/Forward-Time',
        'vertices': [2,4,7,9]
    },
    {
        'name': 'Gain',
        'vertices': [1,6]
    },
    {
        'name': 'Government/City',
        'vertices': [1,3,6,7,4,2]
    },
    {
        'name': 'Grow',
        'vertices': [8,3,6]
    },
    {
        'name': 'Harm',
        'vertices': [5,4,0,3,5,7,9]
    },
    {
        'name': 'Harmony/Peace',
        'vertices': [0,3,5,7,10,6,5,4,0]
    },
    {
        'name': 'Have',
        'vertices': [10,6,5,7]
    },
    {
        'name': 'Help',
        'vertices': [1,3,5,6,7]
    },
    {
        'name': 'Hide',
        'vertices': [3,4,2,7,6]
    },
    {
        'name': 'I/Me/Self',
        'vertices': [3,4,10,3]
    },
    {
        'name': 'Ignore',
        'vertices': [7,9]
    },
    {
        'name': 'Imperfect',
        'vertices': [4,5,6,3,5]
    },
    {
        'name': 'Improve',
        'vertices': [2,4,5,7]
    },
    {
        'name': 'Impure',
        'vertices': [5,3,6,5,10]
    },
    {
        'name': 'Journey',
        'vertices': [2,4,5,3,1,8,10]
    },
    {
        'name': 'Knowledge',
        'vertices': [3,5,4,10,3]
    },
    {
        'name': 'Lead',
        'vertices': [0,1,8,6,10]
    },
    {
        'name': 'Legacy',
        'vertices': [8,6,3,1,0,2,4,7,9]
    },
    {
        'name': 'Less',
        'vertices': [3,5,4]
    },
    {
        'name': 'Liberate',
        'vertices': [0,2,4,5,3,8]
    },
    {
        'name': 'Lie',
        'vertices': [6,3,5,7,4,5]
    },
    {
        'name': 'Live Again',
        'vertices': [2,4,5,6,3,8]
    },
    {
        'name': 'Lose/Loss',
        'vertices': [2,7]
    },
    {
        'name': 'Message',
        'vertices': [2,7,5,3,8]
    },
    {
        'name': 'Mind/Idea/Thought',
        'vertices': [3,5,10,6,3]
    },
    {
        'name': 'More',
        'vertices': [6,5,7]
    },
    {
        'name': 'Mystery',
        'vertices': [1,3,4,0,3,6]
    },
    {
        'name': 'Nature',
        'vertices': [8,6,3,4,7,9]
    },
    {
        'name': 'New',
        'vertices': [4,7,9]
    },
    {
        'name': 'No/Not/Absent/Inside',
        'vertices': [3,4,7]
    },
    {
        'name': 'Nourish',
        'vertices': [5,6,8,10,5]
    },
    {
        'name': 'Old',
        'vertices': [1,3,6]
    },
    {
        'name': 'Open/Accept',
        'vertices': [6,7,10,6]
    },
    {
        'name': 'Open All',
        'vertices': [10,8,1,0,2,9,10,6,7,10]
    },
    {
        'name': 'Opening/Doorway',
        'vertices': [1,3,4,2,9,7,6,8,1]
    },
    {
        'name': 'Past',
        'vertices': [1,3,6,8]
    },
    {
        'name': 'Path',
        'vertices': [0,5,6,8]
    },
    {
        'name': 'Perfection/Balance',
        'vertices': [0,5,6,8,10,9,7,5]
    },
    {
        'name': 'Perspective',
        'vertices': [8,6,5,4,0,3,5,7,9]
    },
    {
        'name': 'Potential',
        'vertices': [0,5,7,9,2]
    },
    {
        'name': 'Presence',
        'vertices': [6,3,5,4,7,10,6,7]
    },
    {
        'name': 'Present/Now',
        'vertices': [3,6,7,4]
    },
    {
        'name': 'Pure/Purity',
        'vertices': [0,5,4,7,5]
    },
    {
        'name': 'Pursue/Aspiration',
        'vertices': [1,3,0,4]
    },
    {
        'name': 'Pursue/Chase',
        'vertices': [0,5,3,6,8]
    },
    {
        'name': 'Question',
        'vertices': [0,4,3,6]
    },
    {
        'name': 'React',
        'vertices': [4,3,5,7,9]
    },
    {
        'name': 'Rebel',
        'vertices': [1,6,5,4,2,9]
    },
    {
        'name': 'Recharge',
        'vertices': [0,1,3,5,0]
    },
    {
        'name': 'Resist/Resistance',
        'vertices': [6,10,5,0,3,4]
    },
    {
        'name': 'Restraint',
        'vertices': [1,3,5,7,9,10]
    },
    {
        'name': 'Retreat',
        'vertices': [0,4,9]
    },
    {
        'name': 'Safety',
        'vertices': [8,3,4,9]
    },
    {
        'name': 'Save/Rescue',
        'vertices': [2,7,5,6]
    },
    {
        'name': 'See',
        'vertices': [0,3]
    },
    {
        'name': 'Seek/Search',
        'vertices': [5,4,3,6,7]
    },
    {
        'name': 'Self',
        'vertices': [8,10,9]
    },
    {
        'name': 'Separate',
        'vertices': [1,3,6,5,4,7,9]
    },
    {
        'name': 'Shaper/Collective',
        'vertices': [8,6,3,0,4,7,9]
    },
    {
        'name': 'Shaoer+Being',
        'vertices': [8,6,3,0,4,3,6,10,7,4,7,9]
    },
    {
        'name': 'Share',
        'vertices': [9,7,6,8,10]
    },
    {
        'name': 'Simple',
        'vertices': [6,7]
    },
    {
        'name': 'Soul/Spirit',
        'vertices': [4,5,10,7,4]
    },
    {
        'name': 'Stability/Stay',
        'vertices': [8,6,7,9]
    },
    {
        'name': 'Strong',
        'vertices': [3,4,7,6]
    },
    {
        'name': 'Together',
        'vertices': [5,3,4,5,6,8]
    },
    {
        'name': 'Truth',
        'vertices': [3,5,7,4,5,6,3]
    },
    {
        'name': 'Use',
        'vertices': [2,7,5]
    },
    {
        'name': 'Victory',
        'vertices': [0,3,10,4,0]
    },
    {
        'name': 'Want/Desire',
        'vertices': [8,6,10,7]
    },
    {
        'name': 'We/Us',
        'vertices': [3,4,10]
    },
    {
        'name': 'Weak',
        'vertices': [1,3,4,7]
    },
    {
        'name': 'Worth',
        'vertices': [1,6,5,7,2]
    },
    {
        'name': 'XM(Exotic Matter)',
        'vertices': [3,4,7,5,6,3]
    },
    {
        'name': 'You/Other',
        'vertices': [0,6,7,0]
    },
]
[
    {
        'name': '',
        'vertices': []
    },
]

def get_next_coords():
    y = glyph_height/2
    x = box_width/2
    while True:
        yield (x,y)
        x += box_width
        if x > width:
            x = box_width/2
            y += box_height

def get_next_glyph():
    n = 0
    while n < len(glyphs):
        yield glyphs[n]
        n += 1

def draw_glyph(x, y, canvas, glyph):

    # Draw a box
    canvas.create_rectangle(
        x-(box_width/2)+1,
        y-(glyph_height/2)+1,
        x+(box_width/2)-1,
        y+(box_height-(glyph_height/2)-1),
        fill = '#000'
    )

    # Draw the glyph
    for i in range(0, len(glyph['vertices']) - 1):
        canvas.create_line(
            x+glyph_coords[glyph['vertices'][i]][0],
            y+glyph_coords[glyph['vertices'][i]][1],
            x+glyph_coords[glyph['vertices'][i+1]][0],
            y+glyph_coords[glyph['vertices'][i+1]][1],
            width = line_width,
            fill = '#fff',
            capstyle = ROUND
        )

    # Draw the grid
    for coords in glyph_coords:
        canvas.create_oval(
            x+coords[0]-node_radius,
            y+coords[1]-node_radius,
            x+coords[0]+node_radius,
            y+coords[1]+node_radius,
            outline = '#fff'
        )

    # Name the glyph
    canvas.create_text(x, y+box_height/2, text=glyph['name'], fill='#fff')

# Create our main window
master = Tk()


width = master.winfo_screenwidth()
if width > 1920: width=width/2
height = master.winfo_screenheight()

frame = Frame(master,width=width, height=height)
frame.pack()

# Create a canvas to draw on
canvas = Canvas(frame, bg='#fff', width=width, height=height)

# Add a acrollbar to the frame and bind it to the canvas
vbar=Scrollbar(frame, orient=VERTICAL)
vbar.pack(side=RIGHT, fill=Y)
vbar.config(command=canvas.yview)
canvas.config(yscrollcommand=vbar.set, yscrollincrement='20')
canvas.pack(expand=True, fill=Y)

# Draw all our glyphs
c = get_next_coords()
for g in get_next_glyph():
    x,y = c.next()
    draw_glyph(x,y,canvas,g)

# Resize the scrollregion on our canvas now we actually know how big it is
canvas.config(width=width, height=height, scrollregion=(0,0,width, y+box_height-(glyph_height/2)))
canvas.pack()

# Bind the scrollwheel to the scrollbar
def _on_mousewheel(event):
    if event.num == 5 or event.delta == -120:
        canvas.yview_scroll(1, UNITS)
    if event.num == 4 or event.delta == 120:
        canvas.yview_scroll(-1, UNITS)

canvas.bind('<MouseWheel>', lambda event: _on_mousewheel(event))
canvas.bind('<Button-4>', lambda event: _on_mousewheel(event))
canvas.bind('<Button-5>', lambda event: _on_mousewheel(event))

mainloop()
