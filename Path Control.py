def on_forever():
    if Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.WHITE) and Tinybit.Line_Sensor(Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.WHITE):
        Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_RUN, 30, 30)
    elif Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.BLACK) and Tinybit.Line_Sensor(Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.WHITE):
        Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_RUN, 20, 110)
    elif Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.WHITE) and Tinybit.Line_Sensor(Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.BLACK):
        Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_RUN, 110, 20)
    else:
        Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_RUN, 30, 60)
basic.forever(on_forever)
