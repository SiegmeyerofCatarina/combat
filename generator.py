import names
from sty import fg

from Health import Health
import ai
from entity import Entity, Action, Team
from Effect import Effect


def get_melee_cooldown(time):
    return Effect('melee c/d', time)


def get_perk_cooldown(time):
    return Effect('perk c/d', time)


def generate_entity(id: int, team: 'Team' = None) -> Entity:
    """
    Generate entity
    :param team:
    :param id:
    :return: new entity
    """
    default_ai = ai.Ai()
    name = names.get_full_name()

    fast_attack = Action(f'fast hit', 'enemy', 1, 2, get_melee_cooldown(1))
    normal_attack = Action(f'normal attack', 'enemy', 1, 5, get_melee_cooldown(2))
    heavy_attack = Action(f'heavy strike', 'enemy', 1, 7, get_melee_cooldown(3))
    pistol_shot = Action('pistol shot', 'enemy', 1, 20, get_perk_cooldown(10))  # pistol
    simple_heal = Action('hp potion', 'ally', 0, -10, get_perk_cooldown(5))  # drink potion

    entity = Entity(
        id,
        (0, 0),
        f'{name}',
        Health(25),
        default_ai,
        dict(),
        {
            fast_attack,
            normal_attack,
            heavy_attack,
            pistol_shot,
            simple_heal,
        },
        team=team,
    )
    return entity


def generate_team(id: int) -> 'Team':
    team_names_list = ['Alba', 'Bertha', 'Gambia', 'Dalton', 'Ephesian']

    team_colors_list = [
        # fg.black,
        # fg.red,
        fg.yellow,
        fg.blue,
        fg.magenta,
        fg.cyan,
        fg.white,
        fg.green,
    ]
    new_team = Team(team_names_list[id], team_colors_list[id])
    return new_team


def generate_scene():
    """
    Generate scene
    :return: new scene
    """
    return 2

