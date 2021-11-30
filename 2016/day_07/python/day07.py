from aoc import AOC


aoc = AOC(year=2016, day=7)
data = aoc.load()


## Part 1

support_tls = 0

for ip in data.lines():
    inside_brackets = False
    is_valid = False
    for letter_idx in range(len(ip) - 3):
        if ip[letter_idx] == "[":
            inside_brackets = True
            continue
        if ip[letter_idx] == "]":
            inside_brackets = False
            continue

        if (
            ip[letter_idx] == ip[letter_idx + 3]
            and ip[letter_idx + 1] == ip[letter_idx + 2]
            and ip[letter_idx] != ip[letter_idx + 1]
        ):
            if inside_brackets:
                is_valid = False
                break
            if is_valid < 1:
                is_valid = True

    if is_valid:
        support_tls += 1

aoc.p1(support_tls)


## Part 2


support_ssl = 0

for ip in data.lines():
    abas = {}
    babs = {}
    inside_brackets = False
    for letter_idx in range(len(ip) - 2):
        if ip[letter_idx] == "[":
            inside_brackets = True
            continue
        if ip[letter_idx] == "]":
            inside_brackets = False
            continue

        if (
            ip[letter_idx] == ip[letter_idx + 2]
            and ip[letter_idx] != ip[letter_idx + 1]
        ):
            code = ip[letter_idx : letter_idx + 3]
            corresponding_code = code[1] + code[0] + code[1]
            if inside_brackets:
                babs[code] = letter_idx
                if corresponding_code in abas:
                    support_ssl += 1
                    break
            else:
                abas[code] = letter_idx
                if corresponding_code in babs:
                    support_ssl += 1
                    break

aoc.p2(support_ssl)
