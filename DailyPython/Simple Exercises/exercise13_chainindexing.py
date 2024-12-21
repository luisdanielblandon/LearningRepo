microsoft = {
    'Engineering': {
        'team1': {
            'members': [
                {'name': 'Alice', 'role': 'Engineer', 'age': 30},
                {'name': 'Bob', 'role': 'Senior Engineer', 'age': 35}
            ],
            'projects': ['Project A', 'Project B']
        },
        'team2': {
            'members': [
                {'name': 'Charlie', 'role': 'Engineer', 'age': 28},
                {'name': 'David', 'role': 'Lead Engineer', 'age': 40}
            ],
            'projects': ['Project C']
        }
    },
    'HR': {
        'team1': {
            'members': [
                {'name': 'Grace', 'role': 'HR Specialist', 'age': 27},
                {'name': 'Hank', 'role': 'HR Manager', 'age': 38}
            ]
        }
    }
}

charliesage = microsoft['Engineering']['team2']['members'][0]['age']

print("Charlie's age is:",charliesage)