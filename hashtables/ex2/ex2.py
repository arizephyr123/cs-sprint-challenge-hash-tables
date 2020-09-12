#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # {"source" : "destination"}
    ticket_dict = {}
    route = [] 
    for ticket in tickets:
        ticket_dict[str(ticket.source)] = ticket.destination
    curr_ticket = ticket_dict['NONE']
    i=-1
    while i < length-1:
        route.append(curr_ticket)
        curr_ticket = ticket_dict[curr_ticket]
        i += 1
    return route
