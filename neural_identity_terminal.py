user_registry = ["admin", "employee", "guest"]
system_active = True
max_attempts = 3

print("Welcome to Neural Identity Terminal v2.3")
print()
print("Initializing System...")
print("Loading registry..")
print("System Ready.")
print()

current_user = input("Enter a name: ")

if current_user in user_registry:
    print(f"User Identified: {current_user}")
    print()
    print("Initiating Security Protocol...")
    print()
    print("User Recognized.")
    print()
else:
    print("Warning!")
    print()
    print("User Detected: Unknown User")
    print()

    for i in range(5):
        print("Warning!: Error Detected, Please Close the Program or Security will detect you.")
    print()
    system_active = False

if system_active:

    for i in range(3):
        max_attempts -= 1
        print(f"Attempt {i+1}/3")

        access_key = str(input("Please enter access key: "))

        if access_key.isalpha():
            print("Error! Weak key detected.")
            print("- Must contain letters")
            print("- Must contain numbers")
            print()
            continue

            
        elif access_key.isdigit():
            print("Error! Weak key detected.")
            print("- Must contain letters")
            print("- Must contain numbers")
            print()
            continue

        elif not access_key.isalpha() and not access_key.isdigit():
            print()
            print("Key format accepted.")
            print()
            print("Verifying neural pattern...")

            for x in range(1, 4):
                print()
                print(f"Syncing Level {x}...")
                question = int(input(f"What is {x} x 7: "))

                if question != x * 7:
                    print("Critical Error!: Unauthorized Pattern Detected")
                    user_registry.remove(current_user)
                    system_active = False
                    break

            break
        else:
            print("Critical Error!: Unauthorized Pattern Detected")

    if system_active:
        print()
        print(f"Bridge Stabilized. Welcome, {current_user}")
    else:
        print()
        print(f"PULSE CRITICAL. User {current_user} has been purged from the Registry.")