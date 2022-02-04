*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

***Test Cases ***
Register With Valid Username And Password
    Set Username  kisse
    Set Password  kisseli1234
    Set Password Confirmation  kisseli1234
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ki
    Set Password  kisseli1234
    Set Password Confirmation  kisseli1234
    Submit Register Credentials
    Register Should Fail With Message  Username length must be between 3-15

Register With Valid Username And Too Short Password
    Set Username  kisse
    Set Password  kis
    Set Password Confirmation  kis
    Submit Register Credentials
    Register Should Fail With Message  Password length must be at least 8


Register With Nonmatching Password And Password Confirmation
    Set Username  kisse
    Set Password  kisseli12
    Set Password Confirmation  sisseli12
    Submit Register Credentials
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Set Username  sisse
    Set Password  sisseli1234
    Set Password Confirmation  sisseli1234
    Submit Register Credentials
    Register Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Set Username  sisse
    Set Password  sisseli1234
    Submit Login Credentials
    Login Should Succeed


Login After Failed Registration
    Set Username  kisse
    Set Password  kisseli12
    Set Password Confirmation  sisseli12
    Submit Register Credentials
    Register Should Fail With Message  Passwords do not match
    Go To Login Page
    Login Page Should Be Open
    Set Username  kisse
    Set Password  kisseli12
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Go To Register Page
    Go To Registering Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Register Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}


