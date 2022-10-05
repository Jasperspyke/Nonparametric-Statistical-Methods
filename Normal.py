import scipy.stats

xbar = 9.5
mu0 = 10
s = 0.38

# Normal testing
class Dataset:
    def __init__(self, x, mew, sd):
        self.x = x
        self.mew = mew
        self.sd = sd
        self.z = None
        self.area = None
        self.two_tailed = None

    def set_z(self, x, mew, sd):
        self.z = (x - mew) / sd

    def set_two_tailed(self, boo):
        self.two_tailed = bool(boo)
        print('two tailed attribute set to', + self.two_tailed)

    def get_z(self):
        print('the z score is', + self.z)
        return self.z

    def get_area(self, z_score):
        self.area = 1 - scipy.stats.norm.cdf(z_score)
        if not self.two_tailed:
            self.area = 2 * self.area
        print('normal area is', + self.area)
        return self.area

    def get_p_value(self, z):
        p = scipy.stats.norm.sf(abs(z))
        if self.two_tailed:
            p *= 2
        print('the p value is ' + str(p))
        return p


