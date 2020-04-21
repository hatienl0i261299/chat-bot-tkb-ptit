import os
from math import sqrt
import sys

data = {
    2: {
        0.5: 1.000,
        0.6: 1.375,
        0.7: 1.963,
        0.8: 3.08,
        0.9: 6.31,
        0.95: 12.71,
        0.98: 31.8,
        0.99: 63.7,
        0.999: 636.6
    },
    3: {
        0.5: 0.861,
        0.6: 1.061,
        0.7: 1.336,
        0.8: 1.886,
        0.9: 2.92,
        0.95: 4.30,
        0.98: 6.96,
        0.99: 6.92,
        0.999: 31.6
    },
    4: {
        0.5: 0.765,
        0.6: 0.978,
        0.7: 1.250,
        0.8: 1.638,
        0.9: 2.35,
        0.95: 3.18,
        0.98: 4.54,
        0.99: 5.84,
        0.999: 12.9
    },
    5: {
        0.5: 0.741,
        0.6: 0.941,
        0.7: 1.190,
        0.8: 1.533,
        0.9: 2.13,
        0.95: 2.77,
        0.98: 3.75,
        0.99: 4.60,
        0.999: 8.61
    },
    6: {
        0.5: 0.737,
        0.6: 0.920,
        0.7: 1.156,
        0.8: 1.476,
        0.9: 2.02,
        0.95: 2.57,
        0.98: 3.36,
        0.99: 4.03,
        0.999: 6.86
    },
    7: {
        0.5: 0.718,
        0.6: 0.906,
        0.7: 1.134,
        0.8: 1.440,
        0.9: 1.943,
        0.95: 2.45,
        0.98: 3.14,
        0.99: 4.71,
        0.999: 5.96
    },
    8: {
        0.5: 0.711,
        0.6: 0.896,
        0.7: 1.119,
        0.8: 1.415,
        0.9: 1.895,
        0.95: 2.36,
        0.98: 3.00,
        0.99: 3.5,
        0.999: 5.40
    },
    9: {
        0.5: 0.706,
        0.6: 0.889,
        0.7: 1.108,
        0.8: 1.397,
        0.9: 1.860,
        0.95: 2.31,
        0.98: 2.90,
        0.99: 3.36,
        0.999: 5.04
    },
    10: {
        0.5: 0.703,
        0.6: 0.883,
        0.7: 1.110,
        0.8: 1.383,
        0.9: 1.833,
        0.95: 2.26,
        0.98: 2.82,
        0.99: 3.25,
        0.999: 4.78
    },
}


def abcdef(lst):
    # TODO: Buoc 1 tinh trung binh
    trungbinh = sum(lst) / len(lst)
    sys.stdout.write("Trung binh cong %s\n" % trungbinh)

    # TODO: Buoc 2 tinh sai so du
    lst_sai_so_du = []
    for i in range(len(lst)):
        ep = abs(lst[i] - trungbinh)
        lst_sai_so_du.append(ep)
    sys.stdout.write("Sai so du %s\n" % lst_sai_so_du)

    # TODO: Buoc 3 tinh sai so trung binh binh phuong
    _epsilon = sqrt(sum([i ** 2 for i in lst_sai_so_du]) / (len(lst_sai_so_du) - 1))
    m = data.get(len(lst_sai_so_du)).get(ptc) * _epsilon
    sys.stdout.write("Sai so trung binh binh phuong %s\n" % m)

    # TODO: Buoc 4 kiem tra sai so
    for i in range(len(lst_sai_so_du)):
        if lst_sai_so_du[i] > m:
            sys.stdout.write("Xoa %s la phan tu sai\n" % lst[i])
            lst.remove(lst[i])
            break
    else:
        sys.stdout.write("Het phan tu sai\n")
        return lst, _epsilon, trungbinh
    sys.stdout.write('\n')
    return abcdef(lst)


TEST_CASE = [
    {
        "name": "Bai 2.16",
        "n": 5,
        "ptc": 0.8,
        "list": [20.50, 21.35, 21.25, 10.25, 20.75]
    },
    {
        "name": "Bai 2.17",
        "n": 7,
        "ptc": 0.9,
        "list": [280.50, 282.40, 277.60, 281.75, 278.25, 279.50, 105.00]
    },
    {
        "name": "Bai 2.18",
        "n": 6,
        "ptc": 0.95,
        "list": [480.00, 482.40, 477.60, 481.75, 488.25, 115.00]
    },
    {
        "name": "Acbdefghi",
        "n": 7,
        "ptc": 0.8,
        "list": [20, 21.1, 21.2, 25.6, 10, 22.2, 23.7]
    }
]

if __name__ == '__main__':
    os.system('cls')
    for test in TEST_CASE:
        sys.stdout.write(f"\t{test.get('name')}\n")
        # sys.stdout.write("Nhap n >> ")
        # n = int(input())
        # sys.stdout.write("Nhap Ptc >> ")
        # ptc = float(input())

        n = test.get('n')
        ptc = test.get("ptc")
        lst = test.get("list")
        # lst = []
        # for i in range(n):
        #     sys.stdout.write(f"Nhap phan tu {i + 1} >> ")
        #     lst.append(float(input()))

        sys.stdout.write("Cac ket qua do %s\n\n" % lst)
        lst, epsilon, trungbinh = abcdef(lst)
        sys.stdout.write(
            'Ket qua do : %s +- %s * %s\n' % (trungbinh, data.get(len(lst)).get(ptc), epsilon / sqrt(len(lst))))
        sys.stdout.write("List phan tu sau khi remove %s" % lst)
        sys.stdout.write('\n\n\n\n')
