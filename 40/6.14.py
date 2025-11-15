# Check if a person is a good influencer (has at least 2 social media accounts)

facebook = True
twitter = False
instagram = True

accounts_count = 0
if facebook:
    accounts_count += 1
if twitter:
    accounts_count += 1
if instagram:
    accounts_count += 1

if accounts_count >= 2:
    print("You are a good influencer!")