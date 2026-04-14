# from playwright.sync_api import sync_playwright

# def test_login():

#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()

#         # site open
#         page.goto("https://labsqajobs.qaharbor.com/")


#         #login button click 
#         page.click("//span[@class='jet-auth-links__item-text']")
#         #check new page open or not 
#         assert "login" in page.url


#         # #reg
#         page.click("//span[@class='elementor-button-text' and text()='Register Now']")
        
# #         # #check new page open or not
#         assert "registration" in page.url


# #         # #Candidate
#         page.click("//span[@class='jet-button__label' and text()='Candidate']")
        
#         # #check new page open or not
#         assert "candidate-registration" in page.url

# #         # #username
#         page.fill("//input[@id='username']", "naf")
#         page.fill("//input[@id='email']", "naf@gmail.com")
#         page.fill("//input[@id='password']", "88888888")
#         page.fill("//input[@id='conf-pass']", "88888888")

#         page.click("//button[@class='jet-form-builder__action-button jet-form-builder__submit submit-type-reload']")
#         page.wait_for_url("**status=success**")
#         assert "status=success" in page.url

#         #log in 
#         page.click("//span[@class='jet-auth-links__item-text']")
#         #check new page open or not 
#         assert "login" in page.url
#         # from fillup
#         page.fill("//input[@id='email']", "naf@gmail.com")
#         page.fill("//input[@id='password']", "88888888")

#         page.click("text=Remember me")

#         #login 
#         page.click("//button[@class='jet-form-builder__action-button jet-form-builder__submit submit-type-reload']")
#         assert "account" in page.url

















