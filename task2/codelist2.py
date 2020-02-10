
class Version:
    def __init__(self, version):
        pass
    def v(version):
        return version.__hash__()

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)



def main():
    to_test = [
        ('1.0.0', '2.0.0'),
        ('1.0.0', '1.42.0'),
        ('1.2.0', '1.2.42'),
        ('1.1.0-alpha', '1.2.0-alpha.1'),
        ('1.0.1b', '1.0.10-alpha.beta'),
        ('1.0.0-rc.1', '1.0.0'),
    ]

    # for version_1, version_2 in to_test:
    #     assert Version.v(version_1) < Version.v(version_2), 'le failed'
    #     assert Version.v(version_2) > Version.v(version_1), 'ge failed'
    #     assert Version.v(version_2) != Version.v(version_1), 'neq failed'

    for version_1, version_2 in to_test:
        print(version_1+' <  '+version_2 ,Version.v(version_1) < Version.v(version_2))
        print(version_1+' >  '+version_2, Version.v(version_2) > Version.v(version_1))
        print(version_1+' !=  '+version_2, Version.v(version_2) != Version.v(version_1))



if __name__ == "__main__":
    main()
