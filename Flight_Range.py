class FlightRangeProcessor:
    '''
    비행거리를 기반으로 단거리/중거리/장거리 구간을 생성하는 클래스
    '''
    def __init__(self):
        # 구간 기준 설정 [0, 1000, 2500,float('inf')]
        # 범위 설정에서 오른쪽 값은 미포함 
        self.bins = [0, 1000, 2500, float('inf')]
        self.labels = ['Short_Haul','Medium_Haul','Long_Haul']
        

    def process(self, df: pd.DataFrame) -> pd.DataFrame:
        print("Processing Flight Range...")

        df['Flight_Range'] = pd.cut(
            df['Flight Distance'],
            bins=self.bins,
            labels=self.labels
            right=self.right
        )
        return df

