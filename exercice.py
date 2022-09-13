#!/usr/bin/env python


def dissipated_power(voltage, resistance):
    # TODO: Calculer la puissance dissipée par la résistance.
    p = (voltage ** 2) / resistance
    return p


def orthogonal(v1, v2):
    # TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
    scalar = v1[0] * v2[0] + v1[1] * v2[1]
    return scalar == 0


def average(values):
    # TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
    # for v in values:
    #     pass  # La variable v contient une valeur de la liste.
    _values = [x for x in values if x >= 0]
    return sum(_values) / len(_values)


def bills(value):
    # TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
    _bills = [0, 0, 0, 0, 0]
    while value != 0:
        if value >= 20:
            _bills[0] += 1
            value -= 20
        elif value >= 10:
            _bills[1] += 1
            value -= 10
        elif value >= 5:
            _bills[2] += 1
            value -= 5
        elif value >= 1:
            _bills[3] += 1
            value -= 1
    return _bills[0], _bills[1], _bills[2], _bills[3]


def format_base(value, base, digit_letters):
    # Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
    # `digits_letters[0]. ` Nous donne la lettre pour le chiffre 0, ainsi de suite.
    result = ""
    abs_value = abs(value)
    while abs_value != 0:
        digit = abs_value % base
        result = digit_letters[digit] + result
        abs_value //= base
    if value < 0:
        # TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
        result = '-' + result

    return result


if __name__ == "__main__":
    print(dissipated_power(69, 420))
    print(orthogonal((1, 1), (-1, 1)))
    print(average([1, 4, -2, 10]))
    print(bills(137))
    print(format_base(-42, 16, "0123456789ABCDEF"))
