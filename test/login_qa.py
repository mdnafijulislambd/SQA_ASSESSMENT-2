
def test_case_1(page):
 
        email="qqq@gmail.com"
        password="00000000"
        username="qqq"

        page.goto("https://labsqajobs.qaharbor.com/")

 
        page.click("//span[@class='jet-auth-links__item-text']")
        assert "login" in page.url

        page.click("//span[@class='elementor-button-text' and text()='Register Now']")
        assert "registration" in page.url

        page.click("//span[@class='jet-button__label' and text()='Candidate']")
        assert "candidate-registration" in page.url

        page.fill("//input[@id='username']", username)
        page.fill("//input[@id='email']", email)
        page.fill("//input[@id='password']", password)
        page.fill("//input[@id='conf-pass']", password)
        

        page.click("//button[@class='jet-form-builder__action-button jet-form-builder__submit submit-type-reload']")
        page.wait_for_url("**status=success**")
        assert "status=success" in page.url

        page.click("//span[@class='jet-auth-links__item-text']")
        assert "login" in page.url

        page.fill("//input[@id='email']", email)
        page.fill("//input[@id='password']", password)
        page.click("text=Remember me")

        page.click("//button[@class='jet-form-builder__action-button jet-form-builder__submit submit-type-reload']")
        assert "account" in page.url









def test_case_2(page):

    username = "qqq"
    email = "qqq@gmail.com"
    password = "88888888"

    page.goto("https://labsqajobs.qaharbor.com/")

    page.click("//span[@class='jet-auth-links__item-text']")
    assert "login" in page.url

    page.click("//span[@class='elementor-button-text' and text()='Register Now']")
    assert "registration" in page.url

    page.click("//span[@class='jet-button__label' and text()='Candidate']")
    assert "candidate-registration" in page.url

    page.fill("//input[@id='username']", username)
    page.fill("//input[@id='email']", email)
    page.fill("//input[@id='password']", password)
    page.fill("//input[@id='conf-pass']", password)


    page.wait_for_timeout(3000)
    error_message = page.locator("body").inner_text().lower()
    assert "use a different email address" in error_message
    assert "we already have an account" in error_message








    
def test_case_3(page):

    username = "www"
    email = "www@gmal.con" # wrong mail format
    password = "88888888"

    page.goto("https://labsqajobs.qaharbor.com/")

    page.click("//span[@class='jet-auth-links__item-text']")
    assert "login" in page.url

    page.click("//span[@class='elementor-button-text' and text()='Register Now']")
    assert "registration" in page.url

    page.click("//span[@class='jet-button__label' and text()='Candidate']")
    assert "candidate-registration" in page.url

    page.fill("//input[@id='username']", username)
    page.fill("//input[@id='email']", email)
    page.fill("//input[@id='password']", password)
    page.fill("//input[@id='conf-pass']", password)

    page.wait_for_timeout(3000)
    error_message = page.locator("body").inner_text().lower()
    assert "use a different email address" in error_message
    assert "we already have an account" in error_message








def test_case_4(page):

    company_name = "sss"
    email = "sss@gmail.com"
    password = "00000000"
    phone="1879654678"

    page.goto("https://labsqajobs.qaharbor.com/")

    page.click("//span[@class='jet-auth-links__item-text']")
    assert "login" in page.url

    page.click("//span[@class='elementor-button-text' and text()='Register Now']")
    assert "registration" in page.url

    page.click("//span[@class='jet-button__label' and text()='Recruiter']")

    page.fill("//input[@id='_recruiter-company-name']", company_name)
    page.fill("//input[@id='_recruiter-email']", email)
    page.fill("//input[@class='jet-form-builder__field text-field phone-class']", phone)
    page.fill("//input[@id='password']", password)
    page.fill("//input[@id='confirm-password']", password)
    
    page.click("//button[@class='jet-form-builder__action-button jet-form-builder__submit submit-type-reload']")
        
    page.wait_for_url("**status=success**")
    assert "status=success" in page.url

    page.click("//span[@class='jet-auth-links__item-text']")
    assert "login" in page.url

    page.fill("//input[@id='email']", email)
    page.fill("//input[@id='password']", password)
    page.click("text=Remember me")

    page.click("//button[@class='jet-form-builder__action-button jet-form-builder__submit submit-type-reload']")
    assert "account" in page.url







