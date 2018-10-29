# f = {
#     'a1': 'python',
#     'b2': 'c',
#     'c3': 'java',
#     'd4': 'ruby',
# }

# friends = ['d4', 'b2']
# for name in f.keys():
#     print(name.title())
#
#     if name in friends:
#         print("Hi" + name.title() + ",language is " + f[name].title())
#
# for name in sorted(f.keys()):
#     print(name.title() + ", thank you!")

# ====================================================================

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princetion',
                             filed='physics')
print(user_profile)
