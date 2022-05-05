from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given(u'Launch chrome')
def step_impl(context):
    context.driver=webdriver.Chrome("D:\Documents\PycharmProjects\Drivers\chromedriver.exe")


@when(u'Opens VSMonitor login page')
def step_impl(context):
    context.driver.get("https://vsmonitor.com")
    context.driver.implicitly_wait(30)


@when(u'Enter e-mail "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    email_Input = context.driver.find_element(By.ID, "email")
    email_Input.send_keys("dd_test_1@outlook.com")
    pass_Input = context.driver.find_element(By.ID, "password")
    pass_Input.send_keys("}krK,gdC6")


@when(u'Click "Log-in" button')
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()


@then(u'Clicks profile button and clicks "My User Account"')
def step_impl(context):
    context.driver.find_element(By.ID, "nav-user-button").click()
    context.driver.find_element(By.ID, "user-profile").click()
    context.driver.implicitly_wait(10)

    page_title = context.driver.title
    page_url = context.driver.current_url

    # Prints page title and Profile page URL to txt file.
    with open("Verify_Page.txt", "w") as f:
        f.write(page_title)
        f.write("\n")
        f.write(page_url)


@then(u'Checks name and email if it matches')
def step_impl(context):
    # Expected Username and E-mail values to be compared to extracted values later
    username_ori = 'test_1'
    email_ori = 'dd_test_1@outlook.com'

    # Extracts "Name" input value
    username_field = context.driver.find_element(By.ID, "username")
    username = username_field.get_attribute("value")

    # Extracts "E-mail address"
    email_feild = context.driver.find_element(By.ID, "email")
    email = email_feild.get_attribute("value")

    print("Username: " + username)
    print("Email Address: " + email)

    # Writing extracted string values to txt file
    with open("User_Cred.txt", "w") as f:
        f.write(username)
        f.write("\n")
        f.write(email)

    # Programmatically verifying if credentials match with expected output
    if username == username_ori and email == email_ori:
        print("Credentials Correct!")
        with open("User_Cred.txt", "a") as f:
            f.write("\n")
            f.write("Credentials Correct!")
    else:
        print("Credentials Wrong!")
        with open("User_Cred.txt", "a") as f:
            f.write("\n")
            f.write("Credentials Wrong!")

