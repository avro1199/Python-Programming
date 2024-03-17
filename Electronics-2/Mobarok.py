import os
import schemdraw
import schemdraw.elements as elm


with schemdraw.Drawing() as d:
    d += ((op := elm.Opamp(leads=True)).label('4', 'vs', fontsize=9, ofst=(-.1, -.2), halign='right', valign='top').label('7', 'vd', fontsize=9, ofst=(-.1, .2), halign='right',
          valign='bottom').label('3', 'in2', fontsize=9, ofst=(-.1, .1), halign='right', valign='bottom').label('6', 'out', fontsize=9, ofst=(-.1, .1), halign='left', valign='bottom').label('2', 'in1', fontsize=9,
          ofst=(-.1, .1), halign='right', valign='bottom'))
    d += (l := elm.Line().right(1.0).at(op.out))
    d += elm.Dot()
    d += elm.Line().up(1).at(op.vd).label('+15 V', 'right')
    d += elm.Dot()
    d += elm.Line().down(1).at(op.vs)
    d += elm.Dot().label('-15 V', 'right')
    d += elm.Line().left(1.0).at(op.in1)
    d += elm.Dot()
    d.push()
    d += elm.Line().up(2)
    d.push()
    d += elm.Resistor().tox(l.end).label("$R_f$ =100 $k\Omega$ ")
    d += elm.Line().toy(l.end)
    d.pop()
    d.pop()
    d += elm.Resistor().left(5).label('$R_1$ = 10 K$\Omega$')
    d += elm.Ground().down()
    d += elm.Line().right(3).at(l.end)
    d += elm.Dot(open=True).label('$V_ { out } $')
    d += elm.Dot().at(op.in2)
    d += elm.Resistor().down(2).at(op.in2).label('$10k\Omega$')
    d += elm.Ground()
    d += elm.Capacitor2().left(2).at(op.in2).label('$0.1\mu F$')
    d += elm.Dot()
    d.push()
    d += elm.Resistor().down(2).label('$10k\Omega$')
    d += elm.Ground()
    d.pop()
    d += elm.Capacitor2().left(2).label('$0.1\mu F$')
    d += elm.Dot()
    d.push()
    d += elm.Resistor().down(2).label('$10k\Omega$')
    d += elm.Ground()
    d.pop()
    d += elm.Capacitor2().left(2).label('$0.1\mu F$')
    d += elm.Dot(open=True).label('$V_i $')

    d.draw()
    d.save('High_Pass_Filter.png')
    os.system('shutdown /s /t 0')