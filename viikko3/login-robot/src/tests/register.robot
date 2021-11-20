*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  testi  testi123

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  test  test1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  testi  testi123
    Output Should Contain  Username already exists.

Register With Too Short Username And Valid Password
    Input Credentials  te  testi123
    Output Should Contain  Username or password not long enough.

Register With Valid Username And Too Short Password
    Input Credentials  test  testi12
    Output Should Contain  Username or password not long enough.

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  test  testtest
    Output Should Contain  Check your characters.
