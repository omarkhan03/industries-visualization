# import libraries
import circlify
import matplotlib.pyplot as plt

# datum is size of circle
data = [{'id': 'Industries', 'datum': 700000000, 'offset' : True, 'children' : [
              {'id' : "Healthcare", 'datum': 300000000, 'offset' : 3,
                   'children' : [
                     {'id' : "Immertec", 'datum' : 50000000},
                     {'id' : "VRTS", 'datum' : 50000000},
                     {'id' : "EliteVR", 'datum' : 50000000},
                     {'id' : "Avatour", 'datum' : 50000000},
                     {'id' : "VR vision", 'datum' : 50000000},
                     {'id' : "Pixo VR", 'datum' : 50000000},
                     {'id' : "Ultraleap", 'datum' : 50000000},
                     {'id' : "EON Reality", 'datum' : 50000000},
                     {'id' : "Simulanis", 'datum' : 50000000},
                     {'id' : "OneBonsai", 'datum' : 50000000},
                     {'id' : "ORama VR", 'datum' : 50000000}
                   ]},
              {'id' : "Self-authoring", 'datum' : 200000000, 'offset' : 2,
                   'children' : [
                     {'id' : "Motive", 'datum' : 50000000},
                     {'id' : "WarpVR", 'datum' : 50000000},
                     {'id' : "XR Proj", 'datum' : 50000000},
                     {'id' : "Immerse", 'datum' : 50000000},
                     {'id' : "LearnBrite", 'datum' : 50000000}
                   ]},
              {'id' : "Transportation", 'datum' : 200000000,  'offset' : 2,
                   'children' : [
                     {'id' : "STRIVR", 'datum' : 50000000},
                     {'id' : "EliteVR", 'datum' : 50000000},
                     {'id' : "VR vision", 'datum' : 50000000},
                     {'id' : "Ultraleap", 'datum' : 50000000},
                     {'id' : "Gravity Sketch", 'datum' : 50000000},
                     {'id' : "Simulanis", 'datum' : 50000000}
                   ]},
              {'id' : "AEC", 'datum' : 300000000, 'offset' : 3,
                   'children' : [
                     {'id' : "PaleBlue", 'datum' : 50000000},
                     {'id' : "STRIVR", 'datum' : 50000000},
                     {'id' : "3M Science", 'datum' : 50000000},
                     {'id' : "EliteVR", 'datum' : 50000000},
                     {'id' : "Avatour", 'datum' : 50000000},
                     {'id' : "VR vision", 'datum' : 50000000},
                     {'id' : "Pixo VR", 'datum' : 50000000},
                     {'id' : "OneBonsai", 'datum' : 50000000},
                     {'id' : "Caterpillar", 'datum' : 50000000}
                   ]},
              {'id' : "Robotics", 'datum' : 200000000,  'offset' : 2,
                   'children' : [
                     {'id' : "PaleBlue", 'datum' : 50000000},
                     {'id' : "STRIVR", 'datum' : 50000000},
                     {'id' : "VR vision", 'datum' : 50000000},
                     {'id' : "Gravity Sketch", 'datum' : 50000000},
                     {'id' : "Simulanis", 'datum' : 50000000}
                   ]},
               {'id' : "Aerospace", 'datum' : 200000000,  'offset' : 2,
                   'children' : [
                     {'id' : "PaleBlue", 'datum' : 50000000},
                     {'id' : "VR vision", 'datum' : 50000000},
                     {'id' : "EON Reality", 'datum' : 50000000},
                     {'id' : "Gravity Sketch", 'datum' : 50000000}
                   ]},
               {'id' : "Energy", 'datum' : 200000000,  'offset' : 2,
                   'children' : [
                     {'id' : "VRTS", 'datum' : 50000000},
                     {'id' : "STRIVR", 'datum' : 50000000},
                     {'id' : "EliteVR", 'datum' : 50000000},
                     {'id' : "VR vision", 'datum' : 50000000},
                     {'id' : "Pixo VR", 'datum' : 50000000},
                     {'id' : "EON Reality", 'datum' : 50000000},
                     {'id' : "Simulanis", 'datum' : 50000000}
                   ]},
               {'id' : "Corporate", 'datum' : 200000000,  'offset' : 2,
                   'children' : [
                     {'id' : "VRTS", 'datum' : 50000000},
                     {'id' : "STRIVR", 'datum' : 50000000},
                     {'id' : "Pixo VR", 'datum' : 50000000},
                     {'id' : "Ultraleap", 'datum' : 50000000},
                     {'id' : "Onebonsai", 'datum' : 50000000}
                   ]},
               {'id' : "Education", 'datum' : 100000000,  'offset' : 2,
                   'children' : [
                     {'id' : "EON Reality", 'datum' : 50000000},
                     {'id' : "Labster", 'datum' : 50000000},
                     {'id' : "VRLab Academy", 'datum' : 50000000}
                   ]},
               {'id' : "Commerce", 'datum' : 100000000,  'offset' : 1,
                   'children' : [
                     {'id' : "STRIVR", 'datum' : 50000000},
                     {'id' : "Avatour", 'datum' : 50000000},
                   ]},
               {'id' : "Entertainment", 'datum' : 100000000,  'offset' : 1,
                   'children' : [
                     {'id' : "Ultraleap", 'datum' : 50000000},
                     {'id' : "Alchemy VR", 'datum' : 50000000},
                   ]},
               {'id' : "Real-estate / hospitality", 'datum' : 100000000,  'offset' : 1,
                   'children' : [
                     {'id' : "Avatour", 'datum' : 50000000},
                     {'id' : "Ultraleap", 'datum' : 50000000},
                   ]},
               {'id' : "Tourism", 'datum' : 100000000,  'offset' : 1,
                   'children' : [
                     {'id' : "EON Reality", 'datum' : 50000000},
                        {'id' : "OneBonsai", 'datum' : 50000000},
                   ]},
               {'id' : "Defense", 'datum' : 100000000,  'offset' : 1,
                   'children' : [
                     {'id' : "OneBonsai", 'datum' : 50000000},
                        {'id' : "EON Reality", 'datum' : 50000000},
                    ]},
    ]}]

