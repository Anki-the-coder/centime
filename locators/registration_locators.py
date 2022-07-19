from selenium.webdriver.common.by import By


class registration_locators:
    firstname = (By.ID, "customer_firstname")
    lastname = (By.ID, "customer_lastname")
    email = (By.ID, "email")
    pwd = (By.ID, "passwd")

    # YOUR ADDRESS
    address_firstname = (By.ID, "firstname")
    address_lastname = (By.ID, "lastname")
    address1 = (By.ID, "address1")
    city = (By.ID, "city")
    state = (By.ID, "uniform-id_state")
    stateValue = (By.XPATH, "//select[@id='id_state']/option[@value='9']")
    postcode = (By.ID, "postcode")
    phone_mobile = (By.ID, "phone_mobile")
    register = (By.ID, "submitAccount")
