from instapy import InstaPy
# fix in https://stackoverflow.com/questions/66963998/cannot-detect-post-media-type-skip-instapy-bot-doesnt-interact-with-posts
browser = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
# browser = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

session = InstaPy(username="mjarmak", password="B~ND9c,Q$4zscyU", browser_executable_path=browser)
# session = InstaPy(username="mjarmak", password="B~ND9c,Q$4zscyU", browser_executable_path=browser, headless_browser=True)
# session.browser
session.login()
# session.set_relationship_bounds(enabled=True, max_followers=200)
session.like_by_tags(["indiemusic", "heartbreakanniversary"], amount=5, interact=True)
session.set_dont_like(["naked", "nsfw"])

# If you run the script now, then the bot will follow fifty percent of the users whose posts it liked. As usual, every action will be logged.
session.set_do_follow(True, percentage=100)
session.set_do_comment(True, percentage=100)
session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])
session.end()

print(session)
