from typing import Dict, List, Optional  # Import types for type hints

class PhoneBook:
    """
    Created by leon on 1/23/18.
    Made WAY better by kristofer 6/16/20
    Python version for beginner coders
    """
    def __init__(self, phonebook_dict: Optional[Dict[str, List[str]]] = None):
        """
        Constructor for PhoneBook
        :param phonebook_dict: Optional dictionary to initialize the phonebook with
        """
        if phonebook_dict is None: # If no existing phonebook was given,
            self.phonebook = {}    # ...then start with an empty phonebook
        else:
            self.phonebook = phonebook_dict  # ...otherwise use the provided dictionary

    def add(self, name: str, phone_number: str) -> None:
        """
        Add a phone number for a contact
        :param name: Contact name
        :param phone_number: Phone number to add
        """
        if name not in self.phonebook:  # If name isn't in phonebook,
            self.phonebook[name] = [phone_number] # ...create a new entry with this number in a list
        else:
            self.phonebook[name].append(phone_number) # ...otherwise, add the number to their list

    def add_all(self, name: str, *phone_numbers: str) -> None:
        """
        Add multiple phone numbers for a contact
        :param name: Contact name
        :param phone_numbers: Variable number of phone numbers to add
        """
        if name not in self.phonebook: # If name isn't in the phonebook,
            self.phonebook[name] = []  # ...start a blank list for them
            for num in phone_numbers:  # For each phone number given,
                self.add(name, num)   # ...use add() to add the number
        else:
            for num in phone_numbers:  # If the name exists, for each number,
                self.add(name, num)  # ...just add it

    def remove(self, name: str) -> None:
        """
        Remove a contact from the phonebook
        :param name: Contact name to remove
        """
        if name not in self.phonebook:  # If name isn't in phonebook,
            return None     # ...do nothing (exit)
        del self.phonebook[name]  # Otherwise, delete this person from the phonebook

    def has_entry(self, name: str, phone_number: str = None) -> bool:
        """
        Check if a contact exists, optionally with a specific phone number
        :param name: Contact name to check
        :param phone_number: Optional phone number to check
        :return: True if contact exists (with phone number if specified), False otherwise
        """
        if name not in self.phonebook:  # If the name isn't in the phonebook,
            return False      # ...return False
        if phone_number not in self.phonebook[name]:# If the phone number isn't found for that name,
            return False   # ...return False
        return True  # If both are found, return True

    def lookup(self, name: str) -> List[str]:
        """
        Look up all phone numbers for a contact
        :param name: Contact name to look up
        :return: List of phone numbers for the contact
        """
        if name not in self.phonebook:  # If name isn't in phonebook,
            return None    # ...return None
        return self.phonebook[name] # ...otherwise return list of their phone numbers

    def reverse_lookup(self, phone_number: str) -> str:
        """
        Find the contact name for a given phone number
        :param phone_number: Phone number to look up
        :return: Contact name associated with the phone number
        """
        for key in self.phonebook: # For every name in the phonebook,
            if phone_number in self.phonebook[key]: # ...if the phone number is in their list,
                return key # ...return the name (key)

    def get_all_contact_names(self) -> List[str]:
        """
        Get all contact names in the phonebook
        :return: List of all contact names
        """
        return list(self.phonebook.keys())  # Return a list of all the names in the phonebook

    def get_map(self) -> Dict[str, List[str]]:
        """
        Get the underlying dictionary representation of the phonebook
        :return: Dictionary mapping names to lists of phone numbers
        """
        return self.phonebook  # Return the whole phonebook as a dictionary