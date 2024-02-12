"""
SGR route from Mombasa to Nairobi
On the way we have the following stops
1. Mombasa
2. Mtito Andei
3. Voi
4. Kibwezi
5. Sultan Hamud
6. Emali
7. Machakos
8. Syokimau


Know if Emali is in the route
Know if Thika is in the route
Count the number of stations
Remove Machakos from the route as it is erroneous
reverse the list of towns
"""


class Town:
    def __init__(self, name, next=None):
        self.name = name
        self.next = next

    def __str__(self):
        return f"{self.name}"


mombasa = Town("Mombasa")
mombasa.next = Town("Mtito Andei")
mombasa.next.next = Town("Voi")
mombasa.next.next.next = Town("Kibwezi")
mombasa.next.next.next.next = Town("Sultan Hamud")
mombasa.next.next.next.next.next = Town("Emali")
mombasa.next.next.next.next.next.next = Town("Machakos")
mombasa.next.next.next.next.next.next.next = Town("Syokimau")


# printing the towns names
def show_town():
    if mombasa is None:
        return "Empty list"
    current_town = mombasa
    while current_town.next is not None:
        print(current_town.name, end="->")
        current_town = current_town.next


def check_town(town_name):
    if mombasa is None:
        return "No towns present"
    current_town = mombasa
    while current_town.next is not None:
        if current_town.name == town_name:
            return True
        current_town = current_town.next
    return False


def count_towns():
    if mombasa is None:
        return 0

    current_town = mombasa
    count = 1
    while current_town.next is not None:
        count += 1
        current_town = current_town.next
    return count


def remove_town(town_to_remove):
    """
    Get the previous town
    Get the current town
    Get the next town
    If current town is the town to remove
        set the next of previous to current's next
    :param town_to_remove:
    :return:
    """
    previous_town = mombasa
    while previous_town.next is not None:
        current_town = previous_town.next
        next_town = current_town.next

        if current_town.name == town_to_remove:
            # run removal operation
            previous_town.next = next_town
            break
        else:
            previous_town = current_town


def add_town_after(required_town_before, town_to_add_str):
    """
    for example add a town after voi called makindu
    loop and detect the required town
    when detected set the next of current as the new town
    set the next of new as the old next
    :param required_town_before:
    :param town_to_add:
    :return:
    """
    previous_town = mombasa
    town_to_add_obj = Town(name=town_to_add_str)
    while previous_town is not None:
        old_next = previous_town.next
        if required_town_before == previous_town.name:
            previous_town.next = town_to_add_obj
            town_to_add_obj.next = old_next
            break
        else:
            previous_town = old_next


# print(remove_town("Nairobi"))
print(show_town())
print("==============================")
print(add_town_after("Voi", "Mtito Andei"))
print("removed")
print('==================')
print(show_town())