def test_case_6(page):

    email = "abdd@gmail.com"
    old_password = "000000000000"  #11111111111
    new_password = "11111111111"   #000000000000

    page.goto("https://labsqajobs.qaharbor.com/")

    page.click("//span[@class='jet-auth-links__item-text']")

    page.fill("//input[@id='email']", email)
    page.fill("//input[@id='password']", old_password)
    page.click("text=Remember me")

    page.click("//button[@class='jet-form-builder__action-button jet-form-builder__submit submit-type-reload']")
    assert "account" in page.url

    page.click("//span[@class='elementor-button-text'and text()='Change Password']")

    page.fill("//input[@id='new_password']", new_password)
    page.fill("//input[@id='confirm_password']", new_password)

    page.click("//button[@class='jet-form-builder__action-button jet-form-builder__submit submit-type-reload']")

    success_text = page.locator("body").inner_text().lower()
    assert "successfully changed your password" in success_text

    page.click("//span[@class='jet-auth-links__item-text'and text()='Log Out']")

    page.click("//span[@class='jet-auth-links__item-text']")

    page.fill("//input[@id='email']", email)
    page.fill("//input[@id='password']", new_password)
    page.click("text=Remember me")

    page.click("//button[@class='jet-form-builder__action-button jet-form-builder__submit submit-type-reload']")
    assert "account" in page.url








def test_case_8(page):

    email = "qqq@gmail.com"
    password = "00000000"

    page.goto("https://labsqajobs.qaharbor.com/")

    page.click("//span[@class='jet-auth-links__item-text']")
    assert "login" in page.url

    page.fill("//input[@id='email']", email)
    page.fill("//input[@id='password']", password)
    page.click("text=Remember me")

    page.click("//button[@class='jet-form-builder__action-button jet-form-builder__submit submit-type-reload']")
    assert "account" in page.url

    page.click("//span[@class='jet-nav-link-text' and text()='Jobs']")
    assert "find-jobs" in page.url

    page.select_option("//select[@name='vacancy-country']", label="Bangladesh")
    page.click("//button[@class='apply-filters__button' and text()='Search']")

    page.wait_for_selector("//span[contains(text(),'Save')]")
    page.locator("//span[contains(text(),'Save')]").first.click()

    page.click("//span[contains(text(),'My Account') or contains(text(),'Account')]")

    page.click("//a[@class='jet-profile-menu__item-link' and text()='Saved Jobs']")

    page.wait_for_selector("//div[contains(@class,'jet-listing') or contains(@class,'job')]")
    assert page.locator("//div[contains(@class,'jet-listing') or contains(@class,'job')]").count() > 0








def test_case_9(page):

    email = "aaaa@gmail.com"
    password = "444444444444"

    page.goto("https://labsqajobs.qaharbor.com/")

    page.click("//span[@class='jet-auth-links__item-text']")
    assert "login" in page.url

    page.fill("//input[@id='email']", email)
    page.fill("//input[@id='password']", password)
    page.click("text=Remember me")

    page.click("//button[@class='jet-form-builder__action-button jet-form-builder__submit submit-type-reload']")
    assert "account" in page.url

    page.click("//span[@class='jet-button__label' and text()='Find Job']")
    assert "find-jobs" in page.url

    page.check("//span[@class='jet-checkboxes-list__label' and text()='on-site']")

    page.click("//button[contains(text(),'Search')]")

    page.wait_for_selector("//div[contains(@class,'jet-listing')]")
    page.locator("(//div[contains(@class,'jet-listing')])[1]").click()






def test_case_10(page):

    email = "bbc@gmail.com"
    password = "00000000"

    page.goto("https://labsqajobs.qaharbor.com/")

    page.click("//span[@class='jet-auth-links__item-text']")
    assert "login" in page.url

    page.fill("//input[@id='email']", email)
    page.fill("//input[@id='password']", password)
    page.click("text=Remember me")

    page.click("//button[@class='jet-form-builder__action-button jet-form-builder__submit submit-type-reload']")
    assert "account" in page.url

    page.click("//span[@class='jet-button__label' and text()='Post A Job']")

