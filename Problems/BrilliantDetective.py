#!/bin/python

'''
Brilliant Detective 
You're a detective. For each crime you're investigating, you've got a number of witnesses that each remember the order of events 
they witnessed. These witnesses are trustworthy. However, any single witness might not have witnessed all events. For instance: 
     Witness Alice remembers: [ "shouting", "fight", "fleeing" ] 
     Witness Bob remembers: [ "fight", "gunshot", "panic", "fleeing" ] 
     Witness Craig remembers: [ "anger", "shouting" ] 

As the detective, we have to put together a timeline of events, in the order they occurred. The longer the resulting timeline is, 
the better. If all witnesses present a single sequence of events or if at least parts of them can be combined to create a longer 
timeline then the probability of a successful conviction goes up. Therefore, it's important to merge their timelines to the maximum 
degree possible. However, the ordering of events must be absolutely correct or else the judge will throw the case out.  In case 
there are events in those timelines that cannot be strictly ordered, it is better to present multiple separate timelines. 
Therefore, for each case, merge as many of the timelines as possible.  More specifically: 
    - if all witnesses remember events in a fully consistent manner then present a single merged timeline, 
    - if some of the events they remember can be combined or if some of them can be extended without fully merging them then present 
    multiple timelines with events merged across them to the degree possible 
    - if none of the events can be combined or extended then present the original unmodified timelines. 

For the example above, we can combine all witness accounts into a single timeline: 
       ["anger", "shouting", "fight", "gunshot", "panic", "fleeing"] 


In other cases/crimes, we may have to present multiple possible timelines: 
      Witness Dan: ["pouring gas", "laughing", "lighting match", "fire"] 
      Witness Ed: ["buying gas", "pouring gas", "crying", "fire", "smoke"] 
We can't tell whether the arsonist was crying before or after laughing / lighting the match, so we'd have to present the prosecution 
with two possible timelines: 
      ["buying gas", "pouring gas", "laughing", "lighting match", "fire", "smoke"] 
      ["buying gas", "pouring gas", "crying", "fire", "smoke"] 
Write a program that, given multiple arrays (eyewitness accounts), produces a minimal 
set of absolutely ordered, maximally long arrays (timelines) to give to the prosecution. 
Examples: 
Input 1:
[
["fight", "gunshot", "fleeing"], 
["gunshot", "falling", "fleeing"] 
]	
Output
Merge is possible 
[
["fight", "gunshot", "falling", "fleeing"]
]

Input 2:
[
["shadowy figure", "demands", "scream", "siren"],
["shadowy figure", "pointed gun", "scream"]
]	
Output:
Partial merge is possible 
[
["shadowy figure", "demand", "scream", "siren"],
["shadowy figure", "pointed gun", "scream", "siren"]
]

Input 3: 
[
["argument", "stuff", "pointing"], 
["press brief", "scandal", "pointing"],
["bribe", "coverup"]
]	
Output:
No merge is possible 
[
["argument", "stuff", "pointing"], ["press brief", "scandal", "pointing"],
["bribe", "coverup"]
]
'''

from collections import defaultdict

class Event:
    def __init__(self, event):
        # The event which is witnesed.
        self.event = event
        # List of all the next witnesed events.
        self.next = []


