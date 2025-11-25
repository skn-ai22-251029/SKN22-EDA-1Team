
class Delay_Severity: # Total_Delay, Flight Distance column 기반

    def __init__(self, total_delay_col="Total_Delay", distance_col="Flight Distance"):
        self.total_delay_col = total_delay_col
        self.distance_col = distance_col

    def add_delay_severity(self, df): # DataFrame 확인 필요
        df["Delay_Severity"] = (
            df[self.total_delay_col] / df[self.distance_col] * 100 # 100마일 당 지연 시간(분)
        )

        return df