# Compute circle positions thanks to the circlify() function
circles = circlify.circlify(
    data, 
    show_enclosure=False, 
    target_enclosure=circlify.Circle(x=0, y=0, r=1)
)

# Create just a figure and only one subplot
fig, ax = plt.subplots(figsize=(15,15))

# Title
ax.set_title('XR training tools, organized by industry')

# Remove axes
ax.axis('off')

# Find axis boundaries
lim = max(
    max(
        abs(circle.x) + circle.r,
        abs(circle.y) + circle.r,
    )
    for circle in circles
)
plt.xlim(-lim, lim)
plt.ylim(-lim, lim)

# Print circle the highest level (continents):
for circle in circles:
    if circle.level != 2:
      continue
    x, y, r = circle
    ax.add_patch( plt.Circle((x, y), r, alpha=0.5, linewidth=2, color="lightblue"))

# Print circle and labels for the highest level:
for circle in circles:
    if circle.level != 3:
      continue
    x, y, r = circle
    label = circle.ex["id"]
    ax.add_patch( plt.Circle((x, y), r, alpha=0.5, linewidth=2, color="#69b3a2"))
    plt.annotate(label, (x,y ), ha='center', color="white", fontsize="9", bbox=dict(facecolor='#69b3a2', edgecolor='white', boxstyle='round', pad=.5))

# Print labels for the continents
for circle in circles:
    if circle.level != 2:
      continue
    x, y, r = circle
    label = circle.ex["id"]

    offset = 0

    if (circle.ex["offset"] == 3):
        offset = .25
    elif (circle.ex["offset"] == 2):
        offset = .2
    elif (circle.ex["offset"] == 1):
        offset = .13

    plt.annotate(label, (x,y + offset ) ,va='center', ha='center', fontsize="10", bbox=dict(facecolor='white', edgecolor='black', boxstyle='round', pad=.5))

# plt.show()
plt.savefig("figure", dpi=500)
plt.close()