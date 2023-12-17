class DoubleAnharmonicity:
    def __init__(self, first_begin = 1000, first_end = 2000, second_begin = 2000, second_end = 4000):
        self.first_begin = first_begin
        self.first_end = first_end
        self.second_begin = second_begin
        self.second_end = second_end

    def apply_anharmanonism(self, df, coef1 = 1, coef2 = 1): 
        df['xAnharm'] = df.apply(lambda x: self.__do_anharmonism(df['X']), axis =  1)
        return df
    
    def __do_anharmonism(self, x, coef1 = 1, coef2 = 1):
        if self.first_begin < x < self.first_end:
            return x * coef1
        elif self.second_begin < x < self.second_end:
            return x * coef2