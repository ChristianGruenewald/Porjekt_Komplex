class Komplex:
    RE=0.0
    IM=0.0

    def __add__(self, other):
        return self.RE+other.RE, self.IM+other.IM

    def __

    def __init__(self, RE,IM):
        self.RE=RE
        self.IM=IM

    def Add(self,RE2,IM2):
        self.RE=self.RE+RE2
        self.IM=self.IM+IM2

    def OUTPUT(self):
        print(str(self.RE) + "+" +"j"+str(self.IM))