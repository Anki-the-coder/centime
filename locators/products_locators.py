from selenium.webdriver.common.by import By


class products_locators:

    profile = (By.XPATH, "//span[text()='John Parker']")
    home = (By.XPATH, "//span[text() = ' Home']")
    blouse = (By.XPATH, "//a[@title='Blouse']")
    printedDress = (By.XPATH, "//a[@title='Printed Chiffon Dress']")
    addToCartFrame = (By.XPATH, "//iframe[@class='fancybox-iframe']")
    addToCart = (By.XPATH, "//form[@id='buy_block']//button[@name='Submit']")
    continueShopping = (By.XPATH, "//span[@title='Continue shopping']")
    # productAddedToCartMsg = (By.XPATH, "//li[text()='Invalid email address.']")
    OKIcon = (By.XPATH, "//i[@class='icon-ok']")
    signOut = (By.XPATH, "//a[@title='Log me out']")


class products_delete_locators:

    cart = (By.XPATH, "//a[@title='View my shopping cart']")
    blouseDelete = (By.XPATH, "//a[text()='Blouse']//ancestor::tr//a[@class ='cart_quantity_delete']")


