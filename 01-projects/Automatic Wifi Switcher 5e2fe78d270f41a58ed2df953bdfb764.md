# Automatic Wifi Switcher

Created: November 24, 2023 10:32 AM
Link: https://github.com/abhijeet8900/wifi-switcher

Script which will listen to or track wifi signal and swtich to known strong network. 

This will help to keep connected to strong network. 

- When wifi signal is below %.
- Find wifi with more strong connection.
- Connect to it.

Steps : 

- Listen to wifi signal.
- Trigger script if signal reaches below x%.
- List out known network and there strength.
- Find wifi with more strength.
- Check if we can connet to it.
- Connect to new wifi.
    - If connection fails try new wifi or fallback to previous one

Tech Stack :

- Something that will be compatible with multiple os : Python
- It will be runing in background all time, should be lightweight.

### Updates :

- Update script to prioritize 5GHz network over 2GHz

Ref : [https://studygyaan.com/python-programming/disabling-and-enabling-wi-fi-option-using-python](https://studygyaan.com/python-programming/disabling-and-enabling-wi-fi-option-using-python)