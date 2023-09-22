import schemdraw
import schemdraw.elements as elm


with schemdraw.Drawing() as ckt:

    ckt += elm.Dot(open=True).label('12V', loc='right')
    ckt += elm.Resistor('down').label(r'$R_D$', loc='top').label(r'$2\ k\Omega$', loc='bot').length(4)
    ckt += elm.Dot()
    ckt.push()
    ckt += elm.Line().length(.8)
    ckt += elm.Dot().label('D', loc='right')
    ckt += (mos:=elm.NMos('right', circle=True, fill='#88ccff')).label('$I_{D(on)} = 6\ mA$', ofst=[.4,.5]).label('$V_{GS(on)} = 8\ V$', ofst=[.4,0]).label('$V_{GS(Th)} = 3\ V$', ofst=[.4,-.5])
    ckt += elm.Dot().at(mos.source).label('S', loc='right')
    ckt += elm.Line('down').length(2)
    ckt += elm.Ground()

    ckt.pop()
    ckt.push()

    ckt += elm.Capacitor2('right').length(4).label('$C_2$').label('$1\ \mu F$', loc='bot')
    ckt += elm.Dot(open=True).label('$V_o$', loc='right')

    ckt.pop()

    ckt += elm.Resistor('left').label('$R_G$').label('$10\ M\Omega$', loc='bot')
    ckt += elm.Line('down').length(1.3)

    ckt += elm.Dot().label('G', loc='top').at(mos.gate)
    ckt += elm.Line('left').length(2.18)
    ckt += elm.Dot()

    ckt += elm.Capacitor2('left').length(4).label('$C_1$').label('$1\ \mu F$', loc='bot')
    ckt += elm.Dot(open=True).label('$V_i$', loc='left')

    ckt.save('Fig7.40_ElecDevice_RBoylstadPg445_11E.pdf')
    ckt.draw()