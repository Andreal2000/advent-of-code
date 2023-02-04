import os
from sys import maxsize
from copy import deepcopy


def part_one(input):
    # 0=manacost, 1=dmg, 2=hp, 3=armour, 4=mana, 5=turns, 6=index
    missile = [53, 4, 0, 0, 0, 0, 0]
    drain = [73, 2, 2, 0, 0, 0, 1]
    shield = [113, 0, 0, 7, 0, 6, 2]
    poison = [173, 3, 0, 0, 0, 6, 3]
    recharge = [229, 0, 0, 0, 101, 5, 4]
    spells = [missile, drain, shield, poison, recharge]
    global least_mana_used
    least_mana_used = maxsize

    def sim(boss_hp, boss_dmg, me_hp, me_mana,
            active_spells=[], player_turn=True, mana_used=0):

        global least_mana_used
        myArmour = 0

        new_active_spells = []
        for active_spell in active_spells:
            boss_hp -= active_spell[1]
            me_hp += active_spell[2]
            myArmour += active_spell[3]
            me_mana += active_spell[4]

            if active_spell[5] > 1:
                new_active_spell = active_spell[:]
                new_active_spell[5] -= 1
                new_active_spells.append(new_active_spell)

        if boss_hp <= 0:
            least_mana_used = min(mana_used, least_mana_used)
            return True

        if mana_used >= least_mana_used:
            return False

        if player_turn:
            for i in range(len(spells)):
                spell = spells[i]
                spell_already_active = False
                for j in range(len(new_active_spells)):
                    if new_active_spells[j][6] == spell[6]:
                        spell_already_active = True
                        break

                spell_mana_cost = spell[0]
                if spell_mana_cost <= me_mana and not spell_already_active:
                    a = deepcopy(new_active_spells)
                    a.append(spell)
                    sim(boss_hp, boss_dmg, me_hp, me_mana - spell_mana_cost,
                        a, False, mana_used + spell_mana_cost)
        else:
            me_hp -= max(1, boss_dmg - myArmour)
            if me_hp > 0:
                sim(boss_hp, boss_dmg, me_hp, me_mana,
                    new_active_spells, True, mana_used)

    boss = [int(i.split()[-1]) for i in input.strip().split("\n")]

    sim(boss[0], boss[1], 50, 500)

    return least_mana_used


def part_two(input):
    # 0=manacost, 1=dmg, 2=hp, 3=armour, 4=mana, 5=turns, 6=index
    missile = [53, 4, 0, 0, 0, 0, 0]
    drain = [73, 2, 2, 0, 0, 0, 1]
    shield = [113, 0, 0, 7, 0, 6, 2]
    poison = [173, 3, 0, 0, 0, 6, 3]
    recharge = [229, 0, 0, 0, 101, 5, 4]
    spells = [missile, drain, shield, poison, recharge]
    global least_mana_used
    least_mana_used = maxsize

    def sim(boss_hp, boss_dmg, me_hp, me_mana,
            active_spells=[], player_turn=True, mana_used=0):

        global least_mana_used
        myArmour = 0

        if player_turn:
            me_hp -= 1
            if me_hp <= 0:
                return False

        new_active_spells = []
        for active_spell in active_spells:
            boss_hp -= active_spell[1]
            me_hp += active_spell[2]
            myArmour += active_spell[3]
            me_mana += active_spell[4]

            if active_spell[5] > 1:
                new_active_spell = active_spell[:]
                new_active_spell[5] -= 1
                new_active_spells.append(new_active_spell)

        if boss_hp <= 0:
            least_mana_used = min(mana_used, least_mana_used)
            return True

        if mana_used >= least_mana_used:
            return False

        if player_turn:
            for i in range(len(spells)):
                spell = spells[i]
                spell_already_active = False
                for j in range(len(new_active_spells)):
                    if new_active_spells[j][6] == spell[6]:
                        spell_already_active = True
                        break

                spell_mana_cost = spell[0]
                if spell_mana_cost <= me_mana and not spell_already_active:
                    a = deepcopy(new_active_spells)
                    a.append(spell)
                    sim(boss_hp, boss_dmg, me_hp, me_mana - spell_mana_cost,
                        a, False, mana_used + spell_mana_cost)
        else:
            me_hp -= max(1, boss_dmg - myArmour)
            if me_hp > 0:
                sim(boss_hp, boss_dmg, me_hp, me_mana,
                    new_active_spells, True, mana_used)

    boss = [int(i.split()[-1]) for i in input.strip().split("\n")]

    sim(boss[0], boss[1], 50, 500)

    return least_mana_used


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 953
    print(part_two(input))  # 1289
