# Coding pizza py
import click
import numpy as np


EMOJI = ['🍕', '🧀', '🍍']


class Pizza(object):

    """
    Базовый класс от которого будут наследоваться все рецепты.
    Тут же определены метод dict и перегруженны repr и eq
    """

    def dict(self):

        return {self.name: self.recipe}

    def __repr__(self):

        return f"- {self.name} {self.emoji}: {', '.join(self.recipe)}"

    def __eq__(self, __o):

        if __o.__class__.__bases__ != 'Pizza':
            return False

        return self.name == __o.name and self.size == __o.size and \
            self.emoji == __o.emoji and self.recipe == __o.recipe


class Margherita(Pizza):

    """
    Рецепт пиццы маграрита
    """

    def __init__(self, size):

        self.recipe = ['tomato sauce', 'mozzarella', 'tomatoes']
        self.emoji = '🧀'
        self.name = 'Margherita'
        self.size = size


class Pepperoni(Pizza):

    """
    Рецепт пиццы пепперони
    """

    def __init__(self, size):

        self.recipe = ['tomato sauce', 'mozzarella', 'pepperoni']
        self.emoji = '🍕'
        self.name = 'Pepperoni'
        self.size = size


class Hawaiian(Pizza):

    """
    Рецепт гавайской пиццы
    """

    def __init__(self, size):

        self.recipe = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
        self.emoji = '🍍'
        self.name = 'Hawaiian'
        self.size = size


@click.group()
def cli():
    pass


@click.command()
@click.option("--delivery", default=False, is_flag=True)
@click.option("--pizza", nargs=1, type=str, default="Pepperoni")
def order(pizza="Pepperoni", delivery=False):

    """
    Функция по заказу пиццы
    Дополнительно может быть выбрана опция по доставке
    """

    if not delivery:
        click.echo(f"👍 Приготовили за {np.random.randint(1, 10)}c!")
    else:
        click.echo(f"👍 Приготовили за {np.random.randint(1, 10)}c!\n \
        🛵 Доставили за {np.random.randint(1, 10)}c!")


@cli.command()
def menu():
    
    """
    Функция вывода меню
    """
    
    print(Margherita('L'))
    print(Pepperoni('L'))
    print(Hawaiian('L'))


if __name__ == '__main__':
    menu()
