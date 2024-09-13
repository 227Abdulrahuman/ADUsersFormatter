# ADUsersFormatter
A tool used to format user names in the form of "FirstName LastName" to most of the active directory's usernames naming conventions. 
# Usage 
python3  ADUsersFormatter.py --file usersNames.txt
# Sample Input File        
Abdulrahman Mohamed 
# Sample Output 
a.mohamed
abdulrahman
abdulrahman-mohamed
abdulrahman.m
abdulrahman.mohamed
abdulrahman_mohamed
abdulrahmanm
abdulrahmanmohamed
am
amohamed
mohamed
# Additional Options 
Some tools like kerbrute require the input to be in the UPN fomate username@domain, you can generate that with the --type upn option and adding the domain --domain healthcare.local
python3 ADUsersFormatter.py --file userNames.txt --type upn --domain healthcare.local
# Sample Output
a.mohamed@healthcare.local
abdulrahman@healthcare.local
abdulrahman-mohamed@healthcare.local
abdulrahman.m@healthcare.local
abdulrahman.mohamed@healthcare.local
abdulrahman_mohamed@healthcare.local
abdulrahmanm@healthcare.local
abdulrahmanmohamed@healthcare.local
am@healthcare.local
amohamed@healthcare.local
mohamed@healthcare.local
