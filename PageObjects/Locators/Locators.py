class Locators:
    # login locators
    username_loc_id = "user-name"
    password_loc_id = "password"
    button_loc_id = "login-button"

    # logout locators
    main_menu_loc_xpath = "//button[contains(text(),'Open Menu')]"
    logout_loc_linktext = "Logout"

    # cart item adding locators
    cart_item1_loc_xpath = "(//button[@class='btn_primary btn_inventory'])[1]"
    cart_item2_loc_xpath = "(//button[@class='btn_primary btn_inventory'])[3]"

    # cart item icon locators
    cart_icon_loc_xpath = "//*[name()='path' and contains(@fill,'currentCol')]"

    # checkout locator
    checkout_loc_xpath = "//a[contains(text(),'CHECKOUT')]"

    # user details locators and confirming order locators
    first_name_loc_id = "first-name"
    last_name_loc_id = "last-name"
    postal_code_loc_id = "postal-code"
    submit_button_loc_xpath = "//input[@type='submit']"
    finish_button_loc_xpath = "//a[contains(text(), 'FINISH')]"
    order_success_loc_xpath = "//h2[@class='complete-header']"