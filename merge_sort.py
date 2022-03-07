
def merge_sort(list):
    
    """
        O(n log n)

        Sorttaa listan kasvavassa järjestyksessä
        palauttaa uuden sortatun listan

        Divide: etsi keskipiste listasta ja jaa se pienempiin listoihin
        Conquer: rekursiivisesti sorttaa pienemmät listat
        Combine: Yhdistä sortatut pienemmät listat
    """

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    O(log n)
    Jakaa sorttaamattoman listan keskeltä pienempiin listoihin ja palauttaa ne
    """
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left,right


def merge(left, right):
    """
    O(n)
    Yhdistää kaksi listaa / arraytä, sortaten ne järjestykseen samalla, ja palauttaa uuden listan
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(list):
    n = len(list)
    if n <= 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


testi = [4,1,77,88,43,22,65,12,16,99]
sorted = merge_sort(testi)

print(verify_sorted(sorted))
print(verify_sorted(testi))
