class Locators:
    # login locators
    username_loc_id = "username"
    password_loc_id = "password"
    button_loc_id = "Login"

    # logout locators
    profile_button = "//div[contains(@class,'profile')]//span[@class='uiImage']"
    logout_loc_linktext = "Log Out"

    # creating lead locators
    sales_tab = "(//span[text()='Sales'])[1]"
    accounts_tab = "(//span[text()='Accounts'])[1]"
    drop_downs = "//one-app-nav-bar-item-root[@data-id='{}']//lightning-primitive-icon[@exportparts='icon']//*[name()='svg']"
    new_button = "a[title='New'][role='button']"
    salutation = "//button[@name='salutation']"
    salutation_option = "//span[@title='{}']"
    first_name = "//input[@name='firstName']"
    last_name = "//input[@name='lastName']"
    company = "//input[@name='Company']"
    save_button = "//button[@name='SaveEdit']"

    #Other locators
    leads_tab = "(//a[@class='slds-context-bar__label-action dndItem']/child::span)[1]"
    contact_tab = "(//a[@class='slds-context-bar__label-action dndItem']/child::span)[2]"
    account_tab = "(//a[@class='slds-context-bar__label-action dndItem']/child::span)[3]"
    opportunities_tab = "(//a[@class='slds-context-bar__label-action dndItem']/child::span)[4]"
    show_more = "//a[contains(@class,'rowActionsPlaceHolder slds-button')]"
    delete_option = "//a[@title='Delete']"
    delete_button = "//span[contains(@class,'label bBody')][normalize-space()='Delete']"
    convert_button1 = "//button[@name='Convert']"
    convert_button2 = "(//button[text()='Convert'])[2]"
    goto_leads = "//button[text()='Go to Leads']"
    verify_lead_created = "(//lightning-formatted-name[contains(.,'Mr.')])[1]"
    lead_converted_verify = "//h2[normalize-space()='Your lead has been converted']"
    existing_account = "//a[normalize-space()='{}']"
    new_opportunity = "//button[normalize-space()='New Opportunity']"


    # Create new contact
    new_contact = "//button[normalize-space()='New Contact']"
    contact_salutation = "(//a[text()='--None--'])[1]"
    contact_salutation_option = "//a[normalize-space()='{}']"
    contact_first_name = "//input[@placeholder='First Name']"
    contact_last_name = "//input[@placeholder='Last Name']"
    select_account_name = "//input[@placeholder='Search Accounts...']"
    account_option = "//lightning-base-combobox-formatted-text[@title='{}']"
    contact_or_opportunity_save_button = "//button[contains(@class,'slds-button slds-button_brand c')]/child::span"
    verify_contact_or_opportunity = "//slot[contains(text(),'{}')]"

    # Create Opportunity
    opportunity_name = "//input[@name='Name']"
    close_date = "//input[@name='CloseDate']"
    stage = "//button[@aria-label='Stage']"
    select_stage_option = "//span[@title='{}']"
    forecast_category = "//button[@aria-label='Forecast Category']"
    forecast_category_option = "//span[@title='{}']"










