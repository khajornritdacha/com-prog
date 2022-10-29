def letter_point(c):
    # คืนคะแนนของตัวอักษรในตัวแปร c ตามตารางที่ให้ไว้
    assert len(c) == 1
    if c in "AEILNORSTU": return 1
    if c in "DG": return 2
    if c in "BCMP": return 3
    if c in "FHVWY": return 4
    if c in "K": return 5
    if c in "JX": return 8
    if c in "QZ": return 10

    raise RuntimeError


def word_point(w):
    # คืนคะแนนของคำที่เก็บในตัวแปร w ที่หาได้จากผลรวมของคะแนนของทุกตัวอักษรใน w
    return sum([letter_point(c) for c in w])

words = input().split()
ans = []
for word in words:
    ans.append([-1 * word_point(word), word])

ans.sort()
for score, word in ans:
    print(word, score*-1)
