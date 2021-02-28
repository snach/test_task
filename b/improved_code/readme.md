## Refactoring legacy_code: ##

1. **class Animals** was created, all common methods were moved in this class.
2. **fix KeyError** for __init__() where key 'name' isn't in init_parameters dict, 
    example: Dog(dog_name, 100, {'energy': 105})
3. Fish_Simple and Fish_Can_Fly were moved to **new file fishes.py**, 
    renamed: Fish_Simple -> Fish, Fish_Can_Fly -> FishCanFly
4. Old bad tests were deleted, new cool 😎 tests added

## Install and run ##
```
install python3
pip3 install pytest
run tests: py.test -v
```