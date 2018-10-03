def power2_digit_sum(n):
    assert n > 10
    power = [4, 2, 0, 1]
    carry = False
    for i in range(11, n + 1):
        if i % (n / 10) == 0:
            print(i / (n / 100), "%")
        for j in range(len(power)):
            new = (power[j] * 2 + (1 if carry else 0)) % 10
            carry = power[j] > 4
            power[j] = new
        if carry:
            carry = False
            power.append(1)
    return sum(power)

if __name__ == '__main__':
    print(power2_digit_sum(1000))
