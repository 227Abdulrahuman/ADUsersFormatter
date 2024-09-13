import argparse

class Generator:
    __names = []
    __domain = None

    all = []

    def __init__(self, names, domain=None):
        self.__names = names
        self.__domain = domain  # Domain can be optional
    
    def make(self, type):
        if self.__domain:
            if type.lower() == 'upn':
                for name in self.__names:
                    self.all.extend(self.UPNgen(self.combinations(name)))
            elif type.lower() == 'down':
                for name in self.__names:
                    self.all.extend(self.DownLevelLogonGen(self.combinations(name)))
        else:
            for name in self.__names:
                self.all.extend(self.combinations(name))
        return self.all

    def combinations(self, names):
        fname, lname = names.lower().split()
        usernames = [
            f"{fname}.{lname}",                             # abdulrahman.mohamed
            f"{fname[0]}.{lname}",                          # a.mohamed
            f"{fname}-{lname}",                             # abdulrahman-mohamed
            f"{fname}_{lname}",                             # abdulrahman_mohamed
            f"{fname}{lname}",                              # abdulrahmanmohamed
            f"{fname[0]}{lname[0]}",                        # am
            f"{fname}{lname[0]}",                           # abdulrahmanm
            f"{fname[0]}{lname}",                           # amohamed
            f"{fname}.{lname[0]}",                          # abdulrahman.m
            f"{fname}", #abdulrahman
            f"{lname}", #Mohamed
        ]
        usernames = sorted(set(usernames))  # Sort and remove duplicates
        return usernames

    def UPNgen(self, usernames):
        all_upns = []
        for name in usernames:
            upn = name + "@" + self.__domain  # Create the UPN format
            all_upns.append(upn)
        return all_upns  # Return the list of UPNs
    
    def DownLevelLogonGen(self, usernames):
        all_down_level = []
        for name in usernames:
            down_level_logon = self.__domain + "/" + name  # Create the Down-Level Logon Name format
            all_down_level.append(down_level_logon)
        return all_down_level  # Return the list of Down-Level Logon Names


# Function to read file content into a list
def read_file_to_list(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()  # Read all lines from the file
        content = [line.strip() for line in content]  # Strip any leading/trailing whitespace/newlines
    return content

def main():
    # Set up argparse to handle file, type, and domain arguments with domain being optional
    parser = argparse.ArgumentParser(description="Generate username combinations")
    parser.add_argument('--file', type=str, required=True, help='Path to the file containing names (each name in a new line)')
    parser.add_argument('--type', type=str, choices=['upn', 'down'], required=False, help='The type of output (UPN or Down-Level Logon). If not specified, only combinations are generated.')
    parser.add_argument('--domain', type=str, required=False, help='The domain name for generating usernames. If not provided, combinations will be generated without domain.')

    # Parse arguments
    args = parser.parse_args()

    # Read names from file
    names = read_file_to_list(args.file)

    # Create a generator instance
    gen = Generator(names, args.domain)

    # If a type is provided (UPN or Down-Level), generate accordingly, else just print combinations
    if args.type:
        generated_names = gen.make(args.type)
    else:
        # If no type is specified, just generate the combinations
        generated_names = []
        for name in names:
            generated_names.extend(gen.combinations(name))

    # Print the generated names
    for name in generated_names:
        print(name)

if __name__ == "__main__":
    main()
