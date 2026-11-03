current_users = ['admin', 'vien', 'abel', 'siera', 'vivi']
new_users = ['VIEN', 'bila', 'SIERAC', 'lina', 'kila']
 
current_users_lower = [user.lower() for user in current_users]
 
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user}: already used, please enter a new username.")
    else:
        print(f"{new_user}: username is available.")