from selenium.webdriver.common.by import By


class locators:

    signIn = (By.XPATH, "//a[@class='login']")

    # Registration:
    emailCreate_ID = (By.ID, "email_create")
    invalidEmailMessage = (By.XPATH, "//li[text()='Invalid email address.']")
    emailAddressRequired = (By.XPATH, "//li[text()='An email address required.']")
    createAccount_button_ID = (By.ID, "SubmitCreate")

    # Login:
    email = (By.ID, "email")
    pwd = (By.ID, "passwd")
    forgotPwd = (By.XPATH, "//a[text()='Forgot your password?']")
    SignInButton = (By.ID, "SubmitLogin")