class BrilliantDetective:
    def __init__(self):
        # All the heads possible for a merged timeline.
        #     Event is the key and the object is the value.
        self.heads = {}
        # All the events encountered so far.
        #     Event is the key and the object is the value.
        self.nodes = {}
        # All final paths to be stored.
        self.path = []

    # ALGO:
    #  1.   Fetch the head of the timeline i.e. first event.  
    #  2.   If first event does not exist in nodes, add it to head list.   
    #  3.   For every element including head, fetch the next elements. 
    #  3'.    Check each of the next element, if it exists in the timeline array, remove it from the next elements list.
    #  4.   Add elements from the timeline as next object in the list. 
    def addTimeline(self, eventList):
        if eventList is None or len(eventList) == 0:
            return
        nextEvents = []
        ###### Process head event ######
        # Current head event and create an object.
        event = eventList[0]
        parentNode = Event(event)

        # Have already visited this event, fetch the object. Else add to nodes. 
        if event in self.nodes:
            parentNode = self.nodes[event]
        else:
            self.nodes[event] = parentNode
            # Add node to head. 
            self.heads[event] = parentNode

        # Fetch next events.
        nextEvents = parentNode.next
        # If any of the next event for the current node are present in current timeline, remove them. 
        #   We will be adding them again.
        for nextEvent in nextEvents:
            if nextEvent in eventList[1:]:
                parentNode.next.remove(nextEvent)
        ###### End processing head event ######

        ###### Process next event ######
        for eventIndex in range(1,len(eventList)):
            # Current event.
            event = eventList[eventIndex]
            # If this event was part of head before, remove it.
            if event in self.heads:
                del self.heads[event]
            
            if event in self.nodes:
                # Already visted this event, fetch object.
                curNode = self.nodes[event]
            else:
                # Create an object.
                curNode = Event(event)
            
            # Fetch next events.
            nextEvents = curNode.next
            # If any of the next event for the current node are present in current timeline, remove them. 
            #   We will be adding them again.
            for nextEvent in nextEvents:
                if nextEvent in eventList[(eventIndex+1):]:
                    curNode.next.remove(nextEvent)
            
            # Add current node to parent.
            parentNode.next.append(event)
            if curNode not in self.nodes:
                self.nodes[event] = curNode
            
            # Set current node as parentNode
            parentNode = curNode



    #  Create Paths.
    #  1.   Start from each head element, walk all the elements till next for a Node is empty.
    #  2.   If at any point we encounter more than 1 next nodes, we create 2 paths out of it.
    #
    def createPaths(self):
        for headNode in self.heads.values():
            self.createPathUtil(headNode, "")
        # Make sure to remove any subset paths
        self.path = filter(lambda f: not any(set(f) < set(g) for g in self.path), self.path)


    def createPathUtil(self, node, curPath):
        # Add current node to the path.
        if len(node.next) == 0:
            curPath += node.event
            if curPath.split() not in self.path:
                self.path.append(curPath.split("-->"))
            return
        else:
            curPath += node.event + "-->"

        # If current node has next events. 
        if node.next:
            # If there is only 1 next event in merged timelines. 
            if len(node.next) == 1:
                nextElem = self.nodes[node.next[0]]
                self.createPathUtil(nextElem, curPath)
            else:
                for nextEvent in node.next:
                    copyCurPath = curPath
                    nextElem = self.nodes[nextEvent]
                    self.createPathUtil(nextElem, copyCurPath)


if __name__ == "__main__":
    # Events
#    events = [ [ "shouting", "fight", "fleeing" ], [ "fight", "gunshot", "panic", "fleeing" ], [ "anger", "shouting" ] ]
    events = [["fight", "gunshot", "fleeing"], ["gunshot", "falling", "fleeing"] ]
#    events = [["shadowy figure", "demand", "scream", "siren"], ["shadowy figure", "pointed gun", "scream", "siren"]]
#    events = [["argument", "stuff", "pointing"], ["press brief", "scandal", "pointing"],["bribe", "coverup"]]
#    events = [  ["0"],  ["1"],  ["2"],  ["3"],  ["0", "1"],  ["0", "2"],  ["0", "3"],  ["1", "2"],  ["1", "3"],  ["2", "3"],  ["0", "1", "2"],  ["0", "1", "3"],  ["0", "2", "3"],  ["1", "2", "3"]]
#    events=[['0', '2', '3'], ['0', '1', '2', '3']]
#    events=[['0', '1', '2', '3'], ['0', '2', '3']]
    bd = BrilliantDetective()
    for event in events:
        bd.addTimeline(event)
    bd.createPaths()
    if len(bd.path) == 1:
        print "Merge is possible "
    elif sorted(bd.path) == sorted(events):
        print "No merge is possible "
    else:
        print "Partial merge is possible"
    for mergedPath in bd.path:
        print mergedPath