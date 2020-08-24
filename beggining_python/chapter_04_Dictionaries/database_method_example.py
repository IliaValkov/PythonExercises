# A simple database using get() 

people = {
    "Alice" : {
        "phone" : "2341",
        "addr" : "Foo Drive 23"
    },
    "Bob" : {
        "phone" : "8331",
        "addr" : "Foo Drive 24"
    },
    "Alice" : {
        "phone" : "6969",
        "addr" : "Foo Drive 25"
    }
}

labels = {
    "phone" : "phone number",
    "addr" : "address"
}

name = input("Name: ") 

# Are we looking for a phone number or an address
request = input("Phone number (p) or address (a)?")

key = request

if request == "p": key = "phone"
if request == "a": key = "addr"

# Use get to provide default values 
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, "not available")

print("%s's %s is %s" % (name, label, result))