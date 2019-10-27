from numpy.random.mtrand import choice
from sty import fg
from emoji import emojize

from Health import Health
import ai
from entity import Entity, Action, Team
from Effect import Effect


def generate_entity(id: int, team: 'Team' = None) -> Entity:
    """
    Generate entity
    :param team:
    :param id:
    :return: new entity
    """
    default_ai = ai.Ai()
    name = 'soldier'

    melee_cooldown = Effect('melee c/d')
    perk_cooldown = Effect('perk c/d')
    fast_attack = Action(f'fast {emojize(":crossed_swords:")}', 'enemy', 1, 2, cooldown=melee_cooldown, cooldown_time=1)
    normal_attack = Action(f'normal {emojize(":crossed_swords:")}', 'enemy', 1, 5, cooldown=melee_cooldown, cooldown_time=2)
    heavy_attack = Action(f'heavy {emojize(":dagger:")}', 'enemy', 1, 7, cooldown=melee_cooldown, cooldown_time=3)
    pistol_shot = Action(emojize(":dagger:"), 'enemy', 1, 20, cooldown=perk_cooldown, cooldown_time=10)  # pistol
    simple_heal = Action(emojize(":syringe:"), 'ally', 0, -10, cooldown=perk_cooldown, cooldown_time=5)  # drink potion

    entity = Entity(
        id,
        (0, 0),
        f'{name}{id}',
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
        # fg.green,
        fg.yellow,
        fg.blue,
        fg.magenta,
        fg.cyan,
        fg.white,
    ]
    new_team = Team(team_names_list[id], team_colors_list[id])
    return new_team


def generate_scene():
    """
    Generate scene
    :return: new scene
    """
    return 2

