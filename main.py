from prettytable import PrettyTable
from math import sqrt, pow

class observation_table:
    def __init__(self, inlet_pressure, P1, P2, Speed, Hanger_weight, Spring_balance, Vaccum_Pressure):
        self.inlet_pressure = inlet_pressure
        self.P1 = P1
        self.P2 = P2
        self.Speed = Speed
        self.Hanger_weight = Hanger_weight
        self.Spring_balance = Spring_balance
        self.Vaccum_Pressure = Vaccum_Pressure

    def Table(self):
        columns = ["Inlet Pressure Kg/cm2", "P1 (m of water)", "P2 (m of water)", "Speed 'N' (rpm)", "Hanger Weight (T1)(kg)", "Spring Balance (T2)(kg)", "Vaccum Pressure (kg/cm2)"]
        mytable = PrettyTable()

        #add columns
        mytable.add_column(columns[0], self.inlet_pressure)
        mytable.add_column(columns[1], self.P1)
        mytable.add_column(columns[2], self.P2)
        mytable.add_column(columns[3], self.Speed)
        mytable.add_column(columns[4], self.Hanger_weight)
        mytable.add_column(columns[5], self.Spring_balance)
        mytable.add_column(columns[6], self.Vaccum_Pressure)

        print(mytable)

# for operating characteristics
def operating(number_of_inputs):
    print("Enter the readings")
    inlet_pressure = []
    P1 = []
    P2 = []
    Speed = []
    Hanger_weight = []
    Spring_balance = []
    Vaccum_Pressure = []
    d = int(input("Enter the speed: "))
    for i in range(number_of_inputs):
        a = float(input("Inlet Pressure: "))
        print("Venturimeter readings: ")
        b = float(input("P1: "))
        c = float(input("P2: "))
        e = float(input("Hanger Weight: "))
        f = float(input("Spring Balance: "))
        g = float(input("Vaccum Pressure: "))
        print("\n\n")
        inlet_pressure.append(a)
        P1.append(b)
        P2.append(c)
        Speed.append(d)
        Hanger_weight.append(e)
        Spring_balance.append(f)
        Vaccum_Pressure.append(g)
    Table = observation_table(inlet_pressure, P1, P2, Speed, Hanger_weight, Spring_balance, Vaccum_Pressure)
    Table.Table()
    return [inlet_pressure, P1, P2, Speed, Hanger_weight, Spring_balance, Vaccum_Pressure]

def main_characteristics(number_of_inputs):
    print("Enter the readings")
    inlet_pressure = []
    P1 = []
    P2 = []
    Speed = []
    Hanger_weight = []
    Spring_balance = []
    Vaccum_Pressure = []
    a = float(input("Inlet Pressure: "))
    print("Venturimeter readings: ")
    b = float(input("P1: "))
    c = float(input("P2: "))
    for i in range(number_of_inputs):
        d = int(input("Enter the speed: "))
        e = float(input("Hanger Weight: "))
        f = float(input("Spring Balance: "))
        g = float(input("Vaccum Pressure: "))
        print("\n\n")
        inlet_pressure.append(a)
        P1.append(b)
        P2.append(c)
        Speed.append(d)
        Hanger_weight.append(e)
        Spring_balance.append(f)
        Vaccum_Pressure.append(g)
    Table = observation_table(inlet_pressure, P1, P2, Speed, Hanger_weight, Spring_balance, Vaccum_Pressure)
    Table.Table()
    return [inlet_pressure, P1, P2, Speed, Hanger_weight, Spring_balance, Vaccum_Pressure]

def calculation(number_of_inputs , inlet_pressure, P1, P2, Speed, Hanger_weight, Spring_balance):
    Net_weight_l = []
    Discharge_l = []
    Head_l = []
    Pressure_diff_l = []
    Output_power_l = []
    input_Power_l = []
    unit_power_l = []
    unit_speed_l = []
    unit_discharge_l = []
    efficiency_l = []
    for i in range(number_of_inputs):
        Pressure_diff = (P1[i]-P2[i])*10
        Discharge = 0.0131*(Pressure_diff**0.5)
        Head = inlet_pressure[i]*10
        input_Power = 1000*Discharge*9.81*Head
        Net_weight = Hanger_weight[i]-Spring_balance[i]
        Resultant_load = Net_weight*9.81
        Output_power = 3.142*0.3*Speed[i]*Resultant_load/60
        efficiency = (Output_power/input_Power)*100
        unit_speed = Speed[i]/sqrt(Head)
        unit_discharge = Discharge/sqrt(Head)
        unit_power = Output_power/pow(Head, 3/2)
        Net_weight_l.append(Net_weight)
        Discharge_l.append(Discharge)
        Head_l.append(Head)
        Pressure_diff_l.append(Pressure_diff)
        Output_power_l.append(Output_power)
        input_Power_l.append(input_Power)
        unit_power_l.append(unit_power)
        unit_speed_l.append(unit_speed)
        unit_discharge_l.append(unit_discharge)
        efficiency_l.append(efficiency)
    return Net_weight_l, Discharge_l, Head_l, Pressure_diff_l, Output_power_l, input_Power_l, unit_power_l, unit_speed_l, unit_discharge_l, efficiency_l

def operating_table(net_wt,discharge,head,dh,out_power,in_power,efficiency):
    mytable = PrettyTable()
    columns = ["Net Wt. (kg)", "Discharge Q (m3/sec)", "H (M of water)", "Dh (kg/cm2)", "Output power", "Input Power", "Efficiency"]
    
    # add columns
    mytable.add_column(columns[0], net_wt)
    mytable.add_column(columns[1], discharge)
    mytable.add_column(columns[2], head)
    mytable.add_column(columns[3], dh)
    mytable.add_column(columns[4], out_power)
    mytable.add_column(columns[5], in_power)
    mytable.add_column(columns[6], efficiency)
    print(mytable)
    return


def main_table(net_wt, discharge, head, dh, out_power, in_power, unit_power, unit_speed, unit_discharge , efficiency):
    mytable = PrettyTable()
    columns = ["Net Wt. (kg)", "Discharge Q (m3/sec)", "H (M of water)", "Dh (kg/cm2)", "Output power", "Input Power",
               "Unit Power", "Unit Speed", "Unit Discharge", "Efficiency"]

    # add columns
    mytable.add_column(columns[0], net_wt)
    mytable.add_column(columns[1], discharge)
    mytable.add_column(columns[2], head)
    mytable.add_column(columns[3], dh)
    mytable.add_column(columns[4], out_power)
    mytable.add_column(columns[5], in_power)
    mytable.add_column(columns[6], unit_power)
    mytable.add_column(columns[7], unit_speed)
    mytable.add_column(columns[8], unit_discharge)
    mytable.add_column(columns[9], efficiency)
    print(mytable)
    return

number_of_inputs = int(input("Enter number of inputs: "))
operating_char = operating(number_of_inputs)
cal_oper = calculation(number_of_inputs,operating_char[0],operating_char[1],operating_char[2],operating_char[3],operating_char[4],operating_char[5])
main_charac = main_characteristics(number_of_inputs)
cal_main = calculation(number_of_inputs,main_charac[0],main_charac[1],main_charac[2],main_charac[3],main_charac[4],main_charac[5])
operating_table(cal_oper[0],cal_oper[1], cal_oper[2], cal_oper[3], cal_oper[4],cal_oper[5], cal_oper[9])
main_table(cal_main[0],cal_main[1], cal_main[2], cal_main[3], cal_main[4],cal_main[5], cal_main[6], cal_main[7], cal_main[8], cal_main[9])
