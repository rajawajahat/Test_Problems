def greetings(name, msg="Hope you are doing good", location = "By the way, I am in Karachi, where are you?"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Hope you are doing good"
    """

    message = "Hello " + name + ', ' + msg
    return message, location


print(greetings("Ali"))
print(greetings("Hussain", "How do you do?"))
print(greetings("Hassan", "How do you do?", "I moved back to germany now:)"))