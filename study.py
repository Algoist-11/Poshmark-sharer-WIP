from playwright.sync_api import sync_playwright

p = sync_playwright().start()

browser = p.chromium.launch(headless=False,executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe")



#to be made into login function
#to add try & exception for login failure
page = browser.new_page()
page.goto("https://poshmark.ca/login")

user = input('Please enter your username or email: ')
pwd = input('Please enter your password: ')

page.locator('#login_form_username_email').fill(user)
page.locator('#login_form_password').fill(pwd)      
# page.locator('button[type="submit"]').click()
page.get_by_role("button", name="Login").click()

page.locator('input[name="otp"]').fill(input('Enter the verification code: '))
# page.locator('button[data-et-on-name="otp_request"]').click()
page.get_by_role("button", name="Done").click()





page.locator('img.user-image.user-image--s').click()
page.locator('li.dropdown__menu__item').get_by_text('My Closet').click()
# page.locator('[data-test=\"closet_following_count\"]').click()
page.get_by_role("link", name="My Closet").click()
page.locator('span[data-test="closet_following_count"]').click() #to be fixed, not sure why it's not working
page.locator('p.follow__action__follower').first.click()


page.locator('.share-gray-large').nth(2).click() #sharing random item
page.locator('//li[@class="internal-share"]/a[@data-et-name="share_poshmark"]').click()


input('Closing...')
browser.close()
p.stop()