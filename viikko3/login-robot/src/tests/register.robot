*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kisse  kisul1xi
    Registered Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  koire  koirul1xi
    Registered Already Output Should Contain  User with username koire already exists

Register With Too Short Username And Valid Password
    Input Credentials  k  kisul1xi
    Too Short Name Output Should Contain  Username length must be between 2-15

Register With Valid Username And Too Short Password
    Input Credentials  kisse  k
    Too Short Password Output Should Contain  Password length must be at least 8

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kisse  kisulixi
    Password Has No Number Output Should Contain  Password must contain at least one number


*** Keywords ***
Create User And Input New Command
    Create User  koire  koirul1x
    Input New Command
