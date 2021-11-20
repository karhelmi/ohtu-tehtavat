*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  testi
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Credentials
    Registering Should Succeed

Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  testi123
    Submit Credentials
    Registering Should Fail with message  Username or password not long enough.

Register With Valid Username And Too Short Password
    Set Username  testi
    Set Password  testi12
    Submit Credentials
    Registering Should Fail with message  Username or password not long enough.

Register With Nonmatching Password And Password Confirmation
    Set Username  testi
    Set Password  testi123
    Set Password Confirmation  321testi321
    Submit Credentials
    Registering Should Fail with message  Passwords do not match.

Login After Successful Registration
    Set Username  testi
    Set Password  testi123
    Submit Credentials
    Go To Login Page
    Set Username  testi
    Set Password  testi123
    Submit Credentials Login
    Login Should Succeed

Login After Failed Registration
    Set Username  testi
    Set Password  testi1
    Submit Credentials
    Go To Login Page
    Set Username  testi
    Set Password  testi1
    Submit Credentials Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***  

Go To Welcome Page
    Go To Welcome Page
    Welcome Page Should Be Open

Welcome Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Submit Credentials Login
    Click Button  Login

Registering Should Succeed
    Welcome Page Should Be Open

Registering Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}