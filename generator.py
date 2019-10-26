from numpy.random.mtrand import choice
from sty import fg
from emoji import emojize

from Health import Health
import ai
from entity import Entity, Effect, Action


def generate_entity(id: int) -> Entity:
    """
    Generate entity
    :param id:
    :return: new entity
    """
    default_ai = ai.Ai()

    melee_cooldown = Effect('melee c/d')
    perk_cooldown = Effect('perk c/d')
    team = choice(['pirates', 'british'])
    fast_hit = Action(f'fast {emojize(":crossed_swords:")}', 'enemy', 1, 2, cooldown=melee_cooldown, cooldown_time=1)
    normal_attack = Action(f'normal {emojize(":crossed_swords:")}', 'enemy', 1, 5, cooldown=melee_cooldown, cooldown_time=2)
    heavy_strike = Action(f'heavy {emojize(":dagger:")}', 'enemy', 1, 7, cooldown=melee_cooldown, cooldown_time=3)
    pistol_shot = Action(emojize(":dagger:"), 'enemy', 1, 20, cooldown=perk_cooldown, cooldown_time=10)  # pistol
    simple_heal = Action(emojize(":syringe:"), 'ally', 0, -10, cooldown=perk_cooldown, cooldown_time=5)  # drink potion

    entity = Entity(
        id,
        (0, 0),
        f'{fg.yellow}{team}{id}{fg.rs}',
        Health(25),
        team,
        default_ai,
        dict(),
        {
            fast_hit,
            normal_attack,
            heavy_strike,
            pistol_shot,
            simple_heal,
        },
        set(),
        set(),
    )
    return entity


def generate_scene():
    """
    Generate scene
    :return: new scene
    """
    return 2

