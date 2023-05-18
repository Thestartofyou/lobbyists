# Hypothetical lobbyist dataset
lobbyist_data = [
    {'name': 'John Smith', 'state': 'California', 'party': 'Democratic'},
    {'name': 'Jane Doe', 'state': 'California', 'party': 'Republican'},
    {'name': 'Mike Johnson', 'state': 'New York', 'party': 'Democratic'},
    {'name': 'Lisa Thompson', 'state': 'Texas', 'party': 'Republican'},
    # ...
]

# Dictionary to store the grouped lobbyists
party_groups = {}

# Group lobbyists by state and party
for lobbyist in lobbyist_data:
    state = lobbyist['state']
    party = lobbyist['party']
    if state not in party_groups:
        party_groups[state] = {}
    if party not in party_groups[state]:
        party_groups[state][party] = []
    party_groups[state][party].append(lobbyist)

# Print the grouped lobbyists
for state, parties in party_groups.items():
    print(f"State: {state}")
    for party, lobbyists in parties.items():
        print(f"Party: {party}")
        for lobbyist in lobbyists:
            print(f"Name: {lobbyist['name']}")
        print()
