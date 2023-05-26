from selenium import webdriver
from behave import *

def before_all(context):
    context.driver = webdriver.Chrome()
    
def after_scenario(context, scenario):
    context.driver.save_screenshot('Screenshots/'+scenario.name.replace(' ', '_')+'.png')

def after_all(context):
    context.driver.quit()
    