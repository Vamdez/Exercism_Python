def create_inventory(items):
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """
    dicionar = dict()
    for c in range(len(items)):
        dicionar[f'{items[c]}'] = items.count(items[c])
    return dicionar


def add_items(inventory, items):
    """
    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """
    for key in items:
        if key not in inventory:
            inventory[key] = 0
        inventory[key] += 1
    return inventory


def decrement_items(inventory, items):
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """
    for key in items:
        if key not in inventory:
            inventory[key] = 0
        inventory[key] -= 1
    return inventory


def remove_item(inventory, item):
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """
    if item in inventory:
        inventory.pop(item)
    return inventory


def list_inventory(inventory):
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    resp = list()
    for key, valor in inventory.items():
        if valor == 0:
            continue
        temp = (key, valor)
        resp.append(temp)
    return resp