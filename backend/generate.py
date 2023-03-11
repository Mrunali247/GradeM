import pandas as pd
import statistics


class GenResult:
    def __init__(self, filename: str, typeR: str):
        self.typeR = typeR
        self.grades = ["AA", "AB", "BB", "BC", "CC", "CD", "FF"]
        self.filename = filename
        self.data = pd.read_excel(filename)
        self.cols = len(self.data.axes[1])
        self.rows = len(self.data.axes[0])
        self.totalCol = self.data[self.data.columns[-1]].tolist()

    def printData(self):
        # print(self.data)
        print(self.totalCol)

    def getAverage(self):
        avg = sum(self.totalCol)/self.rows
        return avg

    def getStandardDev(self):
        stdDev = statistics.stdev(self.totalCol, self.getAverage())
        return stdDev

    def getRange(self):
        if self.typeR == "abs":
            return self.getAbsR()
        else:
            return self.getRelR()

    def getRelR(self):
        av = self.getAverage()
        std = self.getStandardDev()
        if (av + (1.5 * std)) < 100:
            m = av - (1.0 * std)
            if (av - (1.0 * std)) > 40:
                m = 40
            rangeM = [av + (1.5 * std), av + (1.0 * std), av + (0.5 * std), av, av - (0.5 * std),m]
            return rangeM
        else:
            return self.getAbsR()

    def getAbsR(self):
        av = self.getAverage()
        rangeM = [90, 80, 70, 60, 50, 40]
        return rangeM