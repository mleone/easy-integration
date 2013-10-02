#INSTALLATION

From the command-line(may need root privileges):
````bash
$ pip install git+git://github.com/mleone/easy-integration.git
````


#USAGE

From your application's test suite:

from easy_integration import browser


#API EXAMPLES

````python
# Returns True if the page contains the exact text, False otherwise:
browser.displays("Hello world!")

The "click" function is meant to handle the vast majority of browser interaction.

# Click a text element with matching text:
browser.click("View user profile")

# Click a button with matching value:
browser.click("Submit")

# Click the first element that matches the given css selector:
browser.click("form .submit-button")

Fill in a text or password field:
browser.fill_in("email", "address@example.net")
browser.fill_in("password", "abcd1234")

Select an item from a drop-down list, matching the option's id attribute:
browser.select("country", "USA")
browser.select("state", "Rhode Island")
````
