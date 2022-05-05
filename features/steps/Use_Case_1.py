from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Launches Google Chrome
@given(u'Launch chrome browser')
def step_impl(context):
    context.driver=webdriver.Chrome("D:\Documents\PycharmProjects\Drivers\chromedriver.exe")

# Opens vsmonitor.com
@when(u'Opens VistaSoft Monitor login page')
def step_impl(context):
    context.driver.get("https://vsmonitor.com")
    context.driver.implicitly_wait(30)

# Logs into website with given parameters
@when(u'Enters e-mail "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    email_Input = context.driver.find_element(By.ID, "email")
    email_Input.send_keys("dd_test_1@outlook.com")
    pass_Input = context.driver.find_element(By.ID, "password")
    pass_Input.send_keys("}krK,gdC6")

# Clicking login button
@when(u'Clicks "Log-in" button')
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()

# Prints page title after logging in as verification of login success.
@then(u'User is successfully logged in')
def step_impl(context):
    page_title = context.driver.title
    page_url = context.driver.current_url
    with open("Page_Details.txt", "w") as f:
        f.write(page_title)
        f.write("\n")
        f.write(page_url)
