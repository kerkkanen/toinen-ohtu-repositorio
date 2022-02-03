*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123
    Login Output Should Contain  Logged in

Login With Incorrect Password
    Input Credentials  kalle  kalle124
    Incorrect Login Output Should Contain  Invalid username or password

Login With Nonexistent Username
    Input Credentials  ${EMPTY}  kalle123
    No Username Login Output Should Contain  Username and password are required

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command
